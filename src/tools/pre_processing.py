import json
import pandas as pd

def json_to_csv(input_file_name: str) -> pd.DataFrame:
    with open(input_file_name) as file:
        data = json.load(file)['locations']
        return pd.DataFrame(
            {
                'timestampMs': [
                    data_point['timestampMs']
                    for data_point in data
                ],
                'latitudeE7': [
                    data_point['latitudeE7']
                    for data_point in data
                ],
                'longitudeE7': [
                    data_point['longitudeE7']
                    for data_point in data
                ],
                'accuracy': [
                    data_point['accuracy']
                    for data_point in data
                ],
                'activity': [
                    # get returns None for absent fields
                    data_point.get('activity')
                    for data_point in data
                ],
            }
        )