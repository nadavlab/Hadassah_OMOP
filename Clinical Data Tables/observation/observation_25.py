import pandas as pd
from datetime import datetime
import math

source_table = pd.read_csv("25.csv")

### visit detail : ####
visit_detail_table = pd.read_csv("../visit/visit_detail.csv")
df_visit_detail_table = pd.DataFrame(visit_detail_table ,columns=['visit_detail_id', 'person_id','visit_occurrence_id', 'visit_detail_start_datetime', 'visit_detail_end_datetime'])

### visit occurrence : ####
visit_occurrence_table = pd.read_csv("../visit/visit_occurrence.csv")
df_visit_occurrence_table= pd.DataFrame(visit_occurrence_table ,columns=['visit_occurrence_id'])

data = []
index = 1

EHR_CONCEPT_ID = 32817
DATE_OF_LAST_NORMAL_PERIOD = 4088445
SPONTANEOUS = 4196694
FETUS = 40567571
PREGNANCY_AGE = 0 # TODO!!!!

for index_row, row in source_table.iterrows():
    observation_id = index
    person_id = row["ID_BAZNAT"]

    ###date format
    try:
        date = datetime.strptime(row["Record_Date"] , '%d/%m/%Y %H:%M:%S')
    except:
        date = datetime.strptime(row["Record_Date"] , '%m/%d/%Y %H:%M:%S')
    observation_date = date.date()
    observation_datetime = date

    observation_type_concept_id = EHR_CONCEPT_ID

    match_visit_occurrence = df_visit_occurrence_table.loc[df_visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if match_visit_occurrence.shape[0] > 0 :
        visit_occurrence_id = row["Event_baznat"]
    else:
        visit_occurrence_id = ''

    visit_detail_id = ""
    if visit_occurrence_id != '':
        match_visit_detail = df_visit_detail_table.loc[df_visit_detail_table['visit_occurrence_id'] == visit_occurrence_id]
        index_visit_detail = 0
        if match_visit_detail.values.shape[0] > 0 :
            while match_visit_detail.values.shape[0] > index_visit_detail:
                date_start_vd = datetime.strptime(match_visit_detail.values[index_visit_detail][3] , '%Y-%m-%d %H:%M:%S')
                date_end_vd = datetime.strptime(match_visit_detail.values[index_visit_detail][4] , '%Y-%m-%d %H:%M:%S')
                if date_start_vd <= observation_datetime <= date_end_vd:
                    visit_detail_id = match_visit_detail.values[index_visit_detail][0]
                index_visit_detail += 1

    value_as_string = ''
    value_as_number = ''
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

    ############## Date of last normal period #############################
    if row['Last_Period_Date']:
        observation_concept_id = DATE_OF_LAST_NORMAL_PERIOD
        value_as_string = str(row['Last_Period_Date'])
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1
    ############## Spontaneous #############################

    if not math.isnan(row['Spontaneous']):
        observation_concept_id = SPONTANEOUS
        value_as_number = int(row['Spontaneous'])
        value_as_string = ''
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1
    ############## Fetus Count #############################
    if not math.isnan(row['Fetus_Count']):
        observation_concept_id = FETUS
        value_as_number = int(row['Fetus_Count'])
        value_as_string = ''
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1
    ############## Pregnancy Age #############################
    if row['Pregnancy_Age']:
        observation_concept_id = PREGNANCY_AGE
        value_as_number = ''
        value_as_string = str(row['Pregnancy_Age'])
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])

        index += 1

df_result = pd.DataFrame(data , columns=["observation_id", "person_id", "observation_concept_id", "observation_date", "observation_datetime", "observation_type_concept_id",
                 "value_as_number", "value_as_string", "value_as_concept_id", "qualifier_concept_id", "unit_concept_id", "provider_id", "visit_occurrence_id", "visit_detail_id",
                 "observation_source_value", "observation_source_concept_id", "unit_source_value", "qualifier_source_value", "value_source_value", "observation_event_id", "obs_event_field_concept_id"])

df_result.to_csv('observation_25.csv' , encoding='utf-8' , index=False)
