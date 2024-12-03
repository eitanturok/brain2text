import argparse, json, os, sys

import numpy as np
from icecream import ic, install
install()

sys.path.append("semantic-decoding/decoding") # To import from "semantic-decoding/decoding"
import config
from utils_ridge.textgrid import TextGrid

BAD_WORDS_PERCEIVED_SPEECH = frozenset(["sentence_start", "sentence_end", "br", "lg", "ls", "ns", "sp"])
BAD_WORDS_OTHER_TASKS = frozenset(["", "sp", "uh"])
TEST_N_SAMPLES = 10

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--subject", type=str, default='01')
    parser.add_argument("--experiment", type=str, default='perceived_speech')
    parser.add_argument("--task", type=str, default='wheretheressmoke')
    parser.add_argument("--metrics", nargs="+", type=str, default=["WER", "BLEU", "METEOR", "BERT"])
    parser.add_argument("--null", type=int, default=10)
    parser.add_argument("--n_samples", type=int, default=-1)
    parser.add_argument('--start', type=int, default=0)
    args = parser.parse_args()
    return args


def load_transcript(experiment, task):
    skip_words = BAD_WORDS_PERCEIVED_SPEECH if experiment in ["perceived_speech", "perceived_multispeaker"] else BAD_WORDS_OTHER_TASKS
    grid_path = os.path.join(config.DATA_TEST_DIR, "test_stimulus", experiment, task.split("_")[0] + ".TextGrid")
    with open(grid_path, mode='r', encoding='utf=8') as f: grid = TextGrid(f.read())
    idx = experiment == "perceived_speech"
    transcript = grid.tiers[idx].make_simple_transcript()
    transcript = [(float(s), float(e), w.lower()) for s, e, w in transcript if w.lower().strip("{}").strip() not in skip_words]
    words = np.array([x[2] for x in transcript])
    times = np.array([(x[0] + x[1]) / 2 for x in transcript])
    return words, times


def windows(task, step=1):
    """Return windows of `duration` seconds at each time point. Here `duration` is `config.WINDOW`."""
    with open(os.path.join(config.DATA_TEST_DIR, "eval_segments.json"), "r") as f: eval_segments = json.load(f)
    start_time, end_time, half = *tuple(map(int, eval_segments[task])), int(config.WINDOW / 2)
    return [(center - half, center + half) for center in range(start_time + half, end_time - half + 1) if center % step == 0]


def segment_data(data, times, cutoffs):
    """divide [data] into list of segments defined by [cutoffs]"""
    return [[x for c, x in zip(times, data) if c >= start and c < end] for start, end in cutoffs]


def main(args):

    # load predicted/true words, times
    pred_path = os.path.join(config.RESULT_DIR, args.subject, args.experiment, args.task + "_39.npz")
    pred_data = np.load(pred_path)
    pred_words, pred_times = pred_data["words"], pred_data["times"]
    ref_words, ref_times = load_transcript(args.experiment, args.task)
    def _trim(x, s=args.start, n=args.n_samples): return x[s:s+n]
    pred_words, pred_times, ref_words, ref_times = _trim(pred_words), _trim(pred_times), _trim(ref_words), _trim(ref_times)
    assert len(pred_words) == len(pred_times) == len(ref_words) == len(ref_times) == args.n_samples
    ic(pred_times, ref_times)

    # segment prediction and reference words into windows
    window_cutoffs = windows(args.task)
    ref_windows = segment_data(ref_words, ref_times, window_cutoffs)
    pred_windows = segment_data(pred_words, pred_times, window_cutoffs)
    print(window_cutoffs)
    print(ref_windows)
    print(pred_windows)


if __name__ == '__main__':
    main(args())
