# Visit occurrence
#
# Parameters:
# place of service - Inpatient Visit 9201
# visit type - EHR
# Tables:
# source table = Hospitalization ranges
# OMP table - visit_occurrence


import pandas as pd
from datetime import datetime
import math
import numpy

source_table = pd.read_csv("89.csv")
care_site_table = pd.read_csv("CARE_SITE.csv")
dep_table = pd.read_csv("92.csv")

data=[]
index=1
inpatient_visit_concept_id = 9201
EHR_concept_id = 32817

for index_row, row in source_table.iterrows():
    if(float(row["Event_baznat"]) and not numpy.isnan(row["Event_baznat"])):
        visit_occurrence_id=int(row["Event_baznat"])
    if (float(row[0])and not numpy.isnan(row["Event_baznat"])):
        person_id=int(row[0])
    visit_concept_id=inpatient_visit_concept_id
    if type(row["HOSP_ENTRY_DATE"])!=str and math.isnan(row["HOSP_ENTRY_DATE"]):
        if  type(row["Cham_Hosp_Entry_Date"])!=str and math.isnan(row["Cham_Hosp_Entry_Date"]):
            visit_start_date = ''
            visit_start_datetime = ''
        else:
            date_start = datetime.strptime(row["Cham_Hosp_Entry_Date"] , '%d/%m/%Y %H:%M:%S')
            visit_start_date = date_start.date()
            visit_start_datetime = row["Cham_Hosp_Entry_Date"]

    else:
        date_start = datetime.strptime(row["HOSP_ENTRY_DATE"] , '%d/%m/%Y %H:%M:%S')
        visit_start_date = date_start.date()
        visit_start_datetime = row["HOSP_ENTRY_DATE"]


    if type(row["HOSP_EXIT_DATE"])!=str and math.isnan(row["HOSP_EXIT_DATE"]) :
        if type(row["Cham_Hosp_Exit_Date"])!=str and math.isnan(row["Cham_Hosp_Exit_Date"]) :
            visit_end_date = ''
            visit_end_datetime = ''
        else:
            date_end = datetime.strptime(row["Cham_Hosp_Exit_Date"] , '%d/%m/%Y %H:%M:%S')
            visit_end_date = date_end.date()
            visit_end_datetime = row["Cham_Hosp_Exit_Date"]
    else :
        date_end = datetime.strptime(row["HOSP_EXIT_DATE"] , '%d/%m/%Y %H:%M:%S')
        visit_end_date = date_end.date()
        visit_end_datetime = row["HOSP_EXIT_DATE"]

    #EHR
    visit_type_concept_id = EHR_concept_id
    provider_id = ''
    #care_site_id
    care_site_id = ''
    df_dep = pd.DataFrame(dep_table , columns=["ID_BAZNAT",	"Event_baznat",	"SORTER",	"Department",	"Department_Entry_Date",	"Department_Exit_Date"])
    match_event_baznat =  df_dep.loc[df_dep['Event_baznat'] == visit_occurrence_id]
    if match_event_baznat["Department"].size>0:
        df_care = pd.DataFrame(care_site_table ,columns=["care_site_id" , "care_site_name","place_of_service_concept_id"])
        care_site_name = match_event_baznat["Department"].values[0]
        match_care_site = df_care.loc[df_care["care_site_name"] == care_site_name]
        if match_care_site["care_site_id"].size > 0:
            care_site_id = match_care_site["care_site_id"].values[0]

    visit_detail_source_value=''
    visit_source_value=''
    #EHR
    visit_source_concept_id = EHR_concept_id
    admitted_from_concept_id = 0
    admitted_from_source_value = ''
    discharged_to_source_value = ''
    discharged_to_concept_id=''
    preceding_visit_occurrence_id=''
    data.append([visit_occurrence_id, person_id, visit_concept_id,  visit_start_date ,visit_start_datetime,visit_end_date,visit_end_datetime,
                 visit_type_concept_id,provider_id,care_site_id,visit_source_value,admitted_from_concept_id,admitted_from_source_value,
                 discharged_to_source_value, discharged_to_concept_id])
    index+=1

df_result = pd.DataFrame(data, columns=['visit_occurrence_id', 'person_id', 'visit_concept_id',  'visit_start_date' ,'visit_start_datetime','visit_end_date','visit_end_datetime',
                 'visit_type_concept_id','provider_id','care_site_id','visit_source_value','admitted_from_concept_id','admitted_from_source_value',
                 'discharged_to_source_value', 'discharged_to_concept_id'])

df_result.to_csv('visit_occurrence.csv', encoding='utf-8', index=False)
