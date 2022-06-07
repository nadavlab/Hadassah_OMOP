from asyncio.windows_events import NULL
from curses.ascii import NUL
import pandas as pd
from datetime import datetime
visit_occurrence_table = pd.read_csv("visit_occurrence.csv")


# table 2 - מעבדות ילודים
source_table = pd.read_csv("2.csv")
concept_id_table_2 = pd.read_csv("table2_measurement.csv")
df_concept_id_table_2 = pd.DataFrame(concept_id_table_2, columns=[
                                     'rep_component_name', 'concept'])

data = []
index=1

LABORATORY = 261904005  # טיפול מיוחד בילוד

measurement_time = ''
operator_concept_id=0
unit_concept_id=0
range_low=""
range_high=""
provider_id=""

for index_row, row in source_table.iterrows():

    #check if person exists in person
    
    measurement_id = index
    person_id = row[0]



    date_measurement = datetime.strptime(row[7], '%d/%m/%Y %H:%M:%S')
    measurement_date = date_measurement.date()
    measurement_datetime = date_measurement

    # measurement_datetime = row[7]
    # measurement_date = str(row[7])
    # measurement_date = measurement_date[:10]
    
    measurement_type_concept_id = LABORATORY  # unit

    measurement_concept_id = 0
    # search the concept id in other data frame
    # match_measurement_concept_id = concept_id_table.loc[concept_id_table['rep_component_name'] == measurement_concept_id]
    # index_measurement_concept_id = 0
    # if match_measurement_concept_id.values.shape[0] > 0:
    #      while match_measurement_concept_id.values.shape[0] > index_measurement_concept_id:

    match = df_concept_id_table_2.loc[df_concept_id_table_2['rep_component_name']
                                      == row["rep_component_name"]]
    if match.shape[0] > 0:
        measurement_concept_id = match.values[0][1]
    # else:
    #     measurement_concept_id = ''

    value_as_number = row[8]
    value_as_concept_id = ""

    #TODO
    visit_occurrence_id = ""
    #TODO
    visit_detail_id = ""
    #TODO
    measurement_source_value = row[4]
    measurement_source_concept_id = 0

    #TODO???
    unit_source_value=""
    unit_source_concept_id=""
    value_source_value =""
    measurement_event_id=""
    meas_event_field_concept_id=""

    data.append([measurement_id, person_id, measurement_concept_id, measurement_date, measurement_datetime, measurement_time, 
    measurement_type_concept_id,operator_concept_id,value_as_number, value_as_concept_id,unit_concept_id,range_low,range_high,
    provider_id,visit_occurrence_id,visit_detail_id,measurement_source_value,measurement_source_concept_id,unit_source_value,
    unit_source_concept_id,value_source_value,measurement_event_id,meas_event_field_concept_id])

    index+=1

# df_result = pd.DataFrame(data, columns=['measurement_id', 'person_id', 'measurement_concept_id', 'measurement_date',
#                          'measurement_datetime', 'measurement_type_concept_id', 'value_as_number', 'value_as_concept_id'])

# df_result.to_csv('measurement2.csv', encoding='utf-8', index=False)


# table 8 - פגים מדדים קבלה
source_table = pd.read_csv("8.csv")
# data8 = []

BREATHING = 86290005
PLUGS = 75367002
HR = 78564009
HEAT = 386725007
STURGEON = 103228002
COLOR = 248472001
NEONATAL_INTENSIVE_CARE_UNIT = 405269005

for index_row, row in source_table.iterrows():
    
    measurement_id = index
    person_id = row[0]

    if row[3].__contains__('דופק'):
        measurement_concept_id = HR
    elif row[3].__contains__('חום'):
        measurement_concept_id = HEAT
    elif row[3].__contains__('לחץ דם'):
        measurement_concept_id = PLUGS
    elif row[3].__contains__('נשימות'):
        measurement_concept_id = BREATHING
    elif row[3].__contains__('סטורציה'):
        measurement_concept_id = STURGEON
    else:
        measurement_concept_id = COLOR  # color

    measurement_type_concept_id = NEONATAL_INTENSIVE_CARE_UNIT  # טיפול נמרץ ילודים
    
    measurement_datetime = ""
    match_visit_occurrence = visit_occurrence_table.loc[visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if not match_visit_occurrence.empty:
        measurement_datetime = match_visit_occurrence["visit_start_datetime"]
        measurement_date= measurement_datetime.date()


    value_as_concept_id = ''
    value_as_number = ''
    if measurement_concept_id != COLOR:
        value_as_number = row[4]
    elif row[4].__contains__('ורוד'):
        value_as_concept_id = 304230005
    elif row[4].__contains__('כחול') or row[4].__contains__('כחלחל'):
        value_as_concept_id = 119419001
    elif row[4].__contains__('חיוור'):
        value_as_concept_id = 274643008
    elif row[4].__contains__('סגול'):
        value_as_concept_id = 75246004
    elif row[4].__contains__('אדום'):
        value_as_concept_id = 304228008
    elif row[4].__contains__('צהוב'):
        value_as_concept_id = 267030001
    elif row[4].__contains__('תקין'):
        value_as_concept_id = 304228008
    elif row[4].__contains__('אפור'):
        value_as_concept_id = 304231009
    elif row[4].__contains__('ברדיקרדיה'):
        value_as_concept_id = 413341007
    elif row[4].__contains__('מונשם'):
        value_as_concept_id = 371820004
    elif row[4].__contains__('נינוח'):
        value_as_concept_id = 1148974002
    else:
        value_as_concept_id = None

    data.append([measurement_id, person_id, measurement_concept_id, measurement_date, measurement_datetime, measurement_time, 
    measurement_type_concept_id,operator_concept_id,value_as_number, value_as_concept_id,unit_concept_id,range_low,range_high,
    provider_id,visit_occurrence_id,visit_detail_id,measurement_source_value,measurement_source_concept_id,unit_source_value,
    unit_source_concept_id,value_source_value,measurement_event_id,meas_event_field_concept_id])

    index+=1

# df_result = pd.DataFrame(data8, columns=['measurement_id', 'person_id', 'measurement_concept_id',
#                          'measurement_date', 'measurement_type_concept_id', 'value_as_number', 'value_as_concept_id'])

# df_result.to_csv('measurement8.csv', encoding='utf-8', index=False)


# table 17 - תינוקות מדדים
source_table = pd.read_csv("17.csv")
# data17 = []

NEWBORN_NURSERY_UNIT = 427695007  # מחלקת תינוקות
TEMP = 386725007
WEIGHT = 27113001
HR = 78564009
BILICHECK = 365786009
GLUCOCHECK = 365811003


for index_row, row in source_table.iterrows():
    
    measurement_id = index
    person_id = row[0]

    if row[3].__contains__('דופק'):
        measurement_concept_id = HR
    elif row[3].__contains__('חום'):
        measurement_concept_id = TEMP
    elif row[3].__contains__('משקל'):
        measurement_concept_id = WEIGHT
    elif row[3].__contains__('bilicheck'):
        measurement_concept_id = BILICHECK
    elif row[3].__contains__('glucocheck'):
        measurement_concept_id = GLUCOCHECK
    else:
        measurement_concept_id = None

    measurement_datetime = row[4]
    measurement_date = row[4]
    measurement_date = measurement_date[:10]

    measurement_type_concept_id = NEWBORN_NURSERY_UNIT

    if row[5] == 'low':
        value_as_concept_id = 4083207  # Below reference range
    elif row[5] == 'high':
        value_as_concept_id = 4084765  # Above reference range
    else:
        value_as_number = row[5]



    data.append([measurement_id, person_id, measurement_concept_id, measurement_date, measurement_datetime, measurement_time, 
    measurement_type_concept_id,operator_concept_id,value_as_number, value_as_concept_id,unit_concept_id,range_low,range_high,
    provider_id,visit_occurrence_id,visit_detail_id,measurement_source_value,measurement_source_concept_id,unit_source_value,
    unit_source_concept_id,value_source_value,measurement_event_id,meas_event_field_concept_id])

    index+=1




df_result = pd.DataFrame(data, columns=['measurement_id', 'person_id', 'measurement_concept_id', 'measurement_date', 'measurement_datetime', 'measurement_time', 
    'measurement_type_concept_id','operator_concept_id','value_as_number', 'value_as_concept_id','unit_concept_id','range_low','range_high',
    'provider_id','visit_occurrence_id','visit_detail_id','measurement_source_value','measurement_source_concept_id','unit_source_value',
    'unit_source_concept_id','value_source_value','measurement_event_id','meas_event_field_concept_id'])

df_result.to_csv('measurement.csv', encoding='utf-8', index=False)


# # table 49 - בדיקות גנטיות
# source_table = pd.read_csv("49.csv")
# data49 = []
#
# for index_row, row in source_table.iterrows():
#     measurement_id = index_row
#     person_id = row[0]
#
#
#     # complete from Yishai answer - measurement name
#
#     measurement_concept_id = row[3] # test name
#
#     measurement_date = row[10].date()
#     measurement_datetime = row[10]
#
#     #מיון מיילדתי
#     measurement_type_concept_id = 0 # Unit - complete from Yishai answer,
#
#     if row[4] == 'תקין':
#         value_as_concept_id = 0  # complete
#     elif row[4] == 'לא תקין':
#         value_as_concept_id = 0  # complete
#     else:
#         value_as_concept_id = None
#
#     data49.append([measurement_id, person_id, measurement_concept_id, measurement_date, measurement_type_concept_id, value_as_concept_id])
#
# df_result = pd.DataFrame(data49, columns=['measurement_id', 'person_id', 'measurement_concept_id', 'measurement_date', 'measurement_type_concept_id', 'value_as_concept_id'])
#
# df_result.to_csv('measurement49.csv', encoding='utf-8', index=False)
#
#
#


# df = pd.concat(map(pd.read_csv, [
#                'measurement2.csv', 'measurement8.csv', 'measurement17.csv']), ignore_index=True)
# df.to_csv('measurement.csv', encoding='utf-8', index=False)


# # 'measurement2.csv',
