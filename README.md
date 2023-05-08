
# TianGong Knowledge Base

## Env Preparing

Install `Python 3.10`

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10
```

Setup `venv`:

```bash
sudo apt install python3.10-venv
python3.10 -m venv .venv
source .venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt --upgrade
```

## Env Preparing in MacOS

Install `Python 3.10`

```bash
brew update
brew install python@3.10
```

Setup `venv`:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

## Run Streamlit

```bash
streamlit run Home.py
```
