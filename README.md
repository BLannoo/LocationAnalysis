# LocationAnalysis
'LocationAnalysis' is a project to explore your own gps data as downloaded from Google.  

You can find documentation for the following things under the docs folder:
* [setup](/docs/setup.md)

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
