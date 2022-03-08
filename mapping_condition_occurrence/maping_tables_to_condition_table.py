import pandas as pd

# For deleting ICD9

# CONCEPT_table = pd.read_csv("CONCEPT_ICD9.csv", sep='\t')
# # df = pandas.read_csv(filepath, sep='delimiter', header=None)

# #CONCEPT_table.to_csv('new_table.csv', encoding='utf-8', index=False)

# values_table = pd.read_csv("values to condition table eng only.csv")

# new_table = []
# new_table = values_table[~values_table["Code"].isin(
#     CONCEPT_table["concept_code"])]

# new_table.to_csv('new_table1.csv', encoding='utf-8', index=False)
# for index_row, row in CONCEPT_table.iterrows():
#     print(row[0])
#     print(row[1])
#     if row[0] in CONCEPT_table and row[1] in CONCEPT_table:
#         continue
#     new_table.append(row)

# new_table = pd.DataFrame(new_table)

# new_table.to_csv('new_table.csv', encoding='utf-8', index=False)


source_table = pd.read_csv("table6.csv")
table_89_for_date = pd.read_csv("table89.csv")
data = []
index = 1

for index_row, row in source_table.iterrows():

    person_id = row[0]  # ID_BAZNAT
    condition_occurrence_id = index
    condition_concept_id = 0  # TODO concept_id

    # for the date record we use table 89
    row_for_date = table_89_for_date.loc[table_89_for_date['ID_BAZNAT'] == person_id]
    condition_start_date = row_for_date['HOSP_ENTRY_DATE'].values[0]
    condition_type_concept_id = 32817  # EHR record

    visit_occurrence_id = row[1]  # event_baznat
    condition_source_value = row[4]  # condition value

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_type_concept_id, visit_occurrence_id, condition_source_value])
    index += 1


source_table = pd.read_csv("table15.csv")
table_89_for_date = pd.read_csv("table89.csv")

for index_row, row in source_table.iterrows():

    person_id = row[0]
    condition_occurrence_id = index
    condition_concept_id = 0  # TODO concept_id

    row_for_date = table_89_for_date.loc[table_89_for_date['ID_BAZNAT'] == person_id]
    condition_start_date = row_for_date['HOSP_ENTRY_DATE'].values[0]
    condition_type_concept_id = 32817  # EHR record

    visit_occurrence_id = row[1]  # event_baznat
    condition_source_value = row[4]

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_type_concept_id, visit_occurrence_id, condition_source_value])
    index += 1

# table 31 - family conditions need to mapped to OBSERVATION table


source_table = pd.read_csv("table40.csv")

for index_row, row in source_table.iterrows():

    person_id = row[0]
    condition_occurrence_id = index
    condition_concept_id = 0  # TODO concept_id

    condition_start_date = row[14]
    condition_type_concept_id = 32817  # EHR record

    visit_occurrence_id = row[1]  # event_baznat
    condition_source_value = row[12]

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_type_concept_id, visit_occurrence_id, condition_source_value])
    index += 1


source_table = pd.read_csv("table56.csv")

for index_row, row in source_table.iterrows():

    person_id = row[0]
    condition_occurrence_id = index
    condition_concept_id = 0  # TODO concept_id

    condition_start_date = row[14]
    condition_type_concept_id = 32817  # EHR record

    visit_occurrence_id = row[1]  # event_baznat
    condition_source_value = row[12]

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_type_concept_id, visit_occurrence_id, condition_source_value])
    index += 1


source_table = pd.read_csv("table63.csv")


for index_row, row in source_table.iterrows():

    person_id = row[0]
    condition_occurrence_id = index
    condition_concept_id = 0  # TODO concept_id

    condition_start_date = row[14]
    condition_type_concept_id = 32817  # EHR record

    visit_occurrence_id = row[1]  # event_baznat
    condition_source_value = row[12]

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_type_concept_id, visit_occurrence_id, condition_source_value])
    index += 1


source_table = pd.read_csv("table72.csv")

for index_row, row in source_table.iterrows():

    person_id = row[0]
    condition_occurrence_id = index
    condition_concept_id = 0  # TODO concept_id

    condition_start_date = row[14]
    condition_type_concept_id = 32817  # EHR record

    visit_occurrence_id = row[1]  # event_baznat
    condition_source_value = row[12]

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_type_concept_id, visit_occurrence_id, condition_source_value])
    index += 1


source_table = pd.read_csv("table74.csv")

for index_row, row in source_table.iterrows():

    person_id = row[0]
    condition_occurrence_id = index
    condition_concept_id = 0  # TODO concept_id

    condition_start_date = row[15]
    condition_type_concept_id = 32817  # EHR record

    visit_occurrence_id = row[1]  # event_baznat
    condition_source_value = row[13]

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_type_concept_id, visit_occurrence_id, condition_source_value])
    index += 1


source_table = pd.read_csv("table79.csv")

for index_row, row in source_table.iterrows():

    person_id = row[0]
    condition_occurrence_id = index
    condition_concept_id = 0  # TODO concept_id

    condition_start_date = row[15]
    condition_type_concept_id = 32817  # EHR record

    visit_occurrence_id = row[1]  # event_baznat
    condition_source_value = row[13]

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_type_concept_id, visit_occurrence_id, condition_source_value])
    index += 1


source_table = pd.read_csv("table80.csv")

for index_row, row in source_table.iterrows():

    person_id = row[0]
    condition_occurrence_id = index
    condition_concept_id = 0  # TODO concept_id

    condition_start_date = row[14]
    condition_type_concept_id = 32817  # EHR record

    visit_occurrence_id = row[1]  # event_baznat
    condition_source_value = row[12]

    data.append([condition_occurrence_id, person_id, condition_concept_id, condition_start_date,
                condition_type_concept_id, visit_occurrence_id, condition_source_value])
    index += 1


df_result = pd.DataFrame(data, columns=['condition_occurrence_id', 'person_id', 'condition_concept_id', 'condition_start_date',
                         'condition_type_concept_id', 'visit_occurrence_id', 'condition_source_value'])

df_result.to_csv('condition_occurence_table.csv',
                 encoding='utf-8', index=False)
