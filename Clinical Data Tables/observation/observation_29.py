import pandas as pd
from datetime import datetime

source_table = pd.read_csv("29.csv")
visit_detait_table = pd.read_csv("visit_detail.csv")

data = []
index = 1

# previous_pregnancies = [4049024, 4119100, 4205452, 4244737,
#                         4148926, 4330449, 4142640, 4214878, 4069849, 4221287, 4288592]

# TODO
# labor_type_map = {
#     'LSTCS': 37312440,
#     'Spontaneous vaginal birth': 441641,
#     'Vacuum birth': 4189205,
#     'Birth forceps': 4114637,
#     'Breech birth': 4034145,
#     'Mole': 4129710,
#     'Cesarean': 193277,
#     'Vacuum birth': 4189205
# }


for index_row, row in source_table.iterrows():
    # Previous pregnancies
    observation_id = index
    person_id = row[0]

    # TODO
    observation_concept_id = ""  # מספר הריון

    # prev_labor_num = row[2]
    # if prev_labor_num > 10:
    #     observation_concept_id = previous_pregnancies[10]
    # else:
    #     observation_concept_id = previous_pregnancies[prev_labor_num-1]

    observation_datetime = datetime.strptime(row[14], '%d/%m/%Y %H:%M:%S')
    observation_date = observation_datetime.date()
    observation_type_concept_id = 32817  # EHR record
    # TODO
    value_as_number = ""
    value_as_string = ""
    value_as_concept_id = ""
    qualifier_concept_id = ""
    unit_concept_id = ""
    provider_id = ""

    # TODO
    visit_occurrence_id = row[1]
    visit_detail_id = ""

    list_of_visits = visit_detait_table.loc[visit_detait_table['person_id'] == person_id]
    visit_detail_id = ""
    # TODO check
    # if list_of_visits.shape[0] != 1 and not list_of_visits.empty:
    #     row_of_visit = list_of_visits.loc[list_of_visits['visit_detail_start_datetime']
    #                                       == condition_start_datetime_string]
    #     if not row_of_visit.empty:
    #         visit_detail_id = row_of_visit['visit_detail_id'].values[0]
    # elif not list_of_visits.empty:
    #     visit_detail_id = list_of_visits['visit_detail_id'].values[0]

    observation_source_value = ""
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                 value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id, observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
    index += 1

    observation_id = index
    person_id = row[0]

    # TODO
    observation_concept_id = ""  # אופן סיום ההריון

    # prev_labor_num = row[2]
    # if prev_labor_num > 10:
    #     observation_concept_id = previous_pregnancies[10]
    # else:
    #     observation_concept_id = previous_pregnancies[prev_labor_num-1]

    observation_datetime = datetime.strptime(row[14], '%d/%m/%Y %H:%M:%S')
    observation_date = observation_datetime.date()
    observation_type_concept_id = 32817  # EHR record
    # TODO
    value_as_number = ""
    value_as_string = ""
    value_as_concept_id = ""
    qualifier_concept_id = ""
    unit_concept_id = ""
    provider_id = ""

    # TODO
    visit_occurrence_id = row[1]
    visit_detail_id = ""

    list_of_visits = visit_detait_table.loc[visit_detait_table['person_id'] == person_id]
    visit_detail_id = ""
    # TODO check
    # if list_of_visits.shape[0] != 1 and not list_of_visits.empty:
    #     row_of_visit = list_of_visits.loc[list_of_visits['visit_detail_start_datetime']
    #                                       == condition_start_datetime_string]
    #     if not row_of_visit.empty:
    #         visit_detail_id = row_of_visit['visit_detail_id'].values[0]
    # elif not list_of_visits.empty:
    #     visit_detail_id = list_of_visits['visit_detail_id'].values[0]

    observation_source_value = ""
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                 value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id, observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
    index += 1

    observation_id = index
    person_id = row[0]

    # TODO
    observation_concept_id = ""  # שנת סיום הריון

    # prev_labor_num = row[2]
    # if prev_labor_num > 10:
    #     observation_concept_id = previous_pregnancies[10]
    # else:
    #     observation_concept_id = previous_pregnancies[prev_labor_num-1]

    observation_datetime = datetime.strptime(row[14], '%d/%m/%Y %H:%M:%S')
    observation_date = observation_datetime.date()
    observation_type_concept_id = 32817  # EHR record
    # TODO
    value_as_number = ""
    value_as_string = ""
    value_as_concept_id = ""
    qualifier_concept_id = ""
    unit_concept_id = ""
    provider_id = ""

    # TODO
    visit_occurrence_id = row[1]
    visit_detail_id = ""

    list_of_visits = visit_detait_table.loc[visit_detait_table['person_id'] == person_id]
    visit_detail_id = ""
    # TODO check
    # if list_of_visits.shape[0] != 1 and not list_of_visits.empty:
    #     row_of_visit = list_of_visits.loc[list_of_visits['visit_detail_start_datetime']
    #                                       == condition_start_datetime_string]
    #     if not row_of_visit.empty:
    #         visit_detail_id = row_of_visit['visit_detail_id'].values[0]
    # elif not list_of_visits.empty:
    #     visit_detail_id = list_of_visits['visit_detail_id'].values[0]

    observation_source_value = ""
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                 value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id, observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
    index += 1

    observation_id = index
    person_id = row[0]

    # TODO
    observation_concept_id = ""  # שבוע סיום הריון

    # prev_labor_num = row[2]
    # if prev_labor_num > 10:
    #     observation_concept_id = previous_pregnancies[10]
    # else:
    #     observation_concept_id = previous_pregnancies[prev_labor_num-1]

    observation_datetime = datetime.strptime(row[14], '%d/%m/%Y %H:%M:%S')
    observation_date = observation_datetime.date()
    observation_type_concept_id = 32817  # EHR record
    # TODO
    value_as_number = ""
    value_as_string = ""
    value_as_concept_id = ""
    qualifier_concept_id = ""
    unit_concept_id = ""
    provider_id = ""

    # TODO
    visit_occurrence_id = row[1]
    visit_detail_id = ""

    list_of_visits = visit_detait_table.loc[visit_detait_table['person_id'] == person_id]
    visit_detail_id = ""
    # TODO check
    # if list_of_visits.shape[0] != 1 and not list_of_visits.empty:
    #     row_of_visit = list_of_visits.loc[list_of_visits['visit_detail_start_datetime']
    #                                       == condition_start_datetime_string]
    #     if not row_of_visit.empty:
    #         visit_detail_id = row_of_visit['visit_detail_id'].values[0]
    # elif not list_of_visits.empty:
    #     visit_detail_id = list_of_visits['visit_detail_id'].values[0]

    observation_source_value = ""
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                 value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id, observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
    index += 1

    observation_id = index
    person_id = row[0]

    # TODO
    observation_concept_id = ""  # מספר עוברים

    # prev_labor_num = row[2]
    # if prev_labor_num > 10:
    #     observation_concept_id = previous_pregnancies[10]
    # else:
    #     observation_concept_id = previous_pregnancies[prev_labor_num-1]

    observation_datetime = datetime.strptime(row[14], '%d/%m/%Y %H:%M:%S')
    observation_date = observation_datetime.date()
    observation_type_concept_id = 32817  # EHR record
    # TODO
    value_as_number = ""
    value_as_string = ""
    value_as_concept_id = ""
    qualifier_concept_id = ""
    unit_concept_id = ""
    provider_id = ""

    # TODO
    visit_occurrence_id = row[1]
    visit_detail_id = ""

    list_of_visits = visit_detait_table.loc[visit_detait_table['person_id'] == person_id]
    visit_detail_id = ""
    # TODO check
    # if list_of_visits.shape[0] != 1 and not list_of_visits.empty:
    #     row_of_visit = list_of_visits.loc[list_of_visits['visit_detail_start_datetime']
    #                                       == condition_start_datetime_string]
    #     if not row_of_visit.empty:
    #         visit_detail_id = row_of_visit['visit_detail_id'].values[0]
    # elif not list_of_visits.empty:
    #     visit_detail_id = list_of_visits['visit_detail_id'].values[0]

    observation_source_value = ""
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                 value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id, observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
    index += 1

    observation_id = index
    person_id = row[0]

    # TODO
    observation_concept_id = ""  # הילוד(חי או מת)

    # prev_labor_num = row[2]
    # if prev_labor_num > 10:
    #     observation_concept_id = previous_pregnancies[10]
    # else:
    #     observation_concept_id = previous_pregnancies[prev_labor_num-1]

    observation_datetime = datetime.strptime(row[14], '%d/%m/%Y %H:%M:%S')
    observation_date = observation_datetime.date()
    observation_type_concept_id = 32817  # EHR record
    # TODO
    value_as_number = ""
    value_as_string = ""
    value_as_concept_id = ""
    qualifier_concept_id = ""
    unit_concept_id = ""
    provider_id = ""

    # TODO
    visit_occurrence_id = row[1]
    visit_detail_id = ""

    list_of_visits = visit_detait_table.loc[visit_detait_table['person_id'] == person_id]
    visit_detail_id = ""
    # TODO check
    # if list_of_visits.shape[0] != 1 and not list_of_visits.empty:
    #     row_of_visit = list_of_visits.loc[list_of_visits['visit_detail_start_datetime']
    #                                       == condition_start_datetime_string]
    #     if not row_of_visit.empty:
    #         visit_detail_id = row_of_visit['visit_detail_id'].values[0]
    # elif not list_of_visits.empty:
    #     visit_detail_id = list_of_visits['visit_detail_id'].values[0]

    observation_source_value = ""
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id,
                 value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id, observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id])
    index += 1


df_result = pd.DataFrame(data, columns=['observation_id', 'person_id', 'observation_concept_id', 'observation_date', 'observation_datetime', 'observation_type_concept_id',
                                        'value_as_number', 'value_as_string', 'value_as_concept_id', 'qualifier_concept_id', 'unit_concept_id', 'provider_id', 'visit_occurrence_id',
                                        'visit_detail_id', 'observation_source_value', 'observation_source_concept_id', 'unit_source_value', 'qualifier_source_value', 'value_source_value', 'observation_event_id',
                                        'obs_event_field_concept_id'])

df_result.to_csv('observation.csv', encoding='utf-8', index=False)
