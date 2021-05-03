Capstone Project

This final project is a flexible project where students are allowed to use their own criteria in terms of database schemma build and tools. 

Scope:

A fact table on immigration is build toghether with 3 dimension tables demographics, temperature and airportCodes.
The purpose of these data sources, is to provide government analysts information for reporting and modelling purposes.
The hope is that relevant agencies can heep track of inmmigration patterns and also be able to build prediction models that can help assess different potential policies. For example, an analyst could investigate if any patterns exists between city temperature and demographics composition with the different nationality volums migrating into that city. This can easily be achived by joining the immigration table with the demographics table by city. Temperature can then can also be added by joning via city and date. 

The provided data files were used:

I94 Immigration Data
This data comes from the US National Tourism and Trade Office. The workspace already includes a data dictionary. Due to running time contraints, only the sample CSV file was used.
More details can be found in the following link: https://travel.trade.gov/research/reports/i94/historical/2016.html


World Temperature Data
Kaggle dataset . More information in the following link: https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data 


U.S. City Demographic Data. 
More information in the following link: https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/


Airport Code Table

Datahub dataset. More information in the following link: https://datahub.io/core/airport-codes#data



Data Preparation and Steps.

For all datasets, remove fields that generally contain >50% missing values.
The selected fields for each table are listed in the conceptual data model below.
Finally insert the modelled records into their respective tables.

Conceptual Data Model 
Table Name		Fields		                                                                                                                                                        type
AirportCodes		ident, name, type, local_code,coordinated,elevation_ft,iso_country,iso_region, municipality, gps_code		                                                        Dimension
demographics		city, state, median_age, male_population, female_population, total_population, num_veterans, foreign_born, average_household_size, state_code, rece, count		Dimension
immigration		cicid, year, month, cit, res, arrdate,mode,addr,depdate, bir,count, dtadfile, entdepa, entdepd,matflag, biryear,dtaddto,gender, airline, admnum, fltno, visatype	Fact
temperature		timestamp, average_temperature,average_temperature_uncertainty, city, country, latitude, longitude	                                                            	Dimension



Use Description:

There is a key fact table that contains key USA immigration data. This data can be complemented with the dimension tables temperature, demographics, and Airport codes.
The data was uploaded into Redshift tables for analysts consumption.
It is expected that analtysts will build both reporting and modelling solutions from it.



Tools and technologies:

Python language with necessary packages (Pandas, psycopg2) Pyspark if necessary. The Jupyter notebook interface was also used. Tables where save in an Amazon Redshift database.
To run the solution succesfully, first run the run_create_tables.ipynb file. This will create the fact and dimention tables for the project.
Lastly, run the insert statements found towards the end of the capstone Project template file.
Note: The code can be easily adjusted to include pyspark in the event of factor usage increase (code also provided).


The provided I94 dimmigration date is aggregated on a monthly basis. For this reason it is recommended that the data is update also on a monthly basis.

Files included in submission:

-Capstone Project Template.ipynb: This file contains all code for data exploration, cleaning, and record insert.
-create_tables.py: This file contains the python code that generated the fact and dimension tables (Redshift) calling functions from sql_queries.
-sql_queries.py: Contains the python code to create, delete tables and insert records. 
_run_create_tables.ipynb: Contains python code that runs the create tables main function.

FAQ: Scenarios:

    -The data was increased by 100x.
        Make use of the provided pyspark code for handling the immigration fact information. Analysts can also make use of Appache Cassandra for quering the data.
    -The data populates a dashboard that must be updated on a daily basis by 7am every day.
        Use Airflow and create a DAG that performs the logic of the described pipeline in the required timeframe. 
    -The database needed to be accessed by 100+ people.
        Amazon redshift provides the necessary level of elasticity to increase resources if necessary for reads. Analytists can also make use of Appache cassandra (NoSQL)          to query the data efficiently.
        In terms of updating/write the fact table, pyspark can be used. Adding partitions will help improve the performace of write ups.