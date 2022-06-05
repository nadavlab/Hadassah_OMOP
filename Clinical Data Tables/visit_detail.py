# Visit detail

import pandas as pd
from datetime import datetime , date

source_table = pd.read_csv("92.csv")

#### visit occurrence table ####
visit_occurrence = pd.read_csv("visit_occurrence.csv")
df_visit_occurrence = pd.DataFrame(visit_occurrence ,columns=['visit_occurrence_id'])

### care site tabele ####
care_site_table = pd.read_csv("care_site.csv")
df_care = pd.DataFrame(care_site_table , columns=["care_site_id" , "care_site_name" , "place_of_service_concept_id"])

### person ####
df_person = pd.read_csv("person.csv")

def is_exsit_person_id(id_baznat):
    match_person = df_person.loc[df_person['person_id'] == id_baznat]
    if match_person.shape[0] > 0 :
        return True
    else:
        return False

data=[]
index = 1

### Concepts ####
INPATIENT_VISIT_CONCEPT_ID = 4140387
EHR_CONCEPT_ID = 32817

for index_row, row in source_table.iterrows():
    if is_exsit_person_id:
        person_id = int(row["ID_BAZNAT"])
    else:
        continue

    ### check if id visit_occurrence exists ###
    match_visit_occurrence = visit_occurrence.loc[visit_occurrence['visit_occurrence_id'] == row['Event_baznat']]
    if match_visit_occurrence.shape[0] == 0:
        continue
    else:
        visit_occurrence_id = int(row['Event_baznat'])

    visit_detail_id = index
    visit_detail_concept_id = INPATIENT_VISIT_CONCEPT_ID
    visit_detail_type_concept_id = EHR_CONCEPT_ID
    visit_detail_source_concept_id = EHR_CONCEPT_ID

    date_start = datetime.strptime(row["Department_Entry_Date"] , '%d/%m/%Y %H:%M')
    visit_detail_start_date = date_start.date()
    if date_start :
        visit_detail_start_datetime = date_start
    if row[5] !='-1':
        date_end = datetime.strptime(row["Department_Exit_Date"] , '%d/%m/%Y %H:%M')
        visit_detail_end_date = date_end.date()
        if date_end:
            visit_detail_end_datetime = date_end
    else:
        match_visit_occurrence = visit_occurrence.loc[visit_occurrence['preceding_visit_occurrence_id'] == visit_occurrence_id]
        if match_visit_occurrence.values.size != 0:
            index_date = 0
            while match_visit_occurrence["HOSP_ENTRY_DATE"].size > index_date and type(match_visit_occurrence["HOSP_EXIT_DATE"].values[index_date]) != float :
                date_start_89 = datetime.strptime(match_visit_occurrence["HOSP_ENTRY_DATE"].values[index_date] , '%d/%m/%Y %H:%M:%S')
                date_end_89 = datetime.strptime(match_visit_occurrence["HOSP_EXIT_DATE"].values[index_date] , '%d/%m/%Y %H:%M:%S')
                if date_start_89 <= date_start<= date_end_89:
                    visit_detail_end_date = date_end_89.date()
                    visit_detail_end_datetime = date_end_89
                index_date += 1
    if not visit_detail_start_date or not visit_detail_end_date:
        continue

    ### care_site_id ###
    care_site_id = ''
    match_care_site = df_care.loc[df_care["care_site_name"] == row["Department"]]
    if match_care_site.shape[0] > 0:
        care_site_id = match_care_site.values[0][0]

    provider_id = ''
    visit_detail_source_value = ''
    admitted_from_concept_id = 0
    admitted_from_source_value = ''
    discharged_to_source_value = ''
    discharged_to_concept_id = ''
    preceding_visit_detail_id = ''
    parent_visit_detail_id = ''

    data.append([visit_detail_id, person_id, visit_detail_concept_id,  visit_detail_start_date ,visit_detail_start_datetime,visit_detail_end_date,visit_detail_end_datetime,
                 visit_detail_type_concept_id,provider_id,care_site_id,visit_detail_source_value,visit_detail_source_concept_id,admitted_from_concept_id,admitted_from_source_value,
                 discharged_to_source_value, discharged_to_concept_id,preceding_visit_detail_id,parent_visit_detail_id,visit_occurrence_id   ])
    index += 1

df_result = pd.DataFrame(data, columns=['visit_detail_id', 'person_id', 'visit_detail_concept_id',  'visit_detail_start_date' ,'visit_detail_start_datetime','visit_detail_end_date','visit_detail_end_datetime',
                 'visit_detail_type_concept_id','provider_id','care_site_id','visit_detail_source_value','visit_detail_source_concept_id','admitted_from_concept_id','admitted_from_source_value',
                 'discharged_to_source_value', 'discharged_to_concept_id','preceding_visit_detail_id','parent_visit_detail_id','visit_occurrence_id'])

df_result.to_csv('visit_detail.csv', encoding='utf-8', index=False)