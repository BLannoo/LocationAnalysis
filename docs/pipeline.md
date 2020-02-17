# Rewritting the eda as a set of pipelines

1) Transform the data from a .json to a .csv
    * json_to_csv.ipynb
    * processed/full.csv
    * load time .json: 10.8s
    * load time .csv: 1.94s
2) Sample some time intervals
    * sample_intervals.ipynb
    * processed/sample_*.csv
    * 2018, 2019, 2020_01