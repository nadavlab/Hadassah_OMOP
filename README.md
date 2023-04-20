# Hadassah_OMOP- Building the server and application

## Required Permissions
### These permissions were granted by the IT Department at Ben-Gurion University and the permissions are:

* For the remote server
* For a compose tool
* PostgreSQL

## Installations
### Steps to set up a Postgres server snd uploading the load the OHDSI apps:
1. Clone the next repository: OHDSI: https://github.com/OHDSI/Broadsea-WebTools 
2. Run the docker Multiple containers Using the tool compose.
3. Edit the configuration files as follow:

* Set login information to matches the Hadassah database.
* The webAPI and the url of ATLAS to: http://<URL>:8080/atlas/. Where <URL> is should be replace with the actual address (something like 123.45.67.890)
* Download the concepts related tables VOCABULARY, CONCEPTS etc. from OHDSI Athena: https://athena.ohdsi.org/search-terms/start
* Download the scripts that define the schema and tables in the appropriate version and move them to a folder we created on the remote server: [Sql Scripts](<Sql Scripts>). This SQL queries can be generated using the next command
```
CommonDataModel::buildRelease(cdmVersions = "5.4",
                              targetDialects = "postgresql",
                              outputfolder = "/pathToOutput")
```
See https://github.com/OHDSI/CommonDataModel#1-use-the-buildrelease-function and [R Scripts/createNewCDM.r](<R Scripts/createNewCDM.r>).

* The execute these queries.

* Execute it from R on the remote server:

    *	Running a script SQL Which builds the target tables on the server.
      [link to script] 
      (https://github.com/nadavlab/Hadassah_OMOP/blob/main/Sql%20Scripts/OMOPCDM_postgresql_5.46_ddl.sql)
    *	Running a script SQL Which defines the primary keys in each table.
      [link to script] 
      (https://github.com/nadavlab/Hadassah_OMOP/blob/main/Sql%20Scripts/OMOPCDM_postgresql_5.46_primary_keys.sql)

    *	Upload vocabulary tables and concepts  through script execution SQL
      [link to script] (https://github.com/nadavlab/Hadassah_OMOP/blob/main/Sql%20Scripts/omop_vocab_load.sql)

    *	Upload each table individually to the database using a script built in Python.
      [link to script] (https://github.com/nadavlab/Hadassah_OMOP/blob/main/Sql%20Scripts/upload_data.py)

    *	Build constraints using a SQL script on each table.
      [link to script] (https://github.com/nadavlab/Hadassah_OMOP/blob/main/Sql%20Scripts/omop_constraints_load.sql)

## Connections and relevant URLs

•	Connection guide to ATLAS and postgreSQL server:
    
    * Make sure you are connected to BGU VPN with your personal code.    
    * Connect to postgreSQL server with the URL:[link to URL] (http://<URL>:5050/browser/).
    * connect to ATLAS application with the URL:[link to URL] http://<URL>:8080/atlas/).

* Perform the steps for connecting from the ATLAS to PostgreSQL server according to the the next guide - https://github.com/OHDSI/webapi-wiki/blob/master/CDM-Configuration.md .
*	Create 2 new schemas in the DB, each schema will be used for a different purpose. 
* Execute the setup script [cdm_setup.sql](<Sql Scripts/cdm_setup.sql>)

## Transform process
There are several scripts that need to be executed by domain:
* [Care site](<Health System Data Tables/care_site.py>)
* [Location](<Health System Data Tables/location.py>)
* And the others script in [Clinical Data Tables](<Clinical Data Tables>)

## Load the data into the DB
* Load the concepts related tables using [cdm_vocab_load.sql](<Sql Scripts/cdm_vocab_load.sql>)
* Upload the data by executing [upload_data.py ](<Sql Scripts/upload_data.py>) which is a wrapper for upload transformed CSV files.


## Excute the tests
Run the Achilles using R and load the results to the DB. The Achilles is used to analyze the data of the tables visually.

* <R Scripts/checkingAchilles.r>
* <R Scripts/checkingDQD.r>
