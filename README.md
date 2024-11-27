# brain2text
I can read your mind!!!

# Setup

```sh
# clone semantic-decoding repo
git clone https://github.com/eitanturok/semantic-decoding.git
cd semantic-decoding
git switch dev
cd ..

# clone brain2text repo
git clone https://github.com/eitanturok/brain2text.git
cd brain2text
ln -s ../semantic-decoding .

# virtual environment
uv venv --python 3.12
source .venv/bin/activate
uv pip install -e .
```

# Download data for `semantic-decoding`
1. Go to the `brain2text` directory.
2. Install dev requirements: `uv pip install -e ".[dev]"`.

## Language Model
Download the language models:
```sh
mkdir data
wget https://utexas.box.com/shared/static/7ab8qm5e3i0vfsku0ee4dc6hzgeg7nyh.zip -P data
unzip data/7ab8qm5e3i0vfsku0ee4dc6hzgeg7nyh.zip -d data
rm data/7ab8qm5e3i0vfsku0ee4dc6hzgeg7nyh.zip
```

## Training Data
The training data is located in two places.

First, download the ROIs, response dict, and sess_to_story (fmri session to story):
```sh
wget https://utexas.box.com/shared/static/3go1g4gcdar2cntjit2knz5jwr3mvxwe.zip -P data
unzip data/3go1g4gcdar2cntjit2knz5jwr3mvxwe.zip -d data
rm data/3go1g4gcdar2cntjit2knz5jwr3mvxwe.zip
rm -rf data/__MACOSX
```
Then download the actual `(text, fmri)` dataset (53GB) from [OpenNeuro](https://openneuro.org/datasets/ds004510/):
```sh
aws s3 sync --no-sign-request s3://openneuro.org/ds003020 data/ds003020-download/
cp data/ds003020-download/derivative/TextGrids/* data/data_train/train_stimulus/
mkdir data/data_train/train_response/01/ data/data_train/train_response/02/ data/data_train/train_response/03/
cp data/ds003020-download/derivative/preprocessed_data/UTS01/* data/data_train/train_response/01/
cp data/ds003020-download/derivative/preprocessed_data/UTS02/* data/data_train/train_response/02/
cp data/ds003020-download/derivative/preprocessed_data/UTS03/* data/data_train/train_response/03/
```
