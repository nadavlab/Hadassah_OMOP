if (!require("devtools")) install.packages("devtools")
devtools::install_github("OHDSI/DataQualityDashboard")

library(DatabaseConnector)
library(DataQualityDashboard)
library(ParallelLogger)

downloadJdbcDrivers(dbms='postgresql', pathToDriver='~/')

connectionDetails <- createConnectionDetails(dbms='postgresql', server='132.72.65.168/Hadassah', user='postgres', password='ayalonA3', port='5432', pathToDriver='~/')



cdmDatabaseSchema <- "mimic" # the fully qualified database schema name of the CDM
resultsDatabaseSchema <- "results" # the fully qualified database schema name of the results schema (that you can write to)
cdmSourceName <- "CDM mimic v1" # a human readable name for your CDM source

numThreads <- 1 # on Redshift, 3 seems to work well

# specify if you want to execute the queries or inspect them ------------------------------------------
sqlOnly <- FALSE # set to TRUE if you just want to get the SQL scripts and not actually run the queries

# where should the logs go? -------------------------------------------------------------------------
outputFolder <- "output"
outputFile <- "results.json"


# logging type -------------------------------------------------------------------------------------
verboseMode <- TRUE # set to TRUE if you want to see activity written to the console

# write results to table? -----------------------------------------------------------------------
writeToTable <- TRUE # set to FALSE if you want to skip writing to results table

checkLevels <- c("TABLE", "FIELD", "CONCEPT")

# which DQ checks to run? ------------------------------------

checkNames <- c() #Names can be found in inst/csv/OMOP_CDM_v5.3.1_Check_Desciptions.csv

tablesToExclude <- c() 


# run the job --------------------------------------------------------------------------------------
DataQualityDashboard::executeDqChecks(connectionDetails = connectionDetails, 
                                    cdmDatabaseSchema = cdmDatabaseSchema, 
                                    resultsDatabaseSchema = resultsDatabaseSchema,
                                    cdmSourceName = cdmSourceName, 
                                    numThreads = numThreads,
                                    sqlOnly = sqlOnly, 
                                    outputFolder = outputFolder, 
                                    outputFile = outputFile,
                                    verboseMode = verboseMode,
                                    writeToTable = writeToTable,
                                    checkLevels = checkLevels,
                                    tablesToExclude = tablesToExclude,
                                    checkNames = checkNames)

# inspect logs ----------------------------------------------------------------------------
ParallelLogger::launchLogViewer(logFileName = file.path(outputFolder, cdmSourceName, 
                                                      sprintf("log_DqDashboard_%s.txt", cdmSourceName)))

# (OPTIONAL) if you want to write the JSON file to the results table separately -----------------------------
jsonFilePath <- ""
DataQualityDashboard::writeJsonResultsToTable(connectionDetails = connectionDetails, 
                                            resultsDatabaseSchema = resultsDatabaseSchema, 
                                            jsonFilePath = jsonFilePath)

DataQualityDashboard::viewDqDashboard(
  jsonPath = file.path(getwd(), outputFolder, cdmSourceName, outputFile, cdmSourceName))
