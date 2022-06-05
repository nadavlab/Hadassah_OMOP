# Death

import pandas as pd
from datetime import datetime
from enum import Enum

#### 61 table ####
source_table = pd.read_csv("61.csv")

### person ####
df_person = pd.read_csv("person.csv")

def is_exsit_person_id(id_baznat):
    match_person = df_person.loc[df_person['person_id'] == id_baznat]
    if match_person.shape[0] > 0 :
        return True
    else:
        return False

class DeathType(Enum):
    INTRAUTERINE_FETAL_DEATH = 4129846
    FETAL_DEATH_DUE_TO_TERMINATION_OF_PREGNANCY = 436228
    INTRAPARTUM_FETAL_DEATH = 4028785
    EARLY_NEONATAL_DEATH = 4307303
    SELECTIVE_FETECIDE = 4045947
    INTRAUTERINE_DEATH_OF_ONE_TWIN = 4028786

EHR_CONCEPT_ID = 32817



data=[]

for index_row, row in source_table.iterrows():
    if is_exsit_person_id(row['ID_BAZNAT']):
        person_id=row['ID_BAZNAT']
    else:
        continue

    try:
        date = datetime.strptime(row["זמן לידה"] , '%m/%d/%Y %H:%M')
    except:
        date = datetime.strptime(row["זמן לידה"] , '%m/%d/%Y %H:%M:%S %p')

    death_date = date.date()
    death_datetime = date
    death_type_concept_id = EHR_CONCEPT_ID
    if row['סוג מוות'] == 'Intrauterine fetal death':
        cause_concept_id = DeathType.INTRAUTERINE_FETAL_DEATH.value
    elif row['סוג מוות'] == 'Fetal death due to termination of pregnancy':
        cause_concept_id = DeathType.FETAL_DEATH_DUE_TO_TERMINATION_OF_PREGNANCY.value
    elif row['סוג מוות'] == 'Intrapartum Fetal Death':
        cause_concept_id = DeathType.INTRAPARTUM_FETAL_DEATH.value
    elif row['סוג מוות'] == 'Early neonatal death':
        cause_concept_id = DeathType.EARLY_NEONATAL_DEATH.value
    elif row['סוג מוות'] == 'Selective Fetecide':
        cause_concept_id = DeathType.SELECTIVE_FETECIDE.value
    else:
        cause_concept_id = DeathType.INTRAUTERINE_DEATH_OF_ONE_TWIN.value

    cause_source_value = ''
    cause_source_concept_id = ''

    data.append([person_id,death_date,death_datetime,death_type_concept_id,cause_concept_id,cause_source_value,cause_source_concept_id])

df_result = pd.DataFrame(data, columns=["person_id","death_date","death_datetime","death_type_concept_id","cause_concept_id","cause_source_value","cause_source_concept_id"])
df_result.to_csv('death.csv', encoding='utf-8', index=False)
