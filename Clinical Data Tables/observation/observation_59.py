import math

import pandas as pd
from datetime import datetime

source_table = pd.read_csv("59.csv")

### visit detail : ####
visit_detail_table = pd.read_csv("../visit/visit_detail.csv")
df_visit_detail_table = pd.DataFrame(visit_detail_table ,columns=['visit_detail_id', 'person_id','visit_occurrence_id', 'visit_detail_start_datetime', 'visit_detail_end_datetime'])

### visit occurrence : ####
visit_occurrence_table = pd.read_csv("../visit/visit_occurrence.csv")
df_visit_occurrence_table= pd.DataFrame(visit_occurrence_table ,columns=['visit_occurrence_id'])

data = []
index = 1

EHR_CONCEPT_ID = 32817
HINGES_START_TIME = 249123005
FULL_OPENING_TIME = 249160009
DURATION_OF_PERIOD_1 = 169821004
FETAL_DEPARTURE_TIME = 397836004
DURATION_OF_PERIOD_2 = 169822006
PLACENTAL_EXIT_TIME = 249169005
DURATION_OF_PERIOD_3 = 169823001
MEMBRANES_TIME = 289251005

for index_row, row in source_table.iterrows():
    observation_id = index
    person_id = row["ID_BAZNAT"]

    ###date format
    if row["Record_Date"] and type(row["Record_Date"]) == str:
        try:
            dateT = datetime.strptime(row["Record_Date"] , '%m/%d/%Y %H:%M')
        except:
            dateT = datetime.strptime(row["Record_Date"] , '%m/%d/%Y %H:%M:%S %p')

        observation_date = dateT.date()
        observation_datetime = dateT

    observation_type_concept_id = EHR_CONCEPT_ID

    match_visit_occurrence = df_visit_occurrence_table.loc[df_visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if match_visit_occurrence.shape[0] > 0 :
        visit_occurrence_id = row["Event_baznat"]
    else :
        visit_occurrence_id = ''

    visit_detail_id = ""
    if visit_occurrence_id != '' :
        match_visit_detail = df_visit_detail_table.loc[df_visit_detail_table['visit_occurrence_id'] == visit_occurrence_id]
        index_visit_detail = 0
        if match_visit_detail.values.shape[0] > 0 :
            while match_visit_detail.values.shape[0] > index_visit_detail:
                date_start_vd = datetime.strptime(match_visit_detail.values[index_visit_detail][3] , '%Y-%m-%d %H:%M:%S')
                date_end_vd = datetime.strptime(match_visit_detail.values[index_visit_detail][4] , '%Y-%m-%d %H:%M:%S')
                if date_start_vd <= observation_datetime <= date_end_vd:
                    visit_detail_id = match_visit_detail.values[index_visit_detail][0]
                index_visit_detail+=1

    value_as_number = ''
    value_as_string = ''
    value_as_concept_id = ''
    qualifier_concept_id = ""
    unit_concept_id = ""
    provider_id = ""
    observation_source_value = ""
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""

    ################################## זמן תחילת צירים #################################
    if str(row["זמן תחילת צירים"]):
        observation_concept_id = HINGES_START_TIME
        if row["זמן תחילת צירים"] and type(row["זמן תחילת צירים"]) == str :
            try :
                value_as_string = datetime.strptime(row["זמן תחילת צירים"] , '%m/%d/%Y %H:%M')
            except :
                value_as_string = datetime.strptime(row["זמן תחילת צירים"] , '%m/%d/%Y %H:%M:%S %p')
        data.append([observation_id , person_id , observation_concept_id , str(observation_date) , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , str(value_as_string) , value_as_concept_id , qualifier_concept_id ,
                     unit_concept_id , provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id ,
                     obs_event_field_concept_id])
        index += 1

    ################################## זמן פתיחה מלאה #################################
    if str(row["זמן פתיחה מלאה"]):
        observation_concept_id = FULL_OPENING_TIME
        if row["זמן תחילת צירים"] and type(row["זמן תחילת צירים"]) == str :
            try :
                value_as_string = datetime.strptime(row["זמן תחילת צירים"] , '%m/%d/%Y %H:%M')
            except :
                value_as_string = datetime.strptime(row["זמן תחילת צירים"] , '%m/%d/%Y %H:%M:%S %p')
        data.append([observation_id , person_id , observation_concept_id , str(observation_date) , observation_datetime,
                     observation_type_concept_id ,
                     value_as_number , str(value_as_string) , value_as_concept_id , qualifier_concept_id ,
                     unit_concept_id , provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id ,
                     obs_event_field_concept_id])
        index += 1

    ################################## משך תקופה 1 #################################
    if str(row["משך תקופה 1"]):
        observation_concept_id = DURATION_OF_PERIOD_1
        value_as_string = row["משך תקופה 1"]
        data.append([observation_id , person_id , observation_concept_id , str(observation_date) , observation_datetime,
                     observation_type_concept_id ,
                     value_as_number , str(value_as_string) , value_as_concept_id , qualifier_concept_id ,
                     unit_concept_id , provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id ,
                     obs_event_field_concept_id])
        index += 1

    ################################## זמן יציאת עובר #################################
    if str(row["זמן יציאת עובר"]):
        observation_concept_id = FULL_OPENING_TIME
        if row["זמן יציאת עובר"] and type(row["זמן יציאת עובר"]) == str :
            try :
                value_as_string = datetime.strptime(row["זמן יציאת עובר"] , '%m/%d/%Y %H:%M')
            except :
                value_as_string = datetime.strptime(row["זמן יציאת עובר"] , '%m/%d/%Y %H:%M:%S %p')
        data.append([observation_id , person_id , observation_concept_id , str(observation_date) , observation_datetime,
                     observation_type_concept_id ,
                     value_as_number , str(value_as_string) , value_as_concept_id , qualifier_concept_id ,
                     unit_concept_id , provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id ,
                     obs_event_field_concept_id])
        index += 1

    ################################## משך תקופה 2 #################################
    if str(row["משך תקופה 2"]):
        observation_concept_id = DURATION_OF_PERIOD_2
        value_as_string = row["משך תקופה 2"]
        data.append([observation_id , person_id , observation_concept_id , str(observation_date) , observation_datetime,
                     observation_type_concept_id ,
                     value_as_number , str(value_as_string) , value_as_concept_id , qualifier_concept_id ,
                     unit_concept_id , provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id ,
                     obs_event_field_concept_id])
        index += 1

    ################################## זמן יציאת שלייה #################################
    if str(row["זמן יציאת שלייה"]):
        observation_concept_id = FULL_OPENING_TIME
        if row["זמן יציאת שלייה"] and type(row["זמן יציאת שלייה"]) == str :
            try :
                value_as_string = datetime.strptime(row["זמן יציאת שלייה"] , '%m/%d/%Y %H:%M')
            except :
                value_as_string = datetime.strptime(row["זמן יציאת שלייה"] , '%m/%d/%Y %H:%M:%S %p')
        data.append([observation_id , person_id , observation_concept_id , str(observation_date) , observation_datetime,
                     observation_type_concept_id ,
                     value_as_number , str(value_as_string) , value_as_concept_id , qualifier_concept_id ,
                     unit_concept_id , provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id ,
                     obs_event_field_concept_id])
        index += 1

    ################################## משך תקופה 3 #################################
    if str(row["משך תקופה 3"]):
        observation_concept_id = DURATION_OF_PERIOD_3
        value_as_string = row["משך תקופה 3"]
        data.append([observation_id , person_id , observation_concept_id , str(observation_date) , observation_datetime,
                     observation_type_concept_id ,
                     value_as_number , str(value_as_string) , value_as_concept_id , qualifier_concept_id ,
                     unit_concept_id , provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id ,
                     obs_event_field_concept_id])
        index += 1

    ################################## משך תקופה 3 #################################
    if str(row["משך תקופה מזמן פקיעת קרומים עד יציאת עובר"]):
        observation_concept_id = MEMBRANES_TIME
        value_as_string = row["משך תקופה מזמן פקיעת קרומים עד יציאת עובר"]
        data.append([observation_id , person_id , observation_concept_id , str(observation_date) , observation_datetime,
                     observation_type_concept_id ,
                     value_as_number , str(value_as_string) , value_as_concept_id , qualifier_concept_id ,
                     unit_concept_id , provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id ,
                     obs_event_field_concept_id])
        index += 1


df_result = pd.DataFrame(data , columns=["observation_id", "person_id", "observation_concept_id", "observation_date", "observation_datetime", "observation_type_concept_id",
                 "value_as_number", "value_as_string", "value_as_concept_id", "qualifier_concept_id", "unit_concept_id", "provider_id", "visit_occurrence_id", "visit_detail_id",
                 "observation_source_value", "observation_source_concept_id", "unit_source_value", "qualifier_source_value", "value_source_value", "observation_event_id", "obs_event_field_concept_id"])

df_result.to_csv('observation_59.csv' , encoding='utf-8' , index=False)
