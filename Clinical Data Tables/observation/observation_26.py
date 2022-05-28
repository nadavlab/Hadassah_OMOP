import pandas as pd
from datetime import datetime
import math

source_table = pd.read_csv("26.csv")

### visit detail : ####
visit_detail_table = pd.read_csv("../visit/visit_detail.csv")
df_visit_detail_table = pd.DataFrame(visit_detail_table ,columns=['visit_detail_id', 'person_id','visit_occurrence_id', 'visit_detail_start_datetime', 'visit_detail_end_datetime'])

### visit occurrence : ####
visit_occurrence_table = pd.read_csv("../visit/visit_occurrence.csv")
df_visit_occurrence_table= pd.DataFrame(visit_occurrence_table ,columns=['visit_occurrence_id'])

data = []
index = 1
EHR_concept_id = 32817
#concept
Number_of_previous_pregnancies = 4078008
NumOfBirths_P = 118212000
NumOfAbortions_A = 248989003
NumOfEp_EP = 440537001
NumOfCaesars_CS = 4092787
NumOfLiveChildren_LC = 248991006
VBAC = 237313003


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

    observation_type_concept_id = EHR_concept_id

    match_visit_occurrence = df_visit_occurrence_table.loc[df_visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if match_visit_occurrence.shape[0] > 0 :
        visit_occurrence_id = row["Event_baznat"]
    else :
        visit_occurrence_id = ''

    visit_detail_id = ""
    if visit_occurrence_id != '':
        match_visit_detail = df_visit_detail_table.loc[df_visit_detail_table['visit_occurrence_id'] == visit_occurrence_id]
        index_visit_detail = 0
        if match_visit_detail.values.shape[0] > 0 :
            while match_visit_detail.values.shape[0] > index_visit_detail:
                date_start_vd = datetime.strptime(match_visit_detail.values[index_visit_detail][3] , '%Y-%m-%d %H:%M:%S')
                date_end_vd = datetime.strptime(match_visit_detail.values[index_visit_detail][4] , '%Y-%m-%d %H:%M:%S')
                if date_start_vd<=observation_datetime<=date_end_vd:
                    visit_detail_id = match_visit_detail.values[index_visit_detail][0]
                index_visit_detail+=1

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

    ############## NumOfPregnancies_G #############################
    if math.isnan(row['NumOfPregnancies_G']):
        observation_concept_id = Number_of_previous_pregnancies
        value_as_number = int(row['NumOfPregnancies_G'])
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1
    ############## NumOfBirths_P #############################

    if not math.isnan(row['NumOfBirths_P']):
        observation_concept_id = NumOfBirths_P
        value_as_number = int(row['NumOfBirths_P'])
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1
    ############## NumOfAbortions_A #############################
    if not math.isnan(row['NumOfAbortions_A']):
        observation_concept_id = NumOfAbortions_A
        value_as_number = int(row['NumOfAbortions_A'])
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1
    ############## NumOfEp_EP #############################
    if not math.isnan(row['NumOfEp_EP']):
        observation_concept_id = NumOfEp_EP
        value_as_number = int(row['NumOfEp_EP'])
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1
    ############## NumOfCaesars_CS #############################
    if not math.isnan(row['NumOfCaesars_CS']):
        observation_concept_id = NumOfCaesars_CS
        value_as_number = int(row['NumOfCaesars_CS'])
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1
    ############## NumOfLiveChildren_LC #############################
    if not math.isnan(row['NumOfLiveChildren_LC']):
        observation_concept_id = NumOfLiveChildren_LC
        value_as_number = int(row['NumOfLiveChildren_LC'])
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1
    ############## VBAC #############################
    if not math.isnan(row['VBAC']):
        observation_concept_id = VBAC
        value_as_number = int(row['VBAC'])
        data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                     value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                     observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
        index += 1

df_result = pd.DataFrame(data , columns=["observation_id", "person_id", "observation_concept_id", "observation_date", "observation_datetime", "observation_type_concept_id",
                 "value_as_number", "value_as_string", "value_as_concept_id", "qualifier_concept_id", "unit_concept_id", "provider_id", "visit_occurrence_id", "visit_detail_id",
                 "observation_source_value", "observation_source_concept_id", "unit_source_value", "qualifier_source_value", "value_source_value", "observation_event_id", "obs_event_field_concept_id"])

df_result.to_csv('observation_26.csv' , encoding='utf-8' , index=False)
