import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    """
    Template for loading data from API
    """
    url10 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz'
    url11 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz'
    url12 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'



    data_dtypes = {
    'VendorID': pd.Int64Dtype(),
    'passenger_count': pd.Int64Dtype(),
    'trip_distance': 'float',
    'RatecodeID': pd.Int64Dtype(),
    'store_and_fwd_flag': str,
    'PULocationID': pd.Int64Dtype(),
    'DOLocationID': pd.Int64Dtype(),
    'payment_type': pd.Int64Dtype(),
    'fare_amount': 'float',
    'extra': 'float',
    'mta_tax': 'float',
    'tip_amount': 'float',
    'tolls_amount': 'float',
    'improvement_surcharge': 'float',
    'total_amount': 'float',
    'congestion_surcharge':'float'}

    parse_dates= ['lpep_pickup_datetime',
    'lpep_dropoff_datetime']

    df10 = pd.read_csv(url10, sep=",", compression="gzip", dtype=data_dtypes, parse_dates=parse_dates)
    df11 = pd.read_csv(url11, sep=",", compression="gzip", dtype=data_dtypes, parse_dates=parse_dates)
    df12 = pd.read_csv(url12, sep=",", compression="gzip", dtype=data_dtypes, parse_dates=parse_dates)

# Concatenate the DataFrames vertically
    data = pd.concat([df10, df11, df12], ignore_index=True)

# Return the concatenated DataFrame
    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
