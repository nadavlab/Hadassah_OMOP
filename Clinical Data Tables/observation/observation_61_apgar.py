import pandas as pd
from datetime import datetime
import math

source_table = pd.read_csv("61_new.csv")

# 1 minute afgar
one_minute_apgar_heart_rate = 3027152
one_minute_apgar_color = 3026329
one_minute_apgar_muscle_tone = 3013445
one_minute_apgar_score = 3016704
one_minute_apgar_respiratory_effort = 3023275
one_minute_apgar_reflex_irritability = 3027666

# 5 minute afgar
five_minute_apgar_heart_rate = 3026961
five_minute_apgar_color = 3025592
five_minute_apgar_muscle_tone = 3027494
five_minute_apgar_score = 3004221
five_minute_apgar_respiratory_effort = 3024292
five_minute_apgar_reflex_irritability = 3028332

# 10 minute afgar
ten_minute_apgar_heart_rate = 3007503
ten_minute_apgar_color = 3005021
ten_minute_apgar_muscle_tone = 3006474
ten_minute_apgar_score = 3016162
ten_minute_apgar_respiratory_effort = 3025485
ten_minute_apgar_reflex_irritability = 3022387

# others
birth_weight = 4264825
umbilical_cord_normal = 289315001
absent_blood_vessel_in_umbilical_cord = 302945005

visit_detail_table = pd.read_csv("visit_detail.csv")
df_visit_detail_table = pd.DataFrame(visit_detail_table ,
                                     columns=['visit_detail_id' , 'person_id' , 'visit_occurrence_id' ,
                                              'visit_detail_start_datetime' , 'visit_detail_end_datetime'])
#######display#####
display_table = pd.read_csv("display.csv")
df_display_table = pd.DataFrame(display_table ,columns=['display','concept'])

#######delivery way#####
delivery_way_table = pd.read_csv("delivery_way.csv")



data = []
index = 0
EHR_concept_id = 32817

