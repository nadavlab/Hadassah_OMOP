import pandas as pd
from datetime import datetime

source_table = pd.read_csv("6.csv")
table_89_for_date = pd.read_csv("89.csv")
concepts_icd_table = pd.read_csv("concepts_icd_new_table.csv")
data = []
index = 1

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    condition_concept_id = ""  # TODO concept_id

    row_for_date = table_89_for_date.loc[table_89_for_date['ID_BAZNAT'] == person_id]
    date_start = datetime.strptime(
        row_for_date['HOSP_ENTRY_DATE'].values[0], '%d/%m/%Y %H:%M:%S')
    condition_start_date = date_start.date()
    condition_start_datetime = row_for_date['HOSP_ENTRY_DATE'].values[0]
    condition_end_date = ""
    condition_end_datetime = ""

    condition_type_concept_id = 32817  # EHR record
    condition_status_concept_id = ""
    stop_reason = ""
    provider_id = ""

    visit_occurrence_id = row[1]  # event_baznat
    row_for_date = table_89_for_date.loc[table_89_for_date['ID_BAZNAT'] == person_id]
    visit_detail_id = ""  # TODO need to use visit_detail_table
    condition_source_value = row[4]
    condition_source_concept_id = ""
    if row[3]:
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[3]]
        if not row_for_concept.empty:
            condition_source_concept_id = row_for_concept['concept_id'].values[0]
    condition_status_source_value = ""

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("15.csv")

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    condition_concept_id = ""  # TODO concept_id

    row_for_date = table_89_for_date.loc[table_89_for_date['ID_BAZNAT'] == person_id]
    date_start = datetime.strptime(
        row_for_date['HOSP_ENTRY_DATE'].values[0], '%d/%m/%Y %H:%M:%S')
    condition_start_date = date_start.date()
    condition_start_datetime = row_for_date['HOSP_ENTRY_DATE'].values[0]
    condition_end_date = ""
    condition_end_datetime = ""

    condition_type_concept_id = 32817  # EHR record
    condition_status_concept_id = ""
    stop_reason = ""
    provider_id = ""

    visit_occurrence_id = row[1]  # event_baznat
    visit_detail_id = ""  # TODO need to use visit_detail_table
    condition_source_value = row[4]
    condition_source_concept_id = ""
    if row[3]:
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[3]]
        if not row_for_concept.empty:
            condition_source_concept_id = row_for_concept['concept_id'].values[0]
    condition_status_source_value = ""

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("28.csv")

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    condition_concept_id = ""  # TODO concept_id

    date_start = datetime.strptime(row[14], '%d/%m/%Y %H:%M:%S')
    condition_start_date = date_start.date()
    condition_start_datetime = row[14]
    condition_end_date = ""
    condition_end_datetime = ""

    condition_type_concept_id = 32817  # EHR record
    condition_status_concept_id = ""
    stop_reason = ""
    provider_id = ""

    visit_occurrence_id = row[1]  # event_baznat
    visit_detail_id = ""  # TODO need to use visit_detail_table
    condition_source_value = row[12]
    condition_source_concept_id = ""
    if row[11]:
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[11]]
        if not row_for_concept.empty:
            condition_source_concept_id = row_for_concept['concept_id'].values[0]
    condition_status_source_value = ""

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


# table 31 - family conditions need to mapped to OBSERVATION table


source_table = pd.read_csv("40.csv")

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    condition_concept_id = ""  # TODO concept_id

    date_start = datetime.strptime(row[14], '%d/%m/%Y %H:%M:%S')
    condition_start_date = date_start.date()
    condition_start_datetime = row[14]
    condition_end_date = ""
    condition_end_datetime = ""

    condition_type_concept_id = 32817  # EHR record
    condition_status_concept_id = ""
    stop_reason = ""
    provider_id = ""

    visit_occurrence_id = row[1]  # event_baznat
    visit_detail_id = ""  # TODO need to use visit_detail_table
    condition_source_value = row[12]
    condition_source_concept_id = ""
    if row[10]:
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[10]]
        if not row_for_concept.empty:
            condition_source_concept_id = row_for_concept['concept_id'].values[0]
    condition_status_source_value = ""

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("56.csv")

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    condition_concept_id = ""  # TODO concept_id

    date_start = datetime.strptime(row[14], '%d/%m/%Y %H:%M:%S')
    condition_start_date = date_start.date()
    condition_start_datetime = row[14]
    condition_end_date = ""
    condition_end_datetime = ""

    condition_type_concept_id = 32817  # EHR record
    condition_status_concept_id = ""
    stop_reason = ""
    provider_id = ""

    visit_occurrence_id = row[1]  # event_baznat
    visit_detail_id = ""  # TODO need to use visit_detail_table
    condition_source_value = row[12]
    condition_source_concept_id = ""
    if row[10]:
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[10]]
        if not row_for_concept.empty:
            condition_source_concept_id = row_for_concept['concept_id'].values[0]
    condition_status_source_value = ""

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("63.csv")


