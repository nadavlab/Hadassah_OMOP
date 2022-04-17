import pandas as pd

# moms details
source_table = pd.read_csv("89_filter.csv")
data = []

for index_row, row in source_table.iterrows():
        person_id = row[0]
        if row[2] == 'female':
            gender_concept_id = 8532  # female
        else:
            gender_concept_id = 8507  # male

        year_of_birth = row[1]
        month_of_birth = None
        day_of_birth = None
        race_concept_id = 0
        ethnicity_concept_id = 0

        data.append([person_id, gender_concept_id, year_of_birth, month_of_birth, day_of_birth, race_concept_id,
                     ethnicity_concept_id])

df_result = pd.DataFrame(data, columns=['person_id', 'gender_concept_id', 'year_of_birth', 'month_of_birth',
                                'day_of_birth', 'race_concept_id', 'ethnicity_concept_id'])

df_result.to_csv('person1.csv', encoding='utf-8', index=False)

# babies details
source_table = pd.read_csv("61_filter.csv")
data2 = []

for index_row, row in source_table.iterrows():
        person_id = row[0]
        if row[4] == 'female':
            gender_concept_id = 8532  # female
        else:
            gender_concept_id = 8507  # male

        year_of_birth = row[1]
        month_of_birth = row[2]
        day_of_birth = row[3]
        race_concept_id = 0
        ethnicity_concept_id = 0

        data2.append([person_id, gender_concept_id, year_of_birth, month_of_birth, day_of_birth, race_concept_id,
                     ethnicity_concept_id])
df_result = pd.DataFrame(data2, columns=['person_id', 'gender_concept_id', 'year_of_birth', 'month_of_birth', 'day_of_birth', 'race_concept_id', 'ethnicity_concept_id'])

df_result.to_csv('person2.csv', encoding='utf-8', index=False)


df = pd.concat(map(pd.read_csv, ['person1.csv', 'person2.csv']), ignore_index=True)
df.to_csv('person.csv', encoding='utf-8', index=False)
