# Fact Relationships
import pandas as pd
import numpy

### person ####
df_person = pd.read_csv("person.csv")

def is_exsit_person_id(id_baznat):
    match_person = df_person.loc[df_person['person_id'] == id_baznat]
    if match_person.shape[0] > 0 :
        return True
    else:
        return False

person_concept_id = 56 #Person
infant_of_subject_concept_id = 42539764 #Infant of subject
mother_of_subject_concept_id = 40478925
table_name = "89.csv"
source_table = pd.read_csv(table_name)
data=[]

for index_row, row in source_table.iterrows():
    domain_concept_id_1 = person_concept_id
    if(float(row['MOTHER_ID_BAZNAT']) and not numpy.isnan(row['MOTHER_ID_BAZNAT'])):
        fact_id_1 = int(row['MOTHER_ID_BAZNAT'])

    domain_concept_id_2 = person_concept_id
    if float(row['ID_BAZNAT']) and not numpy.isnan(row['ID_BAZNAT']) :
        fact_id_2 = int(row['ID_BAZNAT'])

    if is_exsit_person_id(fact_id_2) and is_exsit_person_id(fact_id_1):
        data.append([domain_concept_id_1, fact_id_1, domain_concept_id_2, fact_id_2, infant_of_subject_concept_id])
        data.append([domain_concept_id_2, fact_id_2,domain_concept_id_1, fact_id_1, mother_of_subject_concept_id])

df_result = pd.DataFrame(data, columns=["domain_concept_id_1" , "fact_id_1","domain_concept_id_2","fact_id_2", "relationship_concept_id"])

df_result.to_csv('fact_relationship.csv', encoding='utf-8', index=False)
