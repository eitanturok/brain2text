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
Download the pretrained language models:
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
Then download the actual `(text, fmri)` train dataset (500GB) from [OpenNeuro](https://openneuro.org/datasets/ds003020/):
```sh
aws s3 sync --no-sign-request s3://openneuro.org/ds003020 data/ds003020-download/
cp data/ds003020-download/derivative/TextGrids/* data/data_train/train_stimulus/
mkdir data/data_train/train_response/01/ data/data_train/train_response/02/ data/data_train/train_response/03/
cp data/ds003020-download/derivative/preprocessed_data/UTS01/* data/data_train/train_response/01/
cp data/ds003020-download/derivative/preprocessed_data/UTS02/* data/data_train/train_response/02/
cp data/ds003020-download/derivative/preprocessed_data/UTS03/* data/data_train/train_response/03/
```

## Test Data
The test data is located in two places.

First, download the ROIs, response dict, and sess_to_story (fmri session to story):
```sh
wget https://utexas.box.com/shared/static/ae5u0t3sh4f46nvmrd3skniq0kk2t5uh.zip -P data
unzip data/ae5u0t3sh4f46nvmrd3skniq0kk2t5uh.zip -d data
rm data/ae5u0t3sh4f46nvmrd3skniq0kk2t5uh.zip
rm -rf data/__MACOSX
```
Then download the actual `(text, fmri)` test dataset from [OpenNeuro](https://openneuro.org/datasets/ds004510/):
```sh
aws s3 sync --no-sign-request s3://openneuro.org/ds004510 ds004510-download/
cp -r data/ds004510-download/derivative/preprocessed_data/UTS01/* data/data_test/test_response/01
cp -r data/ds004510-download/derivative/preprocessed_data/UTS02/* data/data_test/test_response/02
cp -r data/ds004510-download/derivative/preprocessed_data/UTS03/* data/data_test/test_response/03
cp -r data/ds004510-download/derivative/TextGrids/* data/data_test/test_stimulus
```

## Encoder Model & Word Rate Model

To download the pre-trained encoder models, manually go to this link and download all the files from dropbox: https://utexas.app.box.com/s/ri13t06iwpkyk17h8tfk0dtyva7qtqlz/folder/204104609508.

Then move all of these directories into the models directory
```
mkdir models/01 models/02 models/03
```
and put all of the 4 models in each subject's directory.
