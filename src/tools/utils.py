from datetime import datetime

def as_timestampMs(
    date_string: str,
    date_format: str = '%Y-%m-%dT%H:%M:%S'
):
    date = datetime.strptime(date_string, date_format)
    return date.timestamp()*1000