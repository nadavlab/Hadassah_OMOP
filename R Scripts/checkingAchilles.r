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


achilles(connectionDetails,
  cdmDatabaseSchema = "omop_demo",
  resultsDatabaseSchema = "results",
  # scratchDatabaseSchema = "scratch",
  # numThreads = 1,
  outputFolder = "./Output"
)



createIndices(
  connectionDetails = connectionDetails,
  resultsDatabaseSchema = "results",
  outputFolder = "./Output"
)



# dropAllScratchTables(
#   connectionDetails = connectionDetails,
#   scratchDatabaseSchema = "scratch", numThreads = 5, outputFolder = "output/"
# )