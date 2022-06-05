import pandas as pd
from datetime import datetime

source_table = pd.read_csv("27.csv")
visit_detait_table = pd.read_csv("visit_detail.csv")
visit_occurrence_table = pd.read_csv("visit_occurrence.csv")


data = []
index = 1


for index_row, row in source_table.iterrows():

    observation_id = index
    person_id = row[0]

    # TODO
    observation_concept_id = 0  # מספר הריון

    observation_datetime = datetime.strptime(row[14], '%d/%m/%Y %H:%M')
    observation_date = observation_datetime.date()
    observation_date_string = observation_date.strftime('%Y-%m-%d')

    observation_type_concept_id = 32817  # EHR record

    value_as_number = row[3]
    value_as_string = ""
    value_as_concept_id = ""
    qualifier_concept_id = ""
    unit_concept_id = ""
    provider_id = ""

    visit_occurrence_id = ""
    list_of_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['person_id'] == person_id]
    if list_of_visit_occurrence.shape[0] != 1 and not list_of_visit_occurrence.empty:
        row_of_visit_occurrence = list_of_visit_occurrence.loc[list_of_visit_occurrence['visit_start_date']
                                                               == observation_date_string]
        if not row_of_visit_occurrence.empty:
            visit_occurrence_id = row_of_visit_occurrence['visit_occurrence_id'].values[0]
    elif not list_of_visit_occurrence.empty:
        visit_occurrence_id = list_of_visit_occurrence['visit_occurrence_id'].values[0]

    visit_detail_id = ""
    list_of_visits = visit_detait_table.loc[visit_detait_table['person_id'] == person_id]
    if list_of_visits.shape[0] != 1 and not list_of_visits.empty:
        row_of_visit = list_of_visits.loc[list_of_visits['visit_detail_start_date']
                                          == observation_date_string]
        if not row_of_visit.empty:
            visit_detail_id = row_of_visit['visit_detail_id'].values[0]
    elif not list_of_visits.empty:
        visit_detail_id = list_of_visits['visit_detail_id'].values[0]

    observation_source_value = "מספר הריון"
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""

    data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                 value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id, observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
    index += 1

    observation_id = index
    person_id = row[0]

    # TODO
    observation_concept_id = 0  # אופן סיום ההריון

    observation_datetime = datetime.strptime(row[14], '%d/%m/%Y %H:%M')
    observation_date = observation_datetime.date()
    observation_date_string = observation_date.strftime('%Y-%m-%d')

    observation_type_concept_id = 32817  # EHR record

    value_as_number = ""
    value_as_string = row[5]

    # TODO
    value_as_concept_id = ""

    qualifier_concept_id = ""
    unit_concept_id = ""
    provider_id = ""

    visit_occurrence_id = ""
    list_of_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['person_id'] == person_id]
    if list_of_visit_occurrence.shape[0] != 1 and not list_of_visit_occurrence.empty:
        row_of_visit_occurrence = list_of_visit_occurrence.loc[list_of_visit_occurrence['visit_start_date']
                                                               == observation_date_string]
        if not row_of_visit_occurrence.empty:
            visit_occurrence_id = row_of_visit_occurrence['visit_occurrence_id'].values[0]
    elif not list_of_visit_occurrence.empty:
        visit_occurrence_id = list_of_visit_occurrence['visit_occurrence_id'].values[0]

    visit_detail_id = ""
    list_of_visits = visit_detait_table.loc[visit_detait_table['person_id'] == person_id]
    if list_of_visits.shape[0] != 1 and not list_of_visits.empty:
        row_of_visit = list_of_visits.loc[list_of_visits['visit_detail_start_date']
                                          == observation_date_string]
        if not row_of_visit.empty:
            visit_detail_id = row_of_visit['visit_detail_id'].values[0]
    elif not list_of_visits.empty:
        visit_detail_id = list_of_visits['visit_detail_id'].values[0]

    observation_source_value = "אופן סיום ההריון"
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""

    data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                 value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id, observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
    index += 1

    observation_id = index
    person_id = row[0]

    # TODO
    observation_concept_id = 0  # שנת סיום הריון

    observation_datetime = datetime.strptime(row[14], '%d/%m/%Y %H:%M')
    observation_date = observation_datetime.date()
    observation_date_string = observation_date.strftime('%Y-%m-%d')

    observation_type_concept_id = 32817  # EHR record

    value_as_number = row[6]
    value_as_string = ""
    value_as_concept_id = ""
    qualifier_concept_id = ""
    unit_concept_id = ""
    provider_id = ""

    visit_occurrence_id = ""
    list_of_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['person_id'] == person_id]
    if list_of_visit_occurrence.shape[0] != 1 and not list_of_visit_occurrence.empty:
        row_of_visit_occurrence = list_of_visit_occurrence.loc[list_of_visit_occurrence['visit_start_date']
                                                               == observation_date_string]
        if not row_of_visit_occurrence.empty:
            visit_occurrence_id = row_of_visit_occurrence['visit_occurrence_id'].values[0]
    elif not list_of_visit_occurrence.empty:
        visit_occurrence_id = list_of_visit_occurrence['visit_occurrence_id'].values[0]

    visit_detail_id = ""
    list_of_visits = visit_detait_table.loc[visit_detait_table['person_id'] == person_id]
    if list_of_visits.shape[0] != 1 and not list_of_visits.empty:
        row_of_visit = list_of_visits.loc[list_of_visits['visit_detail_start_date']
                                          == observation_date_string]
        if not row_of_visit.empty:
            visit_detail_id = row_of_visit['visit_detail_id'].values[0]
    elif not list_of_visits.empty:
        visit_detail_id = list_of_visits['visit_detail_id'].values[0]

    observation_source_value = "שנת סיום הריון"
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""

    data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                 value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id, observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
    index += 1

    observation_id = index
    person_id = row[0]

    # TODO
    observation_concept_id = 0  # שבוע סיום הריון

    observation_datetime = datetime.strptime(row[14], '%d/%m/%Y %H:%M')
    observation_date = observation_datetime.date()
    observation_date_string = observation_date.strftime('%Y-%m-%d')

    observation_type_concept_id = 32817  # EHR record

    value_as_number = row[7]
    value_as_string = ""
    value_as_concept_id = ""
    qualifier_concept_id = ""
    unit_concept_id = ""
    provider_id = ""

    visit_occurrence_id = ""
    list_of_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['person_id'] == person_id]
    if list_of_visit_occurrence.shape[0] != 1 and not list_of_visit_occurrence.empty:
        row_of_visit_occurrence = list_of_visit_occurrence.loc[list_of_visit_occurrence['visit_start_date']
                                                               == observation_date_string]
        if not row_of_visit_occurrence.empty:
            visit_occurrence_id = row_of_visit_occurrence['visit_occurrence_id'].values[0]
    elif not list_of_visit_occurrence.empty:
        visit_occurrence_id = list_of_visit_occurrence['visit_occurrence_id'].values[0]

    visit_detail_id = ""
    list_of_visits = visit_detait_table.loc[visit_detait_table['person_id'] == person_id]
    if list_of_visits.shape[0] != 1 and not list_of_visits.empty:
        row_of_visit = list_of_visits.loc[list_of_visits['visit_detail_start_date']
                                          == observation_date_string]
        if not row_of_visit.empty:
            visit_detail_id = row_of_visit['visit_detail_id'].values[0]
    elif not list_of_visits.empty:
        visit_detail_id = list_of_visits['visit_detail_id'].values[0]

    observation_source_value = "שבוע סיום הריון"
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""

    data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                 value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id, observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
    index += 1

    observation_id = index
    person_id = row[0]

    # TODO
    observation_concept_id = 0  # מספר עוברים

    observation_datetime = datetime.strptime(row[14], '%d/%m/%Y %H:%M')
    observation_date = observation_datetime.date()
    observation_date_string = observation_date.strftime('%Y-%m-%d')

    observation_type_concept_id = 32817  # EHR record

    value_as_number = row[8]
    value_as_string = ""
    value_as_concept_id = ""
    qualifier_concept_id = ""
    unit_concept_id = ""
    provider_id = ""

    visit_occurrence_id = ""
    list_of_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['person_id'] == person_id]
    if list_of_visit_occurrence.shape[0] != 1 and not list_of_visit_occurrence.empty:
        row_of_visit_occurrence = list_of_visit_occurrence.loc[list_of_visit_occurrence['visit_start_date']
                                                               == observation_date_string]
        if not row_of_visit_occurrence.empty:
            visit_occurrence_id = row_of_visit_occurrence['visit_occurrence_id'].values[0]
    elif not list_of_visit_occurrence.empty:
        visit_occurrence_id = list_of_visit_occurrence['visit_occurrence_id'].values[0]

    visit_detail_id = ""
    list_of_visits = visit_detait_table.loc[visit_detait_table['person_id'] == person_id]
    if list_of_visits.shape[0] != 1 and not list_of_visits.empty:
        row_of_visit = list_of_visits.loc[list_of_visits['visit_detail_start_date']
                                          == observation_date_string]
        if not row_of_visit.empty:
            visit_detail_id = row_of_visit['visit_detail_id'].values[0]
    elif not list_of_visits.empty:
        visit_detail_id = list_of_visits['visit_detail_id'].values[0]

    observation_source_value = "מספר עוברים"
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""

    data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                 value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id, observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
    index += 1

    observation_id = index
    person_id = row[0]


df_result = pd.DataFrame(data, columns=['observation_id', 'person_id', 'observation_concept_id', 'observation_date', 'observation_datetime', 'observation_type_concept_id',
                                        'value_as_number', 'value_as_string', 'value_as_concept_id', 'qualifier_concept_id', 'unit_concept_id', 'provider_id', 'visit_occurrence_id',
                                        'visit_detail_id', 'observation_source_value', 'observation_source_concept_id', 'unit_source_value', 'qualifier_source_value', 'value_source_value', 'observation_event_id',
                                        'obs_event_field_concept_id'])

df_result.to_csv('observation_27.csv', encoding='utf-8', index=False)
