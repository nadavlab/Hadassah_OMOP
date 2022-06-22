import pandas as pd
from datetime import datetime

source_table = pd.read_csv("62.csv")
visit_detait_table = pd.read_csv("visit_detail.csv")
visit_occurrence_table = pd.read_csv("visit_occurrence.csv")
person_table = pd.read_csv("person.csv")


data = []
index = 3280599

for index_row, row in source_table.iterrows():

    observation_id = index
    person_id = row[0]
    match_person = person_table.loc[person_table['person_id'] == person_id]
    if match_person.empty:
        continue
    

    # TODO
    observation_concept_id = 0  # "צורת לידה"

    try:
        observation_datetime = datetime.strptime(
            row['Record_Date'], '%m/%d/%Y %H:%M:%S %p')
    except:
        observation_datetime = datetime.strptime(
            row['Record_Date'], '%d/%m/%Y %H:%M:%S %p')

    observation_date = observation_datetime.date()
    observation_date_string = observation_date.strftime('%Y-%m-%d')

    observation_type_concept_id = 32817  # EHR record
    value_as_number = ""

    temp_val = row[3]
    if temp_val == 'לא':
        value_as_string = 'טבעית'
    elif temp_val == 'כן':
        value_as_string=row[4]

    # TODO
    value_as_concept_id = ""
    qualifier_concept_id = ""
    unit_concept_id = ""
    provider_id = ""

    visit_occurrence_id = ""
    match_visit_occurrence = visit_occurrence_table.loc[visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if not match_visit_occurrence.empty:
        visit_occurrence_id = row["Event_baznat"]

    visit_detail_id = ""
    list_of_visits = visit_detait_table.loc[visit_detait_table['person_id'] == person_id]
    if list_of_visits.shape[0] != 1 and not list_of_visits.empty:
        row_of_visit = list_of_visits.loc[list_of_visits['visit_detail_start_date']
                                          == observation_date_string]
        if not row_of_visit.empty:
            visit_detail_id = row_of_visit['visit_detail_id'].values[0]
    elif not list_of_visits.empty:
        visit_detail_id = list_of_visits['visit_detail_id'].values[0]

    observation_source_value = "צורת לידה"
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""

    data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                 value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id, observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])

    index+=1

df_result = pd.DataFrame(data, columns=['observation_id', 'person_id', 'observation_concept_id', 'observation_date', 'observation_datetime', 'observation_type_concept_id',
                                        'value_as_number', 'value_as_string', 'value_as_concept_id', 'qualifier_concept_id', 'unit_concept_id', 'provider_id', 'visit_occurrence_id',
                                        'visit_detail_id', 'observation_source_value', 'observation_source_concept_id', 'unit_source_value', 'qualifier_source_value', 'value_source_value', 'observation_event_id',
                                        'obs_event_field_concept_id'])

df_result.to_csv('observation_62.csv', encoding='utf-8', index=False)
