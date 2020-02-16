# Exploratory data analysis

## 2018-12-30 19h->21h: Geopandas.ipynb
1) Q: In what countries have I been?
    * A: Visualy: 
        * Belgium and south of it
        * Georgia
        * Abu Dhabi
        * South-east Asia
    * A: In Numbers
        * 87.7% Belgium
        * 4.6% Georgia
        * 2.2% Vietnam
        * ...
2) Q: Where have I been in Leuven?
    * A: Everywhere inside the ring
    * A: Many places around the ring

## 2018-12-30 22h->23h: roads_data_overlay.ipynb
1) Q: Where have I been inside Belgium?
    * A: 1 path towards Kortrijk + coast
    * A: Couple of paths towards the Ardenes
    * A: Many paths towards the Kempen
2) Q: Where was I on 2018/12/25? (can I show 1 day)
    * A: From Leuven to Kortrijk. (yes)

## 2018-12-30: PlayGround.ipynb
1) Q: How much variance is there in my position per hour?
    * A: 0 and |---|e^0|e^30|---|
2) Q: How much variability is there in my movement?
    * A: 0 and |---|e^-5|e^10|---|
3) Q: How are the time intervals between measurements over the time of the day?
    * A: some patterns, but nothing obvious

## 2018-12-30: Working.ipynb
1) Q: When are measurements taken during the day?
    * A: Less at night
2) Q: Can you show me heath maps of important locations?
    * A: Yes it's pretty beautifull
3) Q: Can you plot a couple of single days?
    * A: Yes, but it could need more work
4) Q: How long am I at Kunlabora usually?
    * A: Somewhere between 8 and 9 hours

## 2019-02-05-recognize-missing-data.ipynb
1) Q: How many hours do we typically expect between data points?
    * A: 86 cases > 2h
    * A: outliers > 0.1h
2) Q: When do the bigger gaps happen?
    * A: > 15min => clearly during the night
    * A: > 5min => also kind of during the night

## 2019-02-07-find-dense-areas.ipynb
1) Q: Can we recognize some patterns from plotting all the data in a heath map?
    * A: Yes, we see many of the main Belgian roads and cities
2) Can we show the places with the highest density in a recognizable way?
    * A: Yes, by showing those data points, overlaying a map of the nearby Belgian roads.
    * A: Yes, places show up like: 
        * Ensure, Maisuradze, Eddie, Saman, Bankstraat, Vincent, Leuven marked (crossing of many paths?), Kunlabora, Alfred Delaunoislaan, Cegeka
    * A: we can also show them on a Belgian scale
    
## 2019-02-10-kmeans-clustering.ipynb
1) Q: Is it possible to use K-means to find hotspots?
    * A: Maybe, but K-means would also show paths with no nearby hotspots as being centroids. (not obvious from notebook)

## 2019-02-15-visualize-sequence-of-locations.ipynb
TODO: Notebook is not giving clear output of what it is doing