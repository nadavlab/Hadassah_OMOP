# Visit detail
#
# Parameters:
# place of service - Inpatient Visit 9201
# visit type - EHR
# Tables:
# source table = transition Between departments
# OMP table - visit_detail
import math

import pandas as pd
from datetime import datetime , date
source_table = pd.read_csv("92.csv")
visit_occurrence = pd.read_csv("89.csv")
df_visit_occurrence = pd.DataFrame(visit_occurrence ,columns=['Event_baznat' , 'HOSP_ENTRY_DATE' , 'HOSP_EXIT_DATE'])
data=[]
index=1
EHR_concept_id = 32817
InpatientVisit_concept_id = 9201
care_site_table = pd.read_csv("care_site.csv")

for index_row, row in source_table.iterrows():
    visit_detail_id=index
    visit_occurrence_id = row["Event_baznat"]
    person_id=row["ID_BAZNAT"]

    visit_detail_concept_id=InpatientVisit_concept_id
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
        match_visit_occurrence = df_visit_occurrence.loc[df_visit_occurrence['Event_baznat']==visit_occurrence_id]
        if match_visit_occurrence.values.size != 0:
            index = 0
            while match_visit_occurrence["HOSP_ENTRY_DATE"].size > index and type(match_visit_occurrence["HOSP_EXIT_DATE"].values[index]) != float :
                date_start_89 = datetime.strptime(match_visit_occurrence["HOSP_ENTRY_DATE"].values[index] , '%d/%m/%Y %H:%M:%S')
                date_end_89 = datetime.strptime(match_visit_occurrence["HOSP_EXIT_DATE"].values[index] , '%d/%m/%Y %H:%M:%S')
                if date_start_89<=date_start<=date_end_89:
                    visit_detail_end_date = date_end_89.date()
                    visit_detail_end_datetime = date_end_89
                index+=1
    #EHR
    visit_detail_type_concept_id = EHR_concept_id
    provider_id = ''
    #care_site_id
    care_site_id = ''
    df_care = pd.DataFrame(care_site_table ,columns=["care_site_id" , "care_site_name" , "place_of_service_concept_id"])
    match_care_site = df_care.loc[df_care["care_site_name"] == row["Department"]]
    care_site_id = match_care_site.values[0][0]

    visit_detail_source_value=''
    #EHR
    visit_detail_source_concept_id = EHR_concept_id
    admitted_from_concept_id = 0
    admitted_from_source_value = ''
    discharged_to_source_value = ''
    discharged_to_concept_id=''
    preceding_visit_detail_id=''
    parent_visit_detail_id=''

    if(visit_detail_start_date and visit_detail_end_date):
        data.append([visit_detail_id, person_id, visit_detail_concept_id,  visit_detail_start_date ,visit_detail_start_datetime,visit_detail_end_date,visit_detail_end_datetime,
                     visit_detail_type_concept_id,provider_id,care_site_id,visit_detail_source_value,visit_detail_source_concept_id,admitted_from_concept_id,admitted_from_source_value,
                     discharged_to_source_value, discharged_to_concept_id,preceding_visit_detail_id,parent_visit_detail_id,visit_occurrence_id   ])
        index+=1

df_result = pd.DataFrame(data, columns=['visit_detail_id', 'person_id', 'visit_detail_concept_id',  'visit_detail_start_date' ,'visit_detail_start_datetime','visit_detail_end_date','visit_detail_end_datetime',
                 'visit_detail_type_concept_id','provider_id','care_site_id','visit_detail_source_value','visit_detail_source_concept_id','admitted_from_concept_id','admitted_from_source_value',
                 'discharged_to_source_value', 'discharged_to_concept_id','preceding_visit_detail_id','parent_visit_detail_id','visit_occurrence_id'])

df_result.to_csv('visit_detail.csv', encoding='utf-8', index=False)