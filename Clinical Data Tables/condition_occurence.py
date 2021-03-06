import pandas as pd
from datetime import datetime


table_89_for_date = pd.read_csv("89.csv")
# concept ICD9 from Athena
concepts_icd_table = pd.read_csv("concepts_icd9.csv")
concept_Yishay_table = pd.read_csv("YS_28_03_22.csv")
visit_occurrence_table = pd.read_csv("visit_occurrence.csv")
visit_detait_table = pd.read_csv("visit_detail.csv")
person_table = pd.read_csv("person.csv")


def get_visit_detail(person_id, condition_start_datetime_string):
    visit_detail_id = ""
    list_of_visits = visit_detait_table.loc[visit_detait_table['person_id'] == person_id]

    if list_of_visits.shape[0] != 1 and not list_of_visits.empty:
        row_of_visit = list_of_visits.loc[list_of_visits['visit_detail_start_datetime']
                                          == condition_start_datetime_string]
        if not row_of_visit.empty:
            visit_detail_id = row_of_visit['visit_detail_id'].values[0]
    elif not list_of_visits.empty:
        visit_detail_id = list_of_visits['visit_detail_id'].values[0]
    return visit_detail_id


data = []
index = 1

source_table = pd.read_csv("6.csv")

condition_type_concept_id = 32817  # EHR record
condition_status_concept_id = ""
stop_reason = ""
provider_id = ""
condition_status_source_value = ""

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    match_person = person_table.loc[person_table['person_id'] == person_id]
    if match_person.empty:
        continue

    condition_concept_id = 0
    row_for_concept_id = concept_Yishay_table.loc[concept_Yishay_table['sourceCode'] == row[3]]
    if not row_for_concept_id.empty:
        if row_for_concept_id['targetDomainId'].values[0] == 'Condition':
            condition_concept_id = row_for_concept_id['targetConceptId'].values[0]

    row_for_date = table_89_for_date.loc[table_89_for_date['ID_BAZNAT'] == person_id]
    date_start = datetime.strptime(
        row_for_date['HOSP_ENTRY_DATE'].values[0], '%d/%m/%Y %H:%M:%S')
    condition_start_date = date_start.date()
    condition_start_datetime = date_start
    condition_start_datetime_string = date_start.strftime('%Y-%m-%d %H:%M:%S')
    condition_end_date = condition_start_date
    condition_end_datetime = condition_start_datetime

    # search if event_baznat is in visit_occurrence
    visit_occurrence_id = ""
    match_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if not match_visit_occurrence.empty:
        visit_occurrence_id = row["Event_baznat"]

    visit_detail_id = get_visit_detail(
        person_id, condition_start_datetime_string)

    condition_source_value = row[4]
    condition_source_concept_id = ""
    if pd.notna(row[3]):
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[3]]
        if not row_for_concept.empty:
            if row_for_concept["vocabulary_id"].values[0] == "ICD9CM" and row_for_concept["standard_concept"].values[0] == "S":
                condition_source_concept_id = row_for_concept['concept_id'].values[0]

    if condition_source_concept_id and condition_concept_id == 0:
        condition_concept_id = condition_source_concept_id

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("15.csv")

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    match_person = person_table.loc[person_table['person_id'] == person_id]
    if match_person.empty:
        continue

    condition_concept_id = 0
    row_for_concept_id = concept_Yishay_table.loc[concept_Yishay_table['sourceCode'] == row[3]]
    if not row_for_concept_id.empty:
        condition_concept_id = row_for_concept_id['targetConceptId'].values[0]

    row_for_date = table_89_for_date.loc[table_89_for_date['ID_BAZNAT'] == person_id]
    date_start = datetime.strptime(
        row_for_date['HOSP_ENTRY_DATE'].values[0], '%d/%m/%Y %H:%M:%S')
    condition_start_date = date_start.date()
    condition_start_datetime = date_start
    condition_start_datetime_string = date_start.strftime('%Y-%m-%d %H:%M:%S')
    condition_end_date = condition_start_date
    condition_end_datetime = condition_start_datetime

    visit_occurrence_id = ""
    match_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if not match_visit_occurrence.empty:
        visit_occurrence_id = row["Event_baznat"]

    visit_detail_id = get_visit_detail(
        person_id, condition_start_datetime_string)

    condition_source_value = row[4]
    condition_source_concept_id = ""
    if pd.notna(row[3]):
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[3]]
        if not row_for_concept.empty:
            if row_for_concept["vocabulary_id"].values[0] == "ICD9CM" and row_for_concept["standard_concept"].values[0] == "S":
                condition_source_concept_id = row_for_concept['concept_id'].values[0]

    if condition_source_concept_id and condition_concept_id == 0:
        condition_concept_id = condition_source_concept_id

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("28.csv")

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index

    person_id = row[0]
    match_person = person_table.loc[person_table['person_id'] == person_id]
    if match_person.empty:
        continue

    condition_concept_id = 0
    row_for_concept_id = concept_Yishay_table.loc[concept_Yishay_table['sourceCode'] == row[11]]
    if not row_for_concept_id.empty:
        condition_concept_id = row_for_concept_id['targetConceptId'].values[0]

    date_start = datetime.strptime(row[14], '%d/%m/%Y %H:%M:%S')
    condition_start_date = date_start.date()
    condition_start_datetime = date_start
    condition_start_datetime_string = date_start.strftime('%Y-%m-%d %H:%M:%S')
    condition_end_date = condition_start_date
    condition_end_datetime = condition_start_datetime

    visit_occurrence_id = ""
    match_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if not match_visit_occurrence.empty:
        visit_occurrence_id = row["Event_baznat"]

    visit_detail_id = get_visit_detail(
        person_id, condition_start_datetime_string)

    condition_source_value = row[12]
    condition_source_concept_id = ""
    if pd.notna(row[11]):
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[11]]
        if not row_for_concept.empty:
            if row_for_concept["vocabulary_id"].values[0] == "ICD9CM" and row_for_concept["standard_concept"].values[0] == "S":
                
                condition_source_concept_id = row_for_concept['concept_id'].values[0]
    if condition_source_concept_id and condition_concept_id == 0:
        condition_concept_id = condition_source_concept_id

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
    match_person = person_table.loc[person_table['person_id'] == person_id]
    if match_person.empty:
        continue

    condition_concept_id = 0
    row_for_concept_id = concept_Yishay_table.loc[concept_Yishay_table['sourceCode'] == row[10]]
    if not row_for_concept_id.empty:
        condition_concept_id = row_for_concept_id['targetConceptId'].values[0]

    date_start = datetime.strptime(row[14], '%m/%d/%Y %H:%M:%S %p')
    condition_start_date = date_start.date()
    condition_start_datetime = date_start
    condition_start_datetime_string = date_start.strftime('%Y-%m-%d %H:%M:%S')
    condition_end_date = condition_start_date
    condition_end_datetime = condition_start_datetime

    visit_occurrence_id = ""
    match_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if not match_visit_occurrence.empty:
        visit_occurrence_id = row["Event_baznat"]

    visit_detail_id = get_visit_detail(
        person_id, condition_start_datetime_string)

    condition_source_value = row[12]
    condition_source_concept_id = ""
    if pd.notna(row[10]):
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[10]]
        if not row_for_concept.empty:
            if row_for_concept["vocabulary_id"].values[0] == "ICD9CM" and row_for_concept["standard_concept"].values[0] == "S":
                condition_source_concept_id = row_for_concept['concept_id'].values[0]

    if condition_source_concept_id and condition_concept_id == 0:
        condition_concept_id = condition_source_concept_id

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("56.csv")

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    match_person = person_table.loc[person_table['person_id'] == person_id]
    if match_person.empty:
        continue

    condition_concept_id = 0
    row_for_concept_id = concept_Yishay_table.loc[concept_Yishay_table['sourceCode'] == row[10]]
    if not row_for_concept_id.empty:
        condition_concept_id = row_for_concept_id['targetConceptId'].values[0]

    date_start = datetime.strptime(row[14], '%m/%d/%Y %H:%M:%S %p')
    condition_start_date = date_start.date()
    condition_start_datetime = date_start
    condition_start_datetime_string = date_start.strftime('%Y-%m-%d %H:%M:%S')
    condition_end_date = condition_start_date
    condition_end_datetime = condition_start_datetime

    visit_occurrence_id = ""
    match_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if not match_visit_occurrence.empty:
        visit_occurrence_id = row["Event_baznat"]

    visit_detail_id = get_visit_detail(
        person_id, condition_start_datetime_string)

    condition_source_value = row[12]
    condition_source_concept_id = ""
    if pd.notna(row[10]):
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[10]]
        if not row_for_concept.empty:
            if row_for_concept["vocabulary_id"].values[0] == "ICD9CM" and row_for_concept["standard_concept"].values[0] == "S":
                condition_source_concept_id = row_for_concept['concept_id'].values[0]

    if condition_source_concept_id and condition_concept_id == 0:
        condition_concept_id = condition_source_concept_id

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("63.csv")


for index_row, row in source_table.iterrows():

    condition_occurrence_id = index

    person_id = row[0]
    match_person = person_table.loc[person_table['person_id'] == person_id]
    if match_person.empty:
        continue

    condition_concept_id = 0
    row_for_concept_id = concept_Yishay_table.loc[concept_Yishay_table['sourceCode'] == row[11]]
    if not row_for_concept_id.empty:
        condition_concept_id = row_for_concept_id['targetConceptId'].values[0]

    date_start = datetime.strptime(row[14], '%m/%d/%Y %H:%M:%S %p')
    condition_start_date = date_start.date()
    condition_start_datetime = date_start
    condition_start_datetime_string = date_start.strftime('%Y-%m-%d %H:%M:%S')
    condition_end_date = condition_start_date
    condition_end_datetime = condition_start_datetime

    visit_occurrence_id = ""
    match_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if not match_visit_occurrence.empty:
        visit_occurrence_id = row["Event_baznat"]

    visit_detail_id = get_visit_detail(
        person_id, condition_start_datetime_string)

    condition_source_value = row[12]
    condition_source_concept_id = ""
    if pd.notna(row[11]):
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[11]]
        if not row_for_concept.empty:
            if row_for_concept["vocabulary_id"].values[0] == "ICD9CM" and row_for_concept["standard_concept"].values[0] == "S":
                condition_source_concept_id = row_for_concept['concept_id'].values[0]

    if condition_source_concept_id and condition_concept_id == 0:
        condition_concept_id = condition_source_concept_id

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("72.csv")

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    match_person = person_table.loc[person_table['person_id'] == person_id]
    if match_person.empty:
        continue

    condition_concept_id = 0
    row_for_concept_id = concept_Yishay_table.loc[concept_Yishay_table['sourceCode'] == row[10]]
    if not row_for_concept_id.empty:
        condition_concept_id = row_for_concept_id['targetConceptId'].values[0]

    date_start = datetime.strptime(row[14], '%m/%d/%Y %H:%M:%S %p')
    condition_start_date = date_start.date()
    condition_start_datetime = date_start
    condition_start_datetime_string = date_start.strftime('%Y-%m-%d %H:%M:%S')
    condition_end_date = condition_start_date
    condition_end_datetime = condition_start_datetime

    visit_occurrence_id = ""
    match_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if not match_visit_occurrence.empty:
        visit_occurrence_id = row["Event_baznat"]

    visit_detail_id = get_visit_detail(
        person_id, condition_start_datetime_string)

    condition_source_value = row[12]
    condition_source_concept_id = ""

    if pd.notna(row[10]):
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[10]]
        if not row_for_concept.empty:
            if row_for_concept["vocabulary_id"].values[0] == "ICD9CM" and row_for_concept["standard_concept"].values[0] == "S":
                condition_source_concept_id = row_for_concept['concept_id'].values[0]

    if condition_source_concept_id and condition_concept_id == 0:
        condition_concept_id = condition_source_concept_id

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("74.csv")

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    match_person = person_table.loc[person_table['person_id'] == person_id]
    if match_person.empty:
        continue

    condition_concept_id = 0
    row_for_concept_id = concept_Yishay_table.loc[concept_Yishay_table['sourceCode'] == row[11]]
    if not row_for_concept_id.empty:
        condition_concept_id = row_for_concept_id['targetConceptId'].values[0]

    date_start = datetime.strptime(row[15], '%m/%d/%Y %H:%M:%S %p')
    condition_start_date = date_start.date()
    condition_start_datetime = date_start
    condition_start_datetime_string = date_start.strftime('%Y-%m-%d %H:%M:%S')
    condition_end_date = condition_start_date
    condition_end_datetime = condition_start_datetime

    visit_occurrence_id = ""
    match_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if not match_visit_occurrence.empty:
        visit_occurrence_id = row["Event_baznat"]

    visit_detail_id = get_visit_detail(
        person_id, condition_start_datetime_string)

    condition_source_value = row[13]
    condition_source_concept_id = ""

    if pd.notna(row[11]):
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[11]]
        if not row_for_concept.empty:
            if row_for_concept["vocabulary_id"].values[0] == "ICD9CM" and row_for_concept["standard_concept"].values[0] == "S":
                condition_source_concept_id = row_for_concept['concept_id'].values[0]

    if condition_source_concept_id and condition_concept_id == 0:
        condition_concept_id = condition_source_concept_id

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("79.csv")

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index

    person_id = row[0]
    match_person = person_table.loc[person_table['person_id'] == person_id]
    if match_person.empty:
        continue
    condition_concept_id = 0
    row_for_concept_id = concept_Yishay_table.loc[concept_Yishay_table['sourceCode'] == row[11]]
    if not row_for_concept_id.empty:
        condition_concept_id = row_for_concept_id['targetConceptId'].values[0]

    date_start = datetime.strptime(row[15], '%d/%m/%Y %H:%M:%S')
    condition_start_date = date_start.date()
    condition_start_datetime = date_start
    condition_start_datetime_string = date_start.strftime('%Y-%m-%d %H:%M:%S')
    condition_end_date = condition_start_date
    condition_end_datetime = condition_start_datetime

    visit_occurrence_id = ""
    match_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if not match_visit_occurrence.empty:
        visit_occurrence_id = row["Event_baznat"]

    visit_detail_id = get_visit_detail(
        person_id, condition_start_datetime_string)

    condition_source_value = row[13]
    condition_source_concept_id = ""

    if pd.notna(row[11]):
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[11]]
        if not row_for_concept.empty:
            if row_for_concept["vocabulary_id"].values[0] == "ICD9CM" and row_for_concept["standard_concept"].values[0] == "S":
                condition_source_concept_id = row_for_concept['concept_id'].values[0]

    if condition_source_concept_id and condition_concept_id == 0:
        condition_concept_id = condition_source_concept_id

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


