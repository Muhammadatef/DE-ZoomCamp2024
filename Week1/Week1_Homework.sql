1- docker run --help
 --rm    Automatically remove the container when it exits

2-  docker run -it python:3.9 bash 

root@800960adb454:/# pip list
Package    Version
---------- -------
pip        23.0.1
setuptools 58.1.0
wheel      0.42.0 



3- SELECT COUNT(*) AS total_trips
FROM green_taxi_data
WHERE DATE(lpep_pickup_datetime) = '2019-09-18'
  AND DATE(lpep_dropoff_datetime) = '2019-09-18';
 total_trips 
-------------
       15612
(1 row)
================================
4- 
select Max(trip_distance), lpep_pickup_datetime::date from green_taxi_data  group by lpep_pickup_datetime::date order by Max(trip_distance) DESC ; 
  max   | lpep_pickup_datetime 
--------+----------------------
 341.64 | 2019-09-26
 135.53 | 2019-09-21
  89.64 | 2019-09-28
 
=======================================
 
5-
SELECT
  tz."Borough" AS pickup_borough,
  SUM(gtd."total_amount") AS total_amount_sum
FROM green_taxi_data gtd
JOIN taxi_zones tz ON gtd."PULocationID" = tz."LocationID"
WHERE DATE(gtd."lpep_pickup_datetime") = '2019-09-18'
  AND gtd."PULocationID" IS NOT NULL
GROUP BY tz."Borough"
HAVING SUM(gtd."total_amount") > 50000
ORDER BY total_amount_sum DESC
LIMIT 3;
 pickup_borough | total_amount_sum  
----------------+-------------------
 Brooklyn       | 96333.23999999902
 Manhattan      |  92271.2999999985
 Queens         | 78671.70999999889
(3 rows)
==========================

6- 
SELECT
  tz_dropoff."Zone" AS dropoff_zone,
  MAX(gtd."tip_amount") AS largest_tip
FROM green_taxi_data gtd
JOIN taxi_zones tz_pickup ON gtd."PULocationID" = tz_pickup."LocationID"
JOIN taxi_zones tz_dropoff ON gtd."DOLocationID" = tz_dropoff."LocationID"
WHERE DATE(gtd."lpep_pickup_datetime") >= '2019-09-01'
  AND DATE(gtd."lpep_pickup_datetime") <= '2019-09-30'
  AND tz_pickup."Zone" = 'Astoria'
GROUP BY tz_dropoff."Zone"
ORDER BY largest_tip DESC
LIMIT 1;
 dropoff_zone | largest_tip 
--------------+-------------
 JFK Airport  |       62.31
 
 ==============================
 7- Terraform

 
