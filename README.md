# Hadassah_OMOP- Building the server and application

## Permissions
### These permissions were granted by the Computer Department at Ben-Gurion University and the permissions are:
  •	To the remote server
  
  •	 For a compose tool
  
  •	The tool through which you can connect to the server PostgreSQL Via the remote server Using the command psql In Linux.

## Installations
### Steps to set up a server Postgres And uploading the app OHDSI:
•	clone to Git: OHDSI: https://github.com/OHDSI/Broadsea-WebTools 

•	Running the docker Multiple containers Using the tool compose.

•	Editing the configuration files:
    •	 Of the container that runs the server so that the login information matches the database Hadassah Which is on the PostgreSQL server.
  
    •	Of the container running the webAPI of OHDSI And entering the link address to ATLAS Via the remote server: http://132.72.65.168:8080/atlas/.

•	 Download the tables VOCABULARY CONCEPTS etc ,'of OHDSI Via the link: https://athena.ohdsi.org/search-terms/start

•	Download the scripts that define the tables in the appropriate version and move them to a folder we created on the remote server.

•	Performing the steps given in Git: https://github.com/MIT-LCP/mimic-omop/tree/master/omop/build-omop/postgresql using Linux commands on the remote server:
  
    •	Connecting to a database located on the PostgreSQL server 
  
    •	Running a script SQL Which builds the target tables on the server.
      [link to script] 
      (https://github.com/nadavlab/Hadassah_OMOP/blob/main/Sql%20Scripts/OMOPCDM_postgresql_5.46_ddl.sql)
    •	Running a script SQL Which defines the primary keys in each table.
      [link to script] 
      (https://github.com/nadavlab/Hadassah_OMOP/blob/main/Sql%20Scripts/OMOPCDM_postgresql_5.46_primary_keys.sql)

    •	Upload vocabulary tables and concepts  through script execution SQL
      [link to script] (https://github.com/nadavlab/Hadassah_OMOP/blob/main/Sql%20Scripts/omop_vocab_load.sql)

    •	Upload each table individually to the database using a script built in Python.
      [link to script] (https://github.com/nadavlab/Hadassah_OMOP/blob/main/Sql%20Scripts/upload_data.py)

  •	Build constraints using a SQL script on each table.
    [link to script] (https://github.com/nadavlab/Hadassah_OMOP/blob/main/Sql%20Scripts/omop_constraints_load.sql)

## connections
### Connections during project execution: 
•	Connection to the university's remote server:
    • connect to BGU VPN with personal code.
    • connect to remote server threw VM with personal password.
    • connect to data base in postgreSQL server threw the remote server.

• Perform the steps for connecting the desired consent from the PostgreSQL server To Atlas According to the Git - https://github.com/OHDSI/WebAPI/wiki/CDMConfiguration:
    •	Creating 2 new schemas on the Postgres server, each schema will be used for a different rule. 
  
    •	Entering parameters, which provide login information for the desired schema on the server, into URL Given in the manual and running the script that build tables       to results schema, given by the web page, in PostgreSQL server.
      [link to script]
      (https://github.com/nadavlab/Hadassah_OMOP/blob/main/Sql%20Scripts/cdm_config_webAPI.sql)

    •	 Changing parameters in the script given to us by Git and running it to build the Source tables and connect us to the desired schema to the atlas.
  
    •	 Running the software Achilles in the language R And inserting the results of the run into a scheme we initially created. 
         The Achilles is used to analyze the data of the tables visually.
