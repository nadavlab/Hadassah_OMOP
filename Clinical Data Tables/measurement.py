# from asyncio.windows_events import NULL
# from curses.ascii import NULL
import string
import pandas as pd
from datetime import datetime

# person :
person_table = pd.read_csv("person.csv")

# visit detail :
visit_detail_table = pd.read_csv("visit_detail.csv")
# df_visit_detail_table = pd.DataFrame(visit_detail_table ,columns=['visit_detail_id', 'person_id','visit_occurrence_id', 'visit_detail_start_datetime', 'visit_detail_end_datetime'])

# visit occurrence :
visit_occurrence_table = pd.read_csv("visit_occurrence.csv")
# df_visit_occurrence_table= pd.DataFrame(visit_occurrence_table ,columns=['visit_occurrence_id','visit_start_datetime'])


# table 2 - מעבדות ילודים
source_table = pd.read_csv("2.csv")
concept_id_table_2 = pd.read_csv("table2_measurement_conceptID.csv")
# df_concept_id_table_2 = pd.DataFrame(concept_id_table_2, columns=[
                                    #  'rep_component_name', 'concept'])

data = []
index = 1

LABORATORY = 4135110  # טיפול מיוחד בילוד

measurement_time = ''
operator_concept_id = 0
unit_concept_id = 0
range_low = ""
range_high = ""
provider_id = ""

for index_row, row in source_table.iterrows():

    #check if person exists in person
    # try:
    try:
        person_id = int(row[0])
        match_person = person_table.loc[person_table['person_id'] == person_id]
        if match_person.empty:
            continue
    except:
        continue

    measurement_id = index
    visit_occurrence_id = int(row[1])  # Event baznat
    match_visit_occurrence = visit_occurrence_table.loc[visit_occurrence_table['visit_occurrence_id'] ==
                                                        visit_occurrence_id]
    if match_visit_occurrence.empty:
        continue
        # visit_occurrence_id = ""

    if row[7] == "" or pd.isna(row[7]):
        # row_for_date = visit_occurrence_table.loc[visit_occurrence_table['visit_occurrence_id'] == visit_occurrence_id]

        measurement_datetime =datetime.strptime(match_visit_occurrence['visit_start_datetime'].values[0], '%Y-%m-%d %H:%M:%S')
        # date_start = datetime.strptime(row_for_date['visit_occurrence_id'].values[0], '%d/%m/%Y %H:%M:%S')
        measurement_date = measurement_datetime.date()
        # condition_start_date = date_start.date()


        # if visit_occurrence_table['visit_occurrence_id'] == visit_occurrence_id:
        #     measurement_date = visit_occurrence_table['visit_start_date'].value
        # else:
        #     measurement_date= datetime.datetime(1999, 1, 1)

    else:

        try:
            measurement_datetime = datetime.strptime(row[7], '%d/%m/%Y %H:%M')
        #     measurement_datetime = datetime.strptime(row[7], '%d/%m/%Y %H:%M:%S')
        except:
            measurement_datetime = datetime.strptime(row[8], '%d/%m/%Y %H:%M')

        # date_start = datetime.strptime(row[14], '%m/%d/%Y %H:%M:%S %p')
        # condition_start_date = date_start.date()
        measurement_date = measurement_datetime.date()

        # str_date = str(row[7])
        # try:
        #     date_m = datetime.strptime(str_date, '%d/%m/%Y %H:%M:%S')
        # except:
        #     date_m = datetime.strptime(str_date, '%d/%m/%Y %H:%M')


    # measurement_datetime = date_m

    measurement_type_concept_id = LABORATORY  # unit , where the Measurement record was recorded

    # name of measurement by concept id
    measurement_concept_id = 0
    match = concept_id_table_2.loc[concept_id_table_2['rep_component_name']
                                      == row['rep_component_name']]
    if not match.empty:
        try:
            measurement_concept_id = int(match['id'].values[0])
        except:
            measurement_concept_id = 0
    try:
        value_as_number = float(row[8])
    except:
        value_as_number = ""

    value_as_concept_id = 0

    measurement_source_value = row[4]
    measurement_source_concept_id = 0

    unit_source_value = row[2]
    value_source_value = row[8]

    measurement_event_id = ''
    meas_event_field_concept_id = ''
    unit_source_concept_id = ''

    match_visit_detail = visit_detail_table.loc[
        visit_detail_table['visit_occurrence_id'] == visit_occurrence_id]
    if not match_visit_occurrence.empty:
        try:
            visit_detail_id = match_visit_detail["visit_detail_id"].values[0]
        except:
            visit_detail_id = ''

    data.append([measurement_id, person_id, measurement_concept_id, measurement_date, measurement_datetime,
                 measurement_time, measurement_type_concept_id,operator_concept_id,value_as_number,
                 value_as_concept_id,unit_concept_id,range_low,range_high ,provider_id,visit_occurrence_id,
                 visit_detail_id,measurement_source_value,measurement_source_concept_id,unit_source_value,
                 unit_source_concept_id,value_source_value,measurement_event_id,meas_event_field_concept_id])

    index += 1



# table 8 - פגים מדדים קבלה
source_table = pd.read_csv("8.csv")
# data8 = []

BREATHING = 4313591
PLUGS = 4326744
HR = 4301868
HEAT = 4302666
STURGEON = 4011919
COLOR = 4086675
NEONATAL_INTENSIVE_CARE_UNIT = 4231410

for index_row, row in source_table.iterrows():

    # check if person exists in person
    person_id = row[0]
    match_person = person_table.loc[person_table['person_id'] == person_id]
    if match_person.empty:
        continue

    measurement_id = index

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

    visit_occurrence_id = 0
    measurement_datetime = 0
    measurement_date = 0

    match_visit_occurrence = visit_occurrence_table.loc[visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if match_visit_occurrence.shape[0] > 0 :
        visit_occurrence_id = row["Event_baznat"]
        date_m = match_visit_occurrence['visit_start_datetime']
        date_m = date_m.values[0]
        measurement_datetime = datetime.strptime(date_m, '%Y-%m-%d %H:%M:%S')
        measurement_date = measurement_datetime.date()
    else:
        visit_occurrence_id = ''

    value_as_concept_id = ''
    value_as_number = ''

    if measurement_concept_id != COLOR:
        try:
            if row[4].__contains__('.'):
                temp = row[4].split('.')
                new_num = float(temp[0])
                new_num += float(temp[1])/100
                value_as_number = new_num
            elif row[4].__contains__('/'):
                temp = row[4].split('/')
                new_num = float(temp[0])/float(temp[1])
                value_as_number = new_num
            else:
                value_as_number = float(row[4])
        except:
            value_as_number = 0
    elif row[4].__contains__('ורוד') or row[4].__contains__('ורדרד'):
        value_as_concept_id = 4127287
    elif row[4].__contains__('כחול') or row[4].__contains__('כחלחל'):
        value_as_concept_id = 4000640
    elif row[4].__contains__('חיוור'):
        value_as_concept_id = 4164646
    elif row[4].__contains__('סגול'):
        value_as_concept_id = 4328492
    elif row[4].__contains__('אדום'):
        value_as_concept_id = 4126316
    elif row[4].__contains__('צהוב') or row[4].__contains__('צהבהב'):
        value_as_concept_id = 4144410
    elif row[4].__contains__('תקין'):
        value_as_concept_id = 4126316
    elif row[4].__contains__('אפור') or row[4].__contains__('אפרפר'):
        value_as_concept_id = 4127288
    elif row[4].__contains__('ברדיקרדיה'):
        value_as_concept_id = 443522
    elif row[4].__contains__('מונשם'):
        value_as_concept_id = 4161461
    else:
        value_as_concept_id = None

    measurement_source_value = row[4]
    measurement_source_concept_id = 0

    unit_source_value = row[2]
    value_source_value = row[3]

    measurement_event_id = ""
    meas_event_field_concept_id = ""
    unit_source_concept_id = ""

    match_visit_detail = visit_detail_table.loc[
        visit_detail_table['visit_occurrence_id'] == visit_occurrence_id]
    visit_detail_id=''
    if not match_visit_detail.empty:
        try:
            visit_detail_id = match_visit_detail["visit_detail_id"].values[0]
        except:
            visit_detail_id=''

    data.append([measurement_id, person_id, measurement_concept_id, measurement_date, measurement_datetime,
                 measurement_time, measurement_type_concept_id,operator_concept_id,value_as_number,
                 value_as_concept_id,unit_concept_id,range_low,range_high,provider_id,visit_occurrence_id,
                 visit_detail_id,measurement_source_value,measurement_source_concept_id,unit_source_value,
                 unit_source_concept_id,value_source_value,measurement_event_id,meas_event_field_concept_id])

    index += 1


# table 17 - תינוקות מדדים
source_table = pd.read_csv("17.csv")
# data17 = []

NEWBORN_NURSERY_UNIT = 4160140  # מחלקת תינוקות
TEMP = 4302666
WEIGHT = 4099154
HR = 4301868
BILICHECK = 4269845
GLUCOCHECK = 4275336


for index_row, row in source_table.iterrows():
    # check if person exists in person
    person_id = row[0]
    match_person = person_table.loc[person_table['person_id'] == person_id]
    if match_person.empty:
        continue

    measurement_id = index

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
        measurement_concept_id = 0


    measurement_datetime = 0
    measurement_date = 0

    match_visit_occurrence = visit_occurrence_table.loc[
        visit_occurrence_table['visit_occurrence_id'] == row["Event_baznat"]]
    if match_visit_occurrence.shape[0] > 0:
        visit_occurrence_id = row["Event_baznat"]
    else:
        visit_occurrence_id = ''

    match_visit_detail = visit_detail_table.loc[
        visit_detail_table['visit_occurrence_id'] == visit_occurrence_id]
    visit_detail_id=''    
    if not match_visit_detail.empty:
        try:
            visit_detail_id = match_visit_detail["visit_detail_id"].values[0]
        except:
            visit_detail_id=''  

    try:
        str_date = str(row[4])
        date_m = datetime.strptime(str_date, '%d/%m/%Y %H:%M:%S')
        measurement_date = date_m.date()
        measurement_datetime = date_m
    except:
        date_m = datetime.strptime(str_date, '%d/%m/%Y %H:%M')
        measurement_date = date_m.date()
        measurement_datetime = date_m

    measurement_type_concept_id = NEWBORN_NURSERY_UNIT

    value_as_concept_id = ''
    value_as_number = ''

    if row[5] == 'low' or row[5] == 'LOW':
        value_as_concept_id = 4083207  # Below reference range
    elif row[5] == 'high' or row[5] == 'HIGH':
        value_as_concept_id = 4084765  # Above reference range
    else:
        value_as_number = float(row[5])

    measurement_source_value = row[3]
    measurement_source_concept_id = 0

    unit_source_value = row[2]
    value_source_value = row[5]

    measurement_event_id = ""
    meas_event_field_concept_id = ""
    unit_source_concept_id = ""

    data.append([measurement_id, person_id, measurement_concept_id, measurement_date, measurement_datetime,
                 measurement_time,measurement_type_concept_id,operator_concept_id,value_as_number,
                 value_as_concept_id,unit_concept_id,range_low,range_high,provider_id,visit_occurrence_id,
                 visit_detail_id,measurement_source_value,measurement_source_concept_id,unit_source_value,
                 unit_source_concept_id,value_source_value,measurement_event_id,meas_event_field_concept_id])

    index+=1




df_result = pd.DataFrame(data, columns=['measurement_id', 'person_id', 'measurement_concept_id',
                                        'measurement_date', 'measurement_datetime', 'measurement_time',
                                        'measurement_type_concept_id','operator_concept_id','value_as_number',
                                        'value_as_concept_id','unit_concept_id','range_low','range_high',
                                        'provider_id','visit_occurrence_id','visit_detail_id',
                                        'measurement_source_value','measurement_source_concept_id',
                                        'unit_source_value','unit_source_concept_id','value_source_value',
                                        'measurement_event_id','meas_event_field_concept_id'])

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
#     data.append([measurement_id, person_id, measurement_concept_id, measurement_date, measurement_type_concept_id, value_as_concept_id])
#
