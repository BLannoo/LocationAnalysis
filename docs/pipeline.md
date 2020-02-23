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
