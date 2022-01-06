import pandas as pd


source_table = pd.read_csv("37.csv")
data=[]
index=1

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

    #Total time smoked
    observation_id=index
    person_id=row[0]
    observation_concept_id=4036083
    observation_date=row[7]#01/01/2022
    value_as_number=row[4]
    value_as_string=''
    value_as_concept_id=''
    visit_occurrence_id=row[1]#event_baznat
    observation_source_value='Smoking time'#smoke
    observation_source_concept_id=4036083
    #were we can add the comment? some are important
    data.append([observation_id,person_id,observation_concept_id,observation_date,value_as_string,value_as_number,visit_occurrence_id,observation_source_value,observation_source_concept_id])
    index+=1

    #Alcohol intake
    observation_id=index
    person_id=row[0]
    observation_concept_id=4052351
    observation_date=row[7]#01/01/2022
    value_as_number=''
    value_as_string=row[5]
    value_as_concept_id=''
    if value_as_string=='Yes':
        value_as_concept_id=4188539#for yes concept
    else:
        value_as_concept_id=4188540#for no concept
    visit_occurrence_id=row[1]#event_baznat
    observation_source_value='Alcohol intake'#smoke
    observation_source_concept_id=4052351
    #were we can add the comment? some are important
    data.append([observation_id,person_id,observation_concept_id,observation_date,value_as_string,value_as_number,visit_occurrence_id,observation_source_value,observation_source_concept_id])
    index+=1


    #Smokes drugs
    observation_id=index
    person_id=row[0]
    observation_concept_id=3572303
    observation_date=row[7]#01/01/2022
    value_as_number=''
    value_as_string=row[6]
    value_as_concept_id=''
    if value_as_string=='Yes':
        value_as_concept_id=4188539#for yes concept
    else:
        value_as_concept_id=4188540#for no concept
    visit_occurrence_id=row[1]#event_baznat
    observation_source_value='Alcohol intake'#smoke
    observation_source_concept_id=3572303
    #were we can add the comment? some are important
    data.append([observation_id,person_id,observation_concept_id,observation_date,value_as_string,value_as_number,visit_occurrence_id,observation_source_value,observation_source_concept_id])
    index+=1

df_result = pd.DataFrame(data, columns=['observation_id','person_id','observation_concept_id','observation_date','value_as_string','value_as_number','visit_occurrence_id','observation_source_value','observation_source_concept_id'])

df_result.to_csv('observation.csv', encoding='utf-8', index=False)
