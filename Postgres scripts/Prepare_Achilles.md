@author: nadavrap

# Achilles installation and execution
**Achilles** is the way to generate the results which are summary statistics for the OMOP CDM.
Instructions can be found [here](https://ohdsi.github.io/Achilles/articles/GettingStarted.html) and [here](https://ohdsi.github.io/Achilles/articles/RunningAchilles.html).

## Prepare DB
Make sure that you have the next two schema:
- scratch
- results

If not, create it using the next SQL queries:
```
create schema scratch;
 create schema results;
```

## Install Achilles
```
if (!require("remotes")) install.packages("remotes")

# To install the master branch
remotes::install_github("OHDSI/Achilles")
```

## Run Achilles
```
library(Achilles)
downloadJdbcDrivers(dbms='postgresql', pathToDriver='~/')
connectionDetails <- createConnectionDetails(dbms='postgresql', server='132.72.65.168/Hadassah', user='postgres', password='ayalonA3', port='5432', pathToDriver='~/')
achilles(connectionDetails, 
    cdmDatabaseSchema = "mimic", 
    resultsDatabaseSchema = 'results',
  scratchDatabaseSchema = 'scratch',
  numThreads = 10,
  outputFolder = "output")
  ```