for index_row , row in source_table.iterrows() :
    observation_id = index
    person_id = row["ID_BAZNAT"]
    visit_occurrence_id = row["Event_baznat"]  # event_baznat

    ###date format
    try :
        date = datetime.strptime(row["זמן לידה"] , '%m/%d/%Y %H:%M')
    except :
        date = datetime.strptime(row["זמן לידה"] , '%m/%d/%Y %H:%M:%S %p')
    observation_date = date.date()
    observation_datetime = date
    observation_type_concept_id = EHR_concept_id

    match_visit_detail = df_visit_detail_table.loc[df_visit_detail_table['visit_occurrence_id'] == visit_occurrence_id]
    index_visit_detail = 0
    if match_visit_detail.values.shape[0] > 0 :
        while match_visit_detail.values.shape[0] > index_visit_detail :
            date_start_vd = datetime.strptime(match_visit_detail.values[index_visit_detail][3] , '%Y-%m-%d %H:%M:%S')
            date_end_vd = datetime.strptime(match_visit_detail.values[index_visit_detail][4] , '%Y-%m-%d %H:%M:%S')
            if date_start_vd <= observation_datetime <= date_end_vd :
                visit_detail_id = match_visit_detail.values[index_visit_detail][0]
            index_visit_detail += 1

    else :
        visit_detail_id = ""

    value_as_string = ''
    value_as_concept_id = ''
    qualifier_concept_id = ""
    unit_concept_id = ""
    provider_id = ""
    observation_source_value = ""
    observation_source_concept_id = ""
    unit_source_value = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""
    # --------------------- 1 min Apgar ----------------------#
    if not math.isnan(row['אפגר 1 - סכום ערכים']) :
        observation_concept_id = one_minute_apgar_score
        value_as_number = int(row['אפגר 1 - סכום ערכים'])

        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 1 - דופק']) :
        observation_concept_id = one_minute_apgar_heart_rate
        value_as_number = int(row['אפגר 1 - דופק'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 1 - נשימה']) :
        observation_concept_id = one_minute_apgar_respiratory_effort
        value_as_number = int(row['אפגר 1 - נשימה'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 1 - צבע']) :
        observation_concept_id = one_minute_apgar_color
        value_as_number = int(row['אפגר 1 - צבע'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 1 - טונוס']) :
        observation_concept_id = one_minute_apgar_muscle_tone
        value_as_number = int(row['אפגר 1 - טונוס'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 1 - תגובה']) :
        observation_concept_id = one_minute_apgar_reflex_irritability
        value_as_number = int(row['אפגר 1 - תגובה'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    # --------------------- 5 min Apgar ----------------------#
    if not math.isnan(row['אפגר 5 - סכום ערכים']) :
        observation_concept_id = five_minute_apgar_score
        value_as_number = int(row['אפגר 5 - סכום ערכים'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 5 - דופק']) :
        observation_concept_id = five_minute_apgar_heart_rate
        value_as_number = int(row['אפגר 5 - דופק'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 5 - נשימה']) :
        observation_concept_id = five_minute_apgar_respiratory_effort
        value_as_number = int(row['אפגר 5 - נשימה'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 5 - צבע']) :
        observation_concept_id = five_minute_apgar_color
        value_as_number = int(row['אפגר 5 - צבע'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 5 - טונוס']) :
        observation_concept_id = five_minute_apgar_muscle_tone
        value_as_number = int(row['אפגר 5 - טונוס'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 5 - תגובה']) :
        observation_concept_id = five_minute_apgar_reflex_irritability
        value_as_number = int(row['אפגר 5 - תגובה'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    # --------------------- 10 min Apgar ----------------------#
    if not math.isnan(row['אפגר 10 - סכום ערכים']) :
        observation_concept_id = ten_minute_apgar_score
        value_as_number = int(row['אפגר 10 - סכום ערכים'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 10 - דופק']) :
        observation_concept_id = ten_minute_apgar_heart_rate
        value_as_number = int(row['אפגר 10 - דופק'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 10 - נשימה']) :
        observation_concept_id = ten_minute_apgar_respiratory_effort
        value_as_number = int(row['אפגר 10 - נשימה'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 10 - צבע']) :
        observation_concept_id = ten_minute_apgar_color
        value_as_number = int(row['אפגר 10 - צבע'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 10 - טונוס']) :
        observation_concept_id = ten_minute_apgar_muscle_tone
        value_as_number = int(row['אפגר 10 - טונוס'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    if not math.isnan(row['אפגר 10 - תגובה']) :
        observation_concept_id = ten_minute_apgar_reflex_irritability
        value_as_number = int(row['אפגר 10 - תגובה'])
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    # --------------------- others terms ------------------#
    # weight
    if not math.isnan(row['משקל']) :
        observation_concept_id = birth_weight
        value_as_number = row['משקל']
        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    # umbilical_cord
    if row['חבל טבור עם 3 כלי דם'] :
        value_as_number = ''
        if row['חבל טבור עם 3 כלי דם'] == 'כן' :
            value_as_concept_id = umbilical_cord_normal
        else :
            value_as_concept_id = absent_blood_vessel_in_umbilical_cord

        data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                     observation_type_concept_id ,
                     value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                     provider_id , visit_occurrence_id , visit_detail_id ,
                     observation_source_value , observation_source_concept_id , unit_source_value ,
                     qualifier_source_value , value_source_value , observation_event_id , obs_event_field_concept_id])
        index += 1
        observation_id = index

    # display
    if row['מצג'] :
        value_as_number = ''
        match_display = df_display_table.loc[df_display_table['display'] == row['מצג']]
        if match_display.shape[0]>0:
            value_as_concept_id = match_display.values[0][1]
            data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                         observation_type_concept_id ,
                         value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id ,
                         unit_concept_id ,
                         provider_id , visit_occurrence_id , visit_detail_id ,
                         observation_source_value , observation_source_concept_id , unit_source_value ,
                         qualifier_source_value , value_source_value , observation_event_id ,
                         obs_event_field_concept_id])
            index += 1
            observation_id = index

    # df_delivery_table
    if row['אופן הלידה'] :
        value_as_number = ''
        match_delivery = delivery_way_table.loc[delivery_way_table['delivery_way'] == row['אופן הלידה']]
        if match_delivery.shape[0]>0:
            value_as_concept_id = match_delivery.values[0][2]
            data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                         observation_type_concept_id ,
                         value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id ,
                         unit_concept_id ,
                         provider_id , visit_occurrence_id , visit_detail_id ,
                         observation_source_value , observation_source_concept_id , unit_source_value ,
                         qualifier_source_value , value_source_value , observation_event_id ,
                         obs_event_field_concept_id])
            index += 1
            observation_id = index



df_result = pd.DataFrame(data ,
                         columns=["observation_id" , "person_id" , "observation_concept_id" , "observation_date" ,
                                  "observation_datetime" , "observation_type_concept_id" ,
                                  "value_as_number" , "value_as_string" , "value_as_concept_id" ,
                                  "qualifier_concept_id" , "unit_concept_id" , "provider_id" , "visit_occurrence_id" ,
                                  "visit_detail_id" ,
                                  "observation_source_value" , "observation_source_concept_id" , "unit_source_value" ,
                                  "qualifier_source_value" , "value_source_value" , "observation_event_id" ,
                                  "obs_event_field_concept_id"])

df_result.to_csv('observation_death.csv' , encoding='utf-8' , index=False)
