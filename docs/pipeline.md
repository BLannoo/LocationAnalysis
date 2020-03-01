# Rewritting the eda as a set of notebooks in a pipeline
## Pipes (input -> output)

1) Transform the data from a .json to a .csv
    * json_to_csv.ipynb
    * output: data/raw-csv/full.csv
    * load time .json: 10.8s
    * load time .csv: 1.94s
2) Enrich the gps data with: derived features
    * enrich.ipynb
    * output: data/enriched/enriched.csv
    * adds:
        * dates
        * year, month, day, hour
        * time_of_day
        * duration (half the distance between the 2 surrounding data points)
        * country, continent, iso_a3(Country code)
3) Sample some time intervals
    * sample_intervals.ipynb
    * output: data/samples/*.csv
    * 2018, 2019, 2020/01, 2018-Belgium
        
## Endpoints (input -> graphs/tables/numbers)
### work_life_balance.ipynb
1) Q: How long am I at Kunlabora usually?
    * A: Somewhere between 8 and 9 hours

## find-dense-areas.ipynb
1) Q: Can we find the most important places for me?
    * A: Yes, using a heatmap we can bin Belgium and the bins with the highest counts are indeed places I can recognize.
2) Q: Can we show the places with the highest density in a recognizable way?
    * A: Yes, by showing those data points, overlaying a map of the nearby Belgian roads.
    * A: Yes, places show up like: 
        * Ensure, Maisuradze, Eddie, Saman, Bankstraat, Vincent, Leuven marked (crossing of many paths?), Kunlabora, Alfred Delaunoislaan, Cegeka
    * A: we can also show them on a Belgian scale

### International.ipynb
* Q: In what countries have I been? 
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
        
### roads_data_overlay.ipynb
* Q: Where have I been inside Belgium?
    * A: 1 path towards Kortrijk + coast
    * A: Couple of paths towards the Ardenes
    * A: Many paths towards the Kempen
* Q: Where have I been in Leuven?
    * A: Everywhere inside the ring
    * A: Many places around the ring
* Q: Where was I on 2018/12/25? (can I show 1 day)
    * A: From Leuven to Kortrijk. (yes)

### random-stats.ipynb
1) Q: How much variance is there in my position per hour?
    * A: 0 and |---|e^0|e^30|---|
2) Q: How much variability is there in my movement?
    * A: 0 and |---|e^-5|e^10|---|
3) Q: How are the time intervals between measurements over the time of the day?
    * A: some patterns, but nothing obvious
4) Q: When are measurements taken during the day?
    * A: Less at night

## recognize-missing-data.ipynb
1) Q: How many hours do we typically expect between data points?
    * A: 82 cases > 2h
    * A: outliers > 0.1h == 6min
2) Q: When do the bigger gaps happen?
    * A: > 15min => clearly during the night
    * A: > 6min => also kind of during the night

### area_heathmaps.ipynb
1) Q: Can you show me heath maps of important locations?
    * A: Yes it's pretty beautifull
    * A: Inside Belgium it tells a similar story as roads_data_overlay.ipynb

### visualize_single_days.ipynb
1) Q: Can you plot a couple of single days?
    * A: Yes, but it could need more work 
        * eg: integration with roads_data_overlay.ipynb

### experiment_rendering_speed.ipynb
1) Q: Would it be faster to exclude roads which wont be rendered in the final graph?
    * A: No, it is even slower (mostlikely due to the exclusion logic)
