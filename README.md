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

# Data from `semantic-decoding`
Download data for semantic-decoding. You should already be inside the brain2text directory.

## Language Model Data
```sh
mkdir data
wget https://utexas.box.com/shared/static/7ab8qm5e3i0vfsku0ee4dc6hzgeg7nyh.zip -P data
unzip data/7ab8qm5e3i0vfsku0ee4dc6hzgeg7nyh.zip -d data
rm data/7ab8qm5e3i0vfsku0ee4dc6hzgeg7nyh.zip
```

## Training Data
```sh
wget https://utexas.box.com/shared/static/3go1g4gcdar2cntjit2knz5jwr3mvxwe.zip -P data
unzip data/3go1g4gcdar2cntjit2knz5jwr3mvxwe.zip -d data
rm data/3go1g4gcdar2cntjit2knz5jwr3mvxwe.zip
rm -rf data/__MACOSX
```


