# Module 5: Batch Processing

## Overview
![My Image](Batch_Processing_Spark_Week5/DEZCW5_Diagram.jpg)

This module provides an overview of batch processing with Apache Spark. It covers the following topics:

- **Batch Processing**: Overview of batch processing.
- **Apache Spark**: Introduction to Apache Spark.
- **Spark Dataframes**: Working with Spark Dataframes.
- **Spark SQL**: Executing SQL queries in Spark.
- **Internals**: Understanding Spark internals for grouping and joining.

## Accessing Spark and Jupyter Notebook

To access Spark and Jupyter Notebook for Spark development, follow these steps:

1. Install Spark locally or set up a Spark cluster on a remote server.

2. Start the Spark cluster.

3. Access the Spark Master UI by navigating to http://localhost:8080 in your web browser. This provides information about the Spark cluster and its resources.

4. Access Jupyter Notebook for Spark development by navigating to http://localhost:8888 in your web browser. Here, you can write and execute Spark code using PySpark or other Spark APIs.

5. Optionally, you may need to open additional ports for specific services:
   - Port 8080: Spark Master UI
   - Port 8888: Jupyter Notebook

## Reading Taxi Zone Lookup and FHV Trip Data into Spark

To read the taxi zone lookup and FHV trip data into Spark, you can use the following steps:

1. Load the data files into your working directory or specify the file paths if they're stored elsewhere.

2. Use Spark's DataFrame API or Spark SQL to read the data files. For example:

    ```python
    from pyspark.sql import SparkSession

    spark = SparkSession.builder \
        .appName("Reading Taxi Data into Spark") \
        .getOrCreate()

    # Read the taxi zone lookup data
    taxi_zone_lookup_df = spark.read.option("header", "true").csv("taxi_zone_lookup.csv")

    # Read the FHV trip data
    fhv_trip_data_df = spark.read.option("header", "true").csv("fhv_tripdata_2019-10.csv")
    ```

3. Perform any necessary data cleaning, transformations, or analysis using Spark DataFrames or Spark SQL.

---

This README provides a guide on accessing Spark and Jupyter Notebook for Spark development and reading taxi zone lookup and FHV trip data into Spark. Adjust the instructions as needed based on your specific requirements and configurations.
