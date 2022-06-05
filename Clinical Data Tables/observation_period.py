import pandas as pd
import numpy as np


visit_occurrence_table = pd.read_csv("visit_occurrence.csv")
data = []
index = 1

visit_occurrence_table_group = visit_occurrence_table.groupby(['person_id'])
  
# using agg() function on Date column
visit_occurrence_table_group = visit_occurrence_table_group.agg(Minimum_Date=('visit_start_date', np.min), Maximum_Date=('visit_end_date', np.max))
visit_occurrence_table_group.to_csv('visit_occurrence_table_group.csv', encoding='utf-8', index=True)
source_table = pd.read_csv('visit_occurrence_table_group.csv')

for index_row, row in source_table.iterrows():

    observation_period_id = index
    person_id = row['person_id']
        
    observation_period_start_date =row['Minimum_Date']

    observation_period_end_date =row['Maximum_Date']

    period_type_concept_id = 32817  # EHR record
    

    data.append([observation_period_id, person_id, observation_period_start_date,
                observation_period_end_date, period_type_concept_id])
    index += 1


df_result = pd.DataFrame(data, columns=['observation_period_id', 'person_id', 'observation_period_start_date',
                         'observation_period_end_date', 'period_type_concept_id'])

df_result.to_csv('observation_period.csv', encoding='utf-8', index=False)
