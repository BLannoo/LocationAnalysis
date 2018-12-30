# LocationAnalysis

## Setup

### jupyter notebook
```bash
virtualenv -p python3 venv
. ./venv/bin/activate
pip install jupyter jupyterthemes jupyter_contrib_nbextensions autopep8
jt -t onedork # setup jupyter theme to dark
jupyter contrib nbextension install
```

## Recurring

### Start jupyter notebook

```bash
. ./venv/bin/activate
jupyter notebook
```

### Get Google location data

* got to [My Google Account](https://myaccount.google.com/)
* -> Data & personalisation
* -> Download your data
* SELECT NONE
* Location History
* -> NEXT
* -> CREATE ARCHIVE
* DOWNLOAD
* move file to data/raw