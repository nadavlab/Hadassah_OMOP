import pandas as pd
from datetime import datetime

source_table = pd.read_csv("24.csv")
terms_table = pd.read_csv("24_Usagi.csv")
df_terms_table = pd.DataFrame(terms_table ,columns=['sourceCode', 'SNOMED'])

### visit detail : ####
visit_detail_table = pd.read_csv("../visit/visit_detail.csv")
df_visit_detail_table = pd.DataFrame(visit_detail_table ,columns=['visit_detail_id', 'person_id','visit_occurrence_id', 'visit_detail_start_datetime', 'visit_detail_end_datetime'])

### visit occurrence : ####
visit_occurrence_table = pd.read_csv("../visit/visit_occurrence.csv")
df_visit_occurrence_table= pd.DataFrame(visit_occurrence_table ,columns=['visit_occurrence_id'])


data = []
index = 1
EHR_CONCEPT_ID = 32817
MATERNITY_CLINIC = 4190427

for index_row, row in source_table.iterrows():
    observation_id = index
    person_id = row["ID_BAZNAT"]

    ###date format
    try:
        date = datetime.strptime(row["Record_Date"] , '%d/%m/%Y %H:%M:%S')
    except:
        date = datetime.strptime(row["Record_Date"] , '%d/%m/%Y %H:%M')
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
                if date_start_vd<=observation_datetime<=date_end_vd:
                    visit_detail_id = match_visit_detail.values[index_visit_detail][0]
                index_visit_detail += 1

    value_as_number = ''
    value_as_string = ''
    value_as_concept_id = ''
    qualifier_concept_id = ""
    unit_concept_id = MATERNITY_CLINIC
    provider_id = ""
    observation_source_value = ""
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""
    if str(row["סיבה עיקרית"]) and row["סיבה עיקרית"] != '-1':
        match_visit_occurrence = df_terms_table.loc[df_terms_table['sourceCode'] == row["סיבה עיקרית"]]
        value = match_visit_occurrence.values[0][1]
        list_observation = value.split('+')
        index_concepts = 0
        while len(list_observation) > index_concepts:
            observation_concept_id = list_observation[index_concepts]
            data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                         value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id,
                         observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
            index_concepts += 1
            index += 1
df_result = pd.DataFrame(data , columns=["observation_id", "person_id", "observation_concept_id", "observation_date", "observation_datetime", "observation_type_concept_id",
                 "value_as_number", "value_as_string", "value_as_concept_id", "qualifier_concept_id", "unit_concept_id", "provider_id", "visit_occurrence_id", "visit_detail_id",
                 "observation_source_value", "observation_source_concept_id", "unit_source_value", "qualifier_source_value", "value_source_value", "observation_event_id", "obs_event_field_concept_id"])

df_result.to_csv('observation_24.csv' , encoding='utf-8' , index=False)
