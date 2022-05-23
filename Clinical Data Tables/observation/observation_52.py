import pandas as pd
from datetime import datetime

source_table = pd.read_csv("52.csv")

visit_detail_table = pd.read_csv("../visit_detail.csv")
df_visit_detail_table = pd.DataFrame(visit_detail_table ,columns=['visit_detail_id', 'person_id','visit_occurrence_id', 'visit_detail_start_datetime', 'visit_detail_end_datetime'])

data = []
index = 1
EHR_concept_id = 32817

for index_row, row in source_table.iterrows():
    observation_id = index
    person_id = row["ID_BAZNAT"]

    ###date format
    try:
        dateT = datetime.strptime(row["זמן בדיקה"] , '%m/%d/%Y %H:%M')
    except:
        dateT = datetime.strptime(row["זמן בדיקה"] , '%m/%d/%Y %H:%M:%S %p')

    observation_date = dateT.date()
    observation_datetime = dateT

    observation_type_concept_id = EHR_concept_id
    visit_occurrence_id = row["Event_baznat"]  # event_baznat

    match_visit_detail = df_visit_detail_table.loc[df_visit_detail_table['visit_occurrence_id'] == visit_occurrence_id]
    index_visit_detail = 0
    if match_visit_detail.values.shape[0] > 0 :
        while match_visit_detail.values.shape[0] > index_visit_detail:
            date_start_vd = datetime.strptime(match_visit_detail.values[index_visit_detail][3] , '%Y-%m-%d %H:%M:%S')
            date_end_vd = datetime.strptime(match_visit_detail.values[index_visit_detail][4] , '%Y-%m-%d %H:%M:%S')
            if date_start_vd<=observation_datetime<=date_end_vd:
                visit_detail_id = match_visit_detail.values[index_visit_detail][0]
            index_visit_detail+=1

    else:
        visit_detail_id = ""

    value_as_number = ''
    try:
        value_as_string = datetime.strptime(row["זמן פקיעת קרומים"], '%m/%d/%Y %H:%M')
    except:
        value_as_string = datetime.strptime(row["זמן פקיעת קרומים"], '%m/%d/%Y %H:%M:%S %p')

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
    observation_concept_id = 0

    data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                 value_as_number, str(value_as_string), value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                 observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])

    ######################################### מי שפיר #####################################
    observation_concept_id = 0
    data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                 value_as_number, str(value_as_string), value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                 observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])

    index+=1

df_result = pd.DataFrame(data , columns=["observation_id", "person_id", "observation_concept_id", "observation_date", "observation_datetime", "observation_type_concept_id",
                 "value_as_number", "value_as_string", "value_as_concept_id", "qualifier_concept_id", "unit_concept_id", "provider_id", "visit_occurrence_id", "visit_detail_id",
                 "observation_source_value", "observation_source_concept_id", "unit_source_value", "qualifier_source_value", "value_source_value", "observation_event_id", "obs_event_field_concept_id"])

df_result.to_csv('observation_52.csv' , encoding='utf-8' , index=False)
