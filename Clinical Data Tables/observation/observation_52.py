import math

import pandas as pd
from datetime import datetime

source_table = pd.read_csv("52.csv")

### visit detail : ####
visit_detail_table = pd.read_csv("../visit/visit_detail.csv")
df_visit_detail_table = pd.DataFrame(visit_detail_table ,columns=['visit_detail_id', 'person_id','visit_occurrence_id', 'visit_detail_start_datetime', 'visit_detail_end_datetime'])

### visit occurrence : ####
visit_occurrence_table = pd.read_csv("../visit/visit_occurrence.csv")
df_visit_occurrence_table= pd.DataFrame(visit_occurrence_table ,columns=['visit_occurrence_id'])

amniotic_fluid_table = pd.read_csv("amniotic_fluid.csv")
df_amniotic_fluid = pd.DataFrame(amniotic_fluid_table ,columns=['מי שפיר', 'concept'])

membranes_rupture_table = pd.read_csv("membranes_rupture.csv")
df_membranes_rupture_table = pd.DataFrame(membranes_rupture_table ,columns=['אופן פקיעת קרומים', 'concept'])



data = []
index = 1
EHR_CONCEPT_ID = 32817
AMNIOTIC_FLUID_CONCEPT_ID = 40454100
RUPTURED_MEMBRANES_CONCEPT_ID = 4224704

for index_row, row in source_table.iterrows():
    observation_id = index
    person_id = row["ID_BAZNAT"]

    ###date format
    if row["זמן בדיקה"] and type(row["זמן בדיקה"]) == str:
        try:
            dateT = datetime.strptime(row["זמן בדיקה"] , '%m/%d/%Y %H:%M')
        except:
            dateT = datetime.strptime(row["זמן בדיקה"] , '%m/%d/%Y %H:%M:%S %p')

        observation_date = dateT.date()
        observation_datetime = dateT

    observation_type_concept_id = EHR_CONCEPT_ID

    match_visit_occurrence = df_visit_occurrence_table.loc[
        df_visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
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

    if row["זמן פקיעת קרומים"] and type(row["זמן פקיעת קרומים"]) == str:
        try:
            value_as_string = datetime.strptime(row["זמן פקיעת קרומים"] , '%m/%d/%Y %H:%M')
        except:
            value_as_string = datetime.strptime(row["זמן פקיעת קרומים"] , '%m/%d/%Y %H:%M:%S %p')

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

    ################################## אופן פקיעת קרומים #################################
    if str(row["אופן פקיעת קרומים"]) :
        observation_concept_id = RUPTURED_MEMBRANES_CONCEPT_ID
        match = df_membranes_rupture_table.loc[df_membranes_rupture_table['אופן פקיעת קרומים'] == row["אופן פקיעת קרומים"]]
        if match.shape[0] > 0 :
            value = match.values[0][1]
            list_observation = value.split('+')
            index_concepts = 0
            while len(list_observation) > index_concepts:
                value_as_concept_id = list_observation[index_concepts]
                data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                             observation_type_concept_id ,
                             value_as_number , str(value_as_string) , value_as_concept_id , qualifier_concept_id ,
                             unit_concept_id , provider_id , visit_occurrence_id , visit_detail_id ,
                             observation_source_value , observation_source_concept_id , unit_source_value ,
                             qualifier_source_value , value_source_value , observation_event_id ,
                             obs_event_field_concept_id])
                index_concepts += 1
                index += 1

    ######################################### מי שפיר #####################################
    if str(row["מי שפיר"]) :
        observation_concept_id = AMNIOTIC_FLUID_CONCEPT_ID
        match = df_amniotic_fluid.loc[df_amniotic_fluid['מי שפיר'] == row["מי שפיר"]]
        if match.shape[0] > 0 :
            value_as_concept_id = match.values[0][1]
            data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
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

df_result.to_csv('observation_52.csv' , encoding='utf-8' , index=False)