source_table = pd.read_csv("80.csv")

for index_row, row in source_table.iterrows():

    condition_occurrence_id = index
    person_id = row[0]
    match_person = person_table.loc[person_table['person_id'] == person_id]
    if match_person.empty:
        continue

    condition_concept_id = 0
    row_for_concept_id = concept_Yishay_table.loc[concept_Yishay_table['sourceCode'] == row[10]]
    if not row_for_concept_id.empty:
        condition_concept_id = row_for_concept_id['targetConceptId'].values[0]

    date_start = datetime.strptime(row[14], '%d/%m/%Y %H:%M:%S')
    condition_start_date = date_start.date()
    condition_start_datetime = date_start
    condition_start_datetime_string = date_start.strftime('%Y-%m-%d %H:%M:%S')
    condition_end_date = condition_start_date
    condition_end_datetime = condition_start_datetime

    visit_occurrence_id = ""
    match_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if not match_visit_occurrence.empty:
        visit_occurrence_id = row["Event_baznat"]

    visit_detail_id = get_visit_detail(
        person_id, condition_start_datetime_string)

    condition_source_value = row[12]
    condition_source_concept_id = ""

    if pd.notna(row[10]):
        row_for_concept = concepts_icd_table.loc[concepts_icd_table['concept_code'] == row[10]]
        if not row_for_concept.empty:
            if row_for_concept["vocabulary_id"].values[0] == "ICD9CM" and row_for_concept["standard_concept"].values[0] == "S":
                condition_source_concept_id = row_for_concept['concept_id'].values[0]

    if condition_source_concept_id and condition_concept_id == 0:
        condition_concept_id = condition_source_concept_id

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id,
                condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id,
                visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value])
    index += 1


df_result = pd.DataFrame(data, columns=['condition_occurrence_id', 'person_id', 'condition_concept_id', 'condition_start_date',
                         'condition_start_datetime', 'condition_end_date', 'condition_end_datetime', 'condition_type_concept_id',
                                        'condition_status_concept_id', 'stop_reason', 'provider_id', 'visit_occurrence_id', 'visit_detail_id',
                                        'condition_source_value', 'condition_source_concept_id', 'condition_status_source_value'])

df_result.to_csv('condition_occurrence.csv', encoding='utf-8', index=False)
