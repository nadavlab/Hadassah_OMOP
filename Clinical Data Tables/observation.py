import pandas as pd

source_table = pd.read_csv("27.csv")
data = []
index = 1
previous_pregnancies = [4049024, 4119100, 4205452, 4244737,
                        4148926, 4330449, 4142640, 4214878, 4069849, 4221287, 4288592]
labor_type_map = {
    'LSTCS': 37312440,
    'Spontaneous vaginal birth': 441641,
    'Vacuum birth': 4189205,
    'Birth forceps': 4114637,
    'Breech birth': 4034145,
    'Mole': 4129710,
    'Cesarean': 193277,
    'Vacuum birth': 4189205
}


for index_row, row in source_table.iterrows():
    # Previous pregnancies
    observation_id = index
    person_id = row[0]
    prev_labor_num = row[2]
    if prev_labor_num > 10:
        observation_concept_id = previous_pregnancies[10]
    else:
        observation_concept_id = previous_pregnancies[prev_labor_num-1]

    observation_date = row[6]
    value_as_number = ''
    value_as_string = row[2]
    value_as_concept_id = ''
    if value_as_string == 'Yes':
        value_as_number = 0
        value_as_concept_id = 4188539  # for yes concept
    else:
        value_as_concept_id = 4188540  # for yes concept
    visit_occurrence_id = row[1]  # event_baznat
    observation_source_value = 'Deafthness'  # smoke
    observation_source_concept_id = 4108577
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, value_as_string, value_as_number, visit_occurrence_id,
                 observation_source_value, observation_source_concept_id])
    index += 1

    # hip joints
    observation_id = index
    person_id = row[0]
    observation_concept_id = 4269302
    observation_date = row[6]
    value_as_number = ''
    value_as_string = row[3]  # yes/no
    value_as_concept_id = ''
    if value_as_string == 'Yes':
        # value_as_number=0
        value_as_concept_id = 4188539  # for yes concept
    else:
        value_as_concept_id = 4188540  # for no concept
    visit_occurrence_id = row[1]  # event_baznat
    observation_source_value = 'Hip joints problem'  # smoke
    observation_source_concept_id = 4269302
    data.append([observation_id, person_id, observation_concept_id, observation_date, value_as_string, value_as_number,
                visit_occurrence_id, observation_source_value, observation_source_concept_id, value_source_value])
    index += 1

    # Inherited diseases
    observation_id = index
    person_id = row[0]
    observation_concept_id = 4168318
    observation_date = row[6]  # 01/01/2022
    value_as_number = ''
    value_as_string = row[4]
    value_as_concept_id = ''
    if value_as_string == 'Yes':
        # value_as_number=0
        value_as_concept_id = 4188539  # for yes concept
    else:
        value_as_concept_id = 4188540  # for no concept
    visit_occurrence_id = row[1]  # event_baznat
    observation_source_value = 'Genetic disorder'  # smoke
    observation_source_concept_id = 4168318
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, value_as_string,
                value_as_number, visit_occurrence_id, observation_source_value, observation_source_concept_id])
    index += 1

    # Family closeness between parents
    observation_id = index
    person_id = row[0]
    observation_concept_id = 4052921
    observation_date = row[6]  # 01/01/2022
    value_as_number = ''
    value_as_string = row[4]
    value_as_concept_id = ''
    if value_as_string == 'Yes':
        # value_as_number=0
        value_as_concept_id = 4188539  # for yes concept
    else:
        value_as_concept_id = 4188540  # for no concept
    visit_occurrence_id = row[1]  # event_baznat
    observation_source_value = 'Blood relatives'  # smoke
    observation_source_concept_id = 4052921
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, value_as_string,
                value_as_number, visit_occurrence_id, observation_source_value, observation_source_concept_id])
    index += 1


source_table = pd.read_csv("37.csv")
data = []
index = 1

