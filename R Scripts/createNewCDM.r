# install.packages("devtools")
devtools::install_github("OHDSI/CommonDataModel")

library(CommonDataModel)

CommonDataModel::listSupportedDialects()
CommonDataModel::listSupportedVersions()

CommonDataModel::buildRelease(
    cdmVersions = "5.4",
    targetDialects = "postgresql",
    outputfolder = "pathToOutput"
)

devtools::install_github("OHDSI/DatabaseConnector")

library(DatabaseConnector)

downloadJdbcDrivers(dbms = "postgresql", pathToDriver = "~/")

cd <- DatabaseConnector::createConnectionDetails(
    dbms = "postgresql",
    server = "132.72.65.168/Hadassah",
    user = "postgres",
    password = "ayalonA3",
    pathToDriver = "~/"
)

CommonDataModel::executeDdl(
    connectionDetails = cd,
    cdmVersion = "5.4",
    cdmDatabaseSchema = "omop_demo",
    executeDdl = TRUE,
    executePrimaryKey = TRUE,
    executeForeignKey = FALSE
)