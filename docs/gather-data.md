# Gather gps location data from Google
1) Request your data from Google
    a) go to [My Google Account](https://myaccount.google.com/)
    b) -> Data & personalisation
    c) -> Download your data
        * Deselect all
        * Location History
    d) -> Next step
    e) -> Create export
2) Wait for Google to notify you by e-mail
3) Download your data from Google too this project
    a) Open e-mail: "Your Google data archive is ready"
    b) -> Download archive
    c) move file to data/raw/MyGoogleData
        `mv ~/Downloads/takeout-*.zip ./data/raw/MyGoogleData`
    d) remove old unziped data
        `rm -R ./data/raw/MyGoogleData/Takeout`
    e) unzip file
        (open it in your file explorer)

## Filter out a sample of the data
TODO: make a script for this
* make a copy named LocationHistory2018.json in data
* open file (to big for intellij use visual studio code)
* search for 1514764811728 (01/01/2018 @ 12:00am (UTC))
* remove all data older (bellow) then this

# Gather Belgian maps (shape files)
* go to [mapcruzin](https://mapcruzin.com/free-belgium-arcgis-maps-shapefiles.htm)
* download: Belgium Roads
* move file to data/raw/Belgium
* unzip file (opening it in Finder)