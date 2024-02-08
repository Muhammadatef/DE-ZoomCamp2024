#Extraction Block

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




#Transformers Block
import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    #print(f"Preproccessing: rows with zero passenger: {data['passenger_count'].isin([0]).sum()}")

    # Specify your transformation logic here
    filtered_data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    num_rows = filtered_data.shape[0]

    print(filtered_data)
    print(num_rows)


    unique_vendor_IDs = data['VendorID'].unique()
    print(unique_vendor_IDs)

    data_cols = data.columns
    print(data_cols)


##OUTPUT  : 
# [139370 rows x 20 columns]

# 139370

# <IntegerArray>

# [2, 1, <NA>]

# Length: 3, dtype: Int64

# Index(['VendorID', 'lpep_pickup_datetime', 'lpep_dropoff_datetime',

#        'store_and_fwd_flag', 'RatecodeID', 'PULocationID', 'DOLocationID',

#        'passenger_count', 'trip_distance', 'fare_amount', 'extra', 'mta_tax',

#        'tip_amount', 'tolls_amount', 'ehail_fee', 'improvement_surcharge',

#        'total_amount', 'payment_type', 'trip_type', 'congestion_surcharge'],

#       dtype='object')



#DATA Exporter Block 
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_postgres(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a PostgreSQL database.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#postgresql
    """
    schema_name = 'ny_taxi'  # Specify the name of the schema to export data to
    table_name = 'green_taxi_data'  # Specify the name of the table to export data to
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'dev'

    with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            schema_name,
            table_name,
            index=False,  # Specifies whether to include index in exported table
            if_exists='replace',  # Specify resolution policy if table name already exists
        )
