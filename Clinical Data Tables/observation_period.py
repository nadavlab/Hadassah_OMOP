import pandas as pd
from datetime import datetime

source_table = pd.read_csv("89.csv")
data = []
index = 1

for index_row, row in source_table.iterrows():

    observation_period_id = index
    person_id = row[0]

    date_start = ""
    if pd.notna(row[2]):
        date_start = datetime.strptime(
            row['HOSP_ENTRY_DATE'].values[0], '%d/%m/%Y %H:%M:%S')
    elif pd.notna(row[6]):
        date_start = datetime.strptime(
            row['Cham_Hosp_Entry_Date'].values[0], '%d/%m/%Y %H:%M:%S')

    observation_period_start_date = date_start.date()

    date_end = ""
    if pd.notna(row[3]):
        date_end = datetime.strptime(
            row['HOSP_EXIT_DATE'].values[0], '%d/%m/%Y %H:%M:%S')
    elif pd.notna(row[7]):
        date_end = datetime.strptime(
            row['Cham_Hosp_Exit_Date'].values[0], '%d/%m/%Y %H:%M:%S')

    observation_period_end_date = date_end.date()

    period_type_concept_id = 32817  # EHR record

    data.append([observation_period_id, person_id, observation_period_start_date,
                observation_period_end_date, period_type_concept_id])
    index += 1


df_result = pd.DataFrame(data, columns=['observation_period_id', 'person_id', 'observation_period_start_date',
                         'observation_period_end_date', 'period_type_concept_id'])

df_result.to_csv('condition_occurrence.csv', encoding='utf-8', index=False)
