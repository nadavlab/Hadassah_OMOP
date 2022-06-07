import pandas as pd
from datetime import datetime
import math
from enum import Enum
source_table = pd.read_csv("25.csv")
from num2words import num2words

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
PREGNANCY_AGE = 444135009
PREGNANCY_AGE_BY_WEEK = 366323009


class Preganancy_age_enum(Enum):
    TWENTY = 23464008
    TWENTY_ONE = 41438001
    TWENTY_TWO = 65035007
    TWENTY_THREE = 86883006
    TWENTY_FOUR = 313179009
    TWENTY_FIVE = 72544005
    TWENTY_SEX = 48688005
    TWENTY_SEVEN = 46906003
    TWENTY_EIGHT = 90797000
    TWENTY_NINE = 45139008
    THIRTY = 71355009
    THIRTY_ONE = 64920003
    THIRTY_TWO = 7707000
    THIRTY_THREE = 78395001
    THIRTY_FOUR = 13763000
    THIRTY_FIVE = 84132007
    THIRTY_SEX = 57907009
    THIRTY_SEVEN = 43697006
    THIRTY_EIGHT = 13798002
    THIRTY_NINE = 80487005
    FORTY = 46230007
    FORTY_ONE = 63503002
    FORTY_TWO = 36428009
    FORTY_THREE = 90968009
    FORTY_FOUR = 90968009


for index_row, row in source_table.iterrows():
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
        observation_id = index
        observation_concept_id = DATE_OF_LAST_NORMAL_PERIOD
        value_as_string = str(row['Last_Period_Date'])
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1
    ############## Spontaneous #############################

    if not math.isnan(row['Spontaneous']):
        observation_id = index
        observation_concept_id = SPONTANEOUS
        value_as_number = int(row['Spontaneous'])
        value_as_string = ''
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1
    ############## Fetus Count #############################
    if not math.isnan(row['Fetus_Count']):
        observation_id = index
        observation_concept_id = FETUS
        value_as_number = int(row['Fetus_Count'])
        value_as_string = ''
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1
    ############## Pregnancy Age #############################
    if row['Pregnancy_Age']:
        observation_id = index
        observation_concept_id = PREGNANCY_AGE
        value_as_number = ''
        value_as_string = str(row['Pregnancy_Age'])
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1

        observation_id = index
        observation_concept_id = PREGNANCY_AGE_BY_WEEK
        value_as_number = ''
        value_as_string = ''
        week = row['Pregnancy_Age'].split('+')[0]
        week_in_words = num2words(row['Pregnancy_Age'].split('+')[0]).upper().replace('-','_')
        value_as_concept_id = Preganancy_age_enum[week_in_words].value
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1

df_result = pd.DataFrame(data , columns=["observation_id", "person_id", "observation_concept_id", "observation_date", "observation_datetime", "observation_type_concept_id",
                 "value_as_number", "value_as_string", "value_as_concept_id", "qualifier_concept_id", "unit_concept_id", "provider_id", "visit_occurrence_id", "visit_detail_id",
                 "observation_source_value", "observation_source_concept_id", "unit_source_value", "qualifier_source_value", "value_source_value", "observation_event_id", "obs_event_field_concept_id"])

df_result.to_csv('observation_25.csv' , encoding='utf-8' , index=False)
