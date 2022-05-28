# Care site table
#
# Parameters:
#inpatient_visit_concept_id - 4140387
#initial_index - 1
# Tables:
# source table = transition Between departments
# OMP table - care_site


import pandas as pd

table_name = "92.csv"
INPATIENT_VISIT_CONCEPT_ID = 4140387
initial_index = 1
table = pd.read_csv(table_name)
department = table["Department"].drop_duplicates()
data=[]
care_site_id = initial_index
place_of_service_concept_id = INPATIENT_VISIT_CONCEPT_ID
location_id = ''
care_site_source_value = ''
place_of_service_source_value = ''
for i, department_name in department.items():
    data.append([care_site_id, department_name, place_of_service_concept_id,location_id,care_site_source_value, place_of_service_source_value ])
    care_site_id += 1

df_result = pd.DataFrame(data, columns=["care_site_id" , "care_site_name","place_of_service_concept_id","location_id", "care_site_source_value", "place_of_service_source_value"])

df_result.to_csv('care_site.csv', encoding='utf-8', index=False)