for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    condition_concept_id = ""  # TODO concept_id

    date_start = datetime.strptime(row[14], '%d/%m/%Y %H:%M:%S')
    condition_start_date = date_start.date()
    condition_start_datetime = row[14]
    condition_end_date = ""
    condition_end_datetime = ""

    condition_type_concept_id = 32817  # EHR record
    condition_status_concept_id = ""
    stop_reason = ""
    provider_id = ""

    visit_occurrence_id = row[1]  # event_baznat
    visit_detail_id = ""  # TODO need to use visit_detail_table
    condition_source_value = row[12]
    condition_source_concept_id = ""
    if row[11]:
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[11]]
        if not row_for_concept.empty:
            condition_source_concept_id = row_for_concept['concept_id'].values[0]
    condition_status_source_value = ""

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("72.csv")

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    condition_concept_id = ""  # TODO concept_id

    date_start = datetime.strptime(row[14], '%d/%m/%Y %H:%M:%S')
    condition_start_date = date_start.date()
    condition_start_datetime = row[14]
    condition_end_date = ""
    condition_end_datetime = ""

    condition_type_concept_id = 32817  # EHR record
    condition_status_concept_id = ""
    stop_reason = ""
    provider_id = ""

    visit_occurrence_id = row[1]  # event_baznat
    visit_detail_id = ""  # TODO need to use visit_detail_table
    condition_source_value = row[12]
    condition_source_concept_id = ""
    if row[10]:
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[10]]
        if not row_for_concept.empty:
            condition_source_concept_id = row_for_concept['concept_id'].values[0]
    condition_status_source_value = ""

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("74.csv")

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    condition_concept_id = ""  # TODO concept_id

    date_start = datetime.strptime(row[15], '%d/%m/%Y %H:%M:%S')
    condition_start_date = date_start.date()
    condition_start_datetime = row[15]
    condition_end_date = ""
    condition_end_datetime = ""

    condition_type_concept_id = 32817  # EHR record
    condition_status_concept_id = ""
    stop_reason = ""
    provider_id = ""

    visit_occurrence_id = row[1]  # event_baznat
    visit_detail_id = ""  # TODO need to use visit_detail_table
    condition_source_value = row[13]
    condition_source_concept_id = ""
    if row[11]:
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[11]]
        if not row_for_concept.empty:
            condition_source_concept_id = row_for_concept['concept_id'].values[0]
    condition_status_source_value = ""

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("79.csv")

for index_row, row in source_table.iterrows():

    for index_row, row in source_table.iterrows():

        condition_occurrence_id = index
        person_id = row[0]
        condition_concept_id = ""  # TODO concept_id

        date_start = datetime.strptime(row[15], '%d/%m/%Y %H:%M:%S')
        condition_start_date = date_start.date()
        condition_start_datetime = row[15]
        condition_end_date = ""
        condition_end_datetime = ""

        condition_type_concept_id = 32817  # EHR record
        condition_status_concept_id = ""
        stop_reason = ""
        provider_id = ""

        visit_occurrence_id = row[1]  # event_baznat
        visit_detail_id = ""  # TODO need to use visit_detail_table
        condition_source_value = row[13]
        condition_source_concept_id = ""
        if row[11]:
            row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[11]]
            if not row_for_concept.empty:
                condition_source_concept_id = row_for_concept['concept_id'].values[0]
        condition_status_source_value = ""

        data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                    condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                    condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                    visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
        index += 1


source_table = pd.read_csv("80.csv")

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    condition_concept_id = ""  # TODO concept_id

    date_start = datetime.strptime(row[14], '%d/%m/%Y %H:%M:%S')
    condition_start_date = date_start.date()
    condition_start_datetime = row[14]
    condition_end_date = ""
    condition_end_datetime = ""

    condition_type_concept_id = 32817  # EHR record
    condition_status_concept_id = ""
    stop_reason = ""
    provider_id = ""

    visit_occurrence_id = row[1]  # event_baznat
    visit_detail_id = ""  # TODO need to use visit_detail_table
    condition_source_value = row[12]
    condition_source_concept_id = ""
    if row[10]:
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[10]]
        if not row_for_concept.empty:
            condition_source_concept_id = row_for_concept['concept_id'].values[0]
    condition_status_source_value = ""

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


df_result = pd.DataFrame(data, columns=['condition_occurrence_id', 'person_id', 'condition_concept_id', 'condition_start_date',
                         'condition_start_datetime', 'condition_end_date', 'condition_end_datetime', 'condition_type_concept_id',
                                        'condition_status_concept_id', 'stop_reason', 'provider_id', 'visit_occurrence_id', 'visit_detail_id',
                                        'condition_source_value', 'condition_source_concept_id', 'condition_status_source_value'])

df_result.to_csv('condition_occurence.csv', encoding='utf-8', index=False)