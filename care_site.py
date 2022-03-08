# Care site table
#
# Parameters:
#
# Tables:
# source table = transition Between departments
# OMP table - care_site


import pandas as pd

table_name = "92.csv"
table = pd.read_csv(table_name)
department = table["Department"].drop_duplicates()
data=[]
care_site_id = 1
place_of_service_concept_id = 9201
for i, department_name in department.items():
    data.append([care_site_id, department_name, place_of_service_concept_id])
    care_site_id += 1

df_result = pd.DataFrame(data, columns=["care_site_id" , "care_site_name","place_of_service_concept_id"])

df_result.to_csv('care_site.csv', encoding='utf-8', index=False)


