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

### python requirements
```bash
pip install -r requirements.txt
```


## Recurring

### Start jupyter notebook
```bash
. ./venv/bin/activate
jupyter notebook
```

### Get Google location data
* go to [My Google Account](https://myaccount.google.com/)
* -> Data & personalisation
* -> Download your data
* SELECT NONE
* Location History
* -> NEXT
* -> CREATE ARCHIVE
* DOWNLOAD
* move file to data/raw/MyGoogleData
* unzip file (opening it in Finder)

### Filter 2018 data
* make a copy named LocationHistory2018.json in data
* open file (to big for intellij use visual studio code)
* search for 1514764811728 (01/01/2018 @ 12:00am (UTC))
* remove all data older (bellow) then this

### Download shape files
* go to [mapcruzin](https://mapcruzin.com/free-belgium-arcgis-maps-shapefiles.htm)
* download: Belgium Roads
* move file to data/raw/Belgium
* unzip file (opening it in Finder)