for index_row, row in source_table.iterrows():
    # Smocking
    observation_id = index
    person_id = row[0]
    observation_concept_id = 4041306
    observation_date = row[7]
    value_as_number = ''
    value_as_string = row[2]
    value_as_concept_id = ''
    if value_as_string == 'Yes':
        value_as_concept_id = 4188539  # for yes concept
    else:
        value_as_concept_id = 4188540  # for no concept

    visit_occurrence_id = row[1]  # event_baznat
    observation_source_value = 'Smocking'  # smoke
    observation_source_concept_id = 4041306
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, value_as_string,
                value_as_number, visit_occurrence_id, observation_source_value, observation_source_concept_id])
    index += 1
    # Cigarette per day
    observation_id = index
    person_id = row[0]
    observation_concept_id = 4041508
    observation_date = row[7]
    value_as_number = row[3]
    value_as_string = ""
    value_as_concept_id = ''
    visit_occurrence_id = row[1]  # event_baznat
    observation_source_value = 'Cigarettes per day'  # smoke
    observation_source_concept_id = 4041508
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, value_as_string,
                value_as_number, visit_occurrence_id, observation_source_value, observation_source_concept_id])
    index += 1

    # Total time smoked
    observation_id = index
    person_id = row[0]
    observation_concept_id = 4036083
    observation_date = row[7]  # 01/01/2022
    value_as_number = row[4]
    value_as_string = ''
    value_as_concept_id = ''
    visit_occurrence_id = row[1]  # event_baznat
    observation_source_value = 'Smoking time'  # smoke
    observation_source_concept_id = 4036083
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, value_as_string,
                value_as_number, visit_occurrence_id, observation_source_value, observation_source_concept_id])
    index += 1

    # Alcohol intake
    observation_id = index
    person_id = row[0]
    observation_concept_id = 4052351
    observation_date = row[7]  # 01/01/2022
    value_as_number = ''
    value_as_string = row[5]
    value_as_concept_id = ''
    if value_as_string == 'Yes':
        value_as_concept_id = 4188539  # for yes concept
    else:
        value_as_concept_id = 4188540  # for no concept
    visit_occurrence_id = row[1]  # event_baznat
    observation_source_value = 'Alcohol intake'  # smoke
    observation_source_concept_id = 4052351
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, value_as_string,
                value_as_number, visit_occurrence_id, observation_source_value, observation_source_concept_id])
    index += 1

    # Smokes drugs
    observation_id = index
    person_id = row[0]
    observation_concept_id = 3572303
    observation_date = row[7]  # 01/01/2022
    value_as_number = ''
    value_as_string = row[6]
    value_as_concept_id = ''
    if value_as_string == 'Yes':
        value_as_concept_id = 4188539  # for yes concept
    else:
        value_as_concept_id = 4188540  # for no concept
    visit_occurrence_id = row[1]  # event_baznat
    observation_source_value = 'Alcohol intake'  # smoke
    observation_source_concept_id = 3572303
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, value_as_string,
                value_as_number, visit_occurrence_id, observation_source_value, observation_source_concept_id])
    index += 1


    source_table = pd.read_csv("38.csv")
data = []
index = 1

for index_row, row in source_table.iterrows():
    # deafthness
    observation_id = index
    person_id = row[0]
    observation_concept_id = 4108577
    observation_date = row[6]
    value_as_number = ''
    value_as_string = row[2]
    value_as_concept_id = ''
    if value_as_string == 'Yes':
        value_as_number = 0
        value_as_concept_id = 4188539  # for yes concept
    else:
        value_as_concept_id = 4188540  # for yes concept
    visit_occurrence_id = row[1]  # event_baznat
    observation_source_value = 'Deafthness'  # smoke
    observation_source_concept_id = 4108577
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, value_as_string, value_as_number, visit_occurrence_id,
                 observation_source_value, observation_source_concept_id])
    index += 1

    # hip joints
    observation_id = index
    person_id = row[0]
    observation_concept_id = 4269302
    observation_date = row[6]
    value_as_number = ''
    value_as_string = row[3]  # yes/no
    value_as_concept_id = ''
    if value_as_string == 'Yes':
        # value_as_number=0
        value_as_concept_id = 4188539  # for yes concept
    else:
        value_as_concept_id = 4188540  # for no concept
    visit_occurrence_id = row[1]  # event_baznat
    observation_source_value = 'Hip joints problem'  # smoke
    observation_source_concept_id = 4269302
    data.append([observation_id, person_id, observation_concept_id, observation_date, value_as_string, value_as_number,
                visit_occurrence_id, observation_source_value, observation_source_concept_id])
    index += 1

    # Inherited diseases
    observation_id = index
    person_id = row[0]
    observation_concept_id = 4168318
    observation_date = row[6]  # 01/01/2022
    value_as_number = ''
    value_as_string = row[4]
    value_as_concept_id = ''
    if value_as_string == 'Yes':
        # value_as_number=0
        value_as_concept_id = 4188539  # for yes concept
    else:
        value_as_concept_id = 4188540  # for no concept
    visit_occurrence_id = row[1]  # event_baznat
    observation_source_value = 'Genetic disorder'  # smoke
    observation_source_concept_id = 4168318
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, value_as_string,
                value_as_number, visit_occurrence_id, observation_source_value, observation_source_concept_id])
    index += 1

    # Family closeness between parents
    observation_id = index
    person_id = row[0]
    observation_concept_id = 4052921
    observation_date = row[6]  # 01/01/2022
    value_as_number = ''
    value_as_string = row[5]
    value_as_concept_id = ''
    if value_as_string == 'Yes':
        # value_as_number=0
        value_as_concept_id = 4188539  # for yes concept
    else:
        value_as_concept_id = 4188540  # for no concept
    visit_occurrence_id = row[1]  # event_baznat
    observation_source_value = 'Blood relatives'  # smoke
    observation_source_concept_id = 4052921
    # were we can add the comment? some are important
    data.append([observation_id, person_id, observation_concept_id, observation_date, value_as_string,
                value_as_number, visit_occurrence_id, observation_source_value, observation_source_concept_id])
    index += 1











