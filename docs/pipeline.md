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
3) Sample some time intervals
    * sample_intervals.ipynb
    * output: data/samples/sample_*.csv
    * 2018, 2019, 2020_01
        
## Endpoints (input -> graphs/tables/numbers)

* Q: In what countries have I been?
    * international.ipynb
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
        