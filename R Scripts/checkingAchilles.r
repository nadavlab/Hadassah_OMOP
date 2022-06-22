if (!require("remotes")) install.packages("remotes")

# To install the master branch
install_github("OHDSI/Achilles")

library(Achilles)
library(DatabaseConnector)

downloadJdbcDrivers(dbms = "postgresql", pathToDriver = "~/")
connectionDetails <- createConnectionDetails(
  dbms = "postgresql",
  server = "132.72.65.168/Hadassah", 
  user = "postgres", 
  password = "ayalonA3", 
  port = "5432", 
  pathToDriver = "~/"
)

cdmDbSchema <- "omop_demo"
cdmVersion <- "5.4"

achilles(connectionDetails,
  cdmDatabaseSchema = cdmDbSchema,
  resultsDatabaseSchema = "results",
  outputFolder = "./Output",
  cdmVersion = cdmVersion
)


# exportToJson(connectionDetails,
#              cdmDatabaseSchema = cdmDbSchema,
#              resultsDatabaseSchema = "results",
#              outputPath = "achillesOut")



createIndices(
  connectionDetails = connectionDetails,
  resultsDatabaseSchema = "results",
  outputFolder = "./Output"
)