df_result = pd.DataFrame(data, columns=['observation_id', 'person_id', 'observation_concept_id', 'observation_date',
                         'value_as_string', 'value_as_number', 'visit_occurrence_id', 'observation_source_value', 'observation_source_concept_id'])

df_result.to_csv('observation.csv', encoding='utf-8', index=False)


source_table = pd.read_csv("37.csv")
data=[]
index=1

def from_soucre_to_orm_yes_no(index,row_person_id_index,concept_id,row_concept_id,row_concept,row_visit_occurrence,value_name):
    observation_id=index
    person_id=row_person_id_index
    observation_concept_id=concept_id
    observation_date=row_concept_id
    value_as_number=''
    value_as_string=row_concept
    value_as_concept_id=''
    if value_as_string=='Yes':
        value_as_concept_id=4188539#for yes concept
    else:
        value_as_concept_id=4188540#for no concept
    visit_occurrence_id=row_visit_occurrence#event_baznat
    observation_source_value=value_name#smoke
    observation_source_concept_id=concept_id
    #were we can add the comment? some are important
    data.append([observation_id,person_id,observation_concept_id,observation_date,value_as_string,value_as_number,visit_occurrence_id,observation_source_value,observation_source_concept_id])
    index+=1

def from_soucre_to_orm_yes_no(index,row_person_id_index,concept_id,row_concept_id,row_concept,row_visit_occurrence,value_name):
    observation_id=index
    person_id=row[0]
    observation_concept_id=4036083
    observation_date=row[7]#01/01/2022
    value_as_number=row[4]
    value_as_string=''
    value_as_concept_id=''
    visit_occurrence_id=row[1]#event_baznat
    observation_source_value=value_name#smoke
    observation_source_concept_id=4036083
    #were we can add the comment? some are important
    data.append([observation_id,person_id,observation_concept_id,observation_date,value_as_string,value_as_number,visit_occurrence_id,observation_source_value,observation_source_concept_id])
    index+=1


for index_row, row in source_table.iterrows():
    #Smocking
    observation_id=index
    person_id=row[0]
    observation_concept_id=4041306
    observation_date=row[7]
    value_as_number=''
    value_as_string=row[2]
    value_as_concept_id=''
    if value_as_string=='Yes':
        value_as_concept_id=4188539#for yes concept
    else:
        value_as_concept_id=4188540#for no concept

    visit_occurrence_id=row[1]#event_baznat
    observation_source_value='Smocking'#smoke
    observation_source_concept_id=4041306
    #were we can add the comment? some are important
    data.append([observation_id,person_id,observation_concept_id,observation_date,value_as_string,value_as_number,visit_occurrence_id,observation_source_value,observation_source_concept_id])
    index+=1
    #Cigarette per day
    observation_id=index
    person_id=row[0]
    observation_concept_id=4041508
    observation_date=row[7]
    value_as_number=row[3]
    value_as_string=""
    value_as_concept_id=''
    visit_occurrence_id=row[1]#event_baznat
    observation_source_value='Cigarettes per day'#smoke
    observation_source_concept_id=4041508
    #were we can add the comment? some are important
    data.append([observation_id,person_id,observation_concept_id,observation_date,value_as_string,value_as_number,visit_occurrence_id,observation_source_value,observation_source_concept_id])
    index+=1






df_result = pd.DataFrame(data, columns=['observation_id','person_id','observation_concept_id','observation_date','value_as_string','value_as_number','visit_occurrence_id','observation_source_value','observation_source_concept_id'])

df_result.to_csv('observation.csv', encoding='utf-8', index=False)
