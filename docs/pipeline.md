# Rewritting the eda as a set of pipelines

1) Transform the data from a .json to a .csv
    * json_to_csv.ipynb
    * output: data/raw-csv/full.csv
    * load time .json: 10.8s
    * load time .csv: 1.94s
2) Sample some time intervals
    * sample_intervals.ipynb
    * output: data/samples/sample_*.csv
    * 2018, 2019, 2020_01
3) Enrich all the csv generated previously with some derived data
    * enrich.ipynb
    * output: data/enriched/*.csv
    * adds:
        * dates
        * year, month, day, hour
        * time_of_day
        * duration (half the distance between the 2 surrounding data points)