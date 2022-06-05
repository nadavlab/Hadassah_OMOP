import pandas as pd
from datetime import datetime
import math
from enum import Enum
from num2words import num2words
#
# Tables 24,25,26,29,52,59,61
#

### visit detail : ####
visit_detail_table = pd.read_csv("visit_detail.csv")
df_visit_detail_table = pd.DataFrame(visit_detail_table ,
                                     columns=['visit_detail_id' , 'person_id' , 'visit_occurrence_id' ,
                                              'visit_detail_start_datetime' , 'visit_detail_end_datetime'])

### visit occurrence : ####
visit_occurrence_table = pd.read_csv("visit_occurrence.csv")
df_visit_occurrence_table = pd.DataFrame(visit_occurrence_table , columns=['visit_occurrence_id'])

### person ####
df_person = pd.read_csv("person.csv")

data = []
index = 0
EHR_CONCEPT_ID = 32817
MATERNITY_CLINIC = 4190427


def add_to_data ( index , person_id , observation_concept_id , observation_date , observation_datetime ,
                  value_as_number ,
                  value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id , unit_concept_id ) :
    observation_id = index
    observation_type_concept_id = EHR_CONCEPT_ID
    qualifier_concept_id = ""
    unit_source_value = ""
    provider_id = ""
    observation_source_value = ""
    observation_source_concept_id = ""
    qualifier_source_value = ""
    value_source_value = ""
    observation_event_id = ""
    obs_event_field_concept_id = ""
    data.append([observation_id , person_id , observation_concept_id , observation_date , observation_datetime ,
                 observation_type_concept_id ,
                 value_as_number , value_as_string , value_as_concept_id , qualifier_concept_id , unit_concept_id ,
                 provider_id , visit_occurrence_id , visit_detail_id ,
                 observation_source_value , observation_source_concept_id , unit_source_value , qualifier_source_value ,
                 value_source_value , observation_event_id , obs_event_field_concept_id])


def is_exsit_visit_occurrence_id ( event_baznat ) :
    match_visit_occurrence = df_visit_occurrence_table.loc[
        df_visit_occurrence_table['visit_occurrence_id'] == event_baznat]
    if match_visit_occurrence.shape[0] > 0 :
        return row["Event_baznat"]
    else :
        return ''


def is_exsit_visit_detail_id ( visit_occurrence_id ) :
    match_visit_detail = df_visit_detail_table.loc[df_visit_detail_table['visit_occurrence_id'] == visit_occurrence_id]
    index_visit_detail = 0
    if match_visit_detail.values.shape[0] > 0 :
        while match_visit_detail.values.shape[0] > index_visit_detail :
            date_start_vd = datetime.strptime(match_visit_detail.values[index_visit_detail][3] , '%Y-%m-%d %H:%M:%S')
            date_end_vd = datetime.strptime(match_visit_detail.values[index_visit_detail][4] , '%Y-%m-%d %H:%M:%S')
            if date_start_vd <= observation_datetime <= date_end_vd :
                return match_visit_detail.values[index_visit_detail][0]
            index_visit_detail += 1
    else :
        return ''

def is_exsit_person_id(id_baznat):
    match_person = df_person.loc[df_person['person_id'] == id_baznat]
    if match_person.shape[0] > 0 :
        return True
    else:
        return False


#### 24 table ###
source_table = pd.read_csv("24.csv")
terms_table = pd.read_csv("24_Usagi.csv")
df_terms_table = pd.DataFrame(terms_table , columns=['sourceCode' , 'SNOMED'])

for index_row , row in source_table.iterrows() :
    if is_exsit_person_id(row['ID_BAZNAT']) == True:
        person_id = row["ID_BAZNAT"]
    else:
        continue

    try :
        date = datetime.strptime(row["Record_Date"] , '%d/%m/%Y %H:%M:%S')
    except :
        date = datetime.strptime(row["Record_Date"] , '%d/%m/%Y %H:%M')
    observation_date = date.date()
    observation_datetime = date

    visit_occurrence_id = is_exsit_visit_occurrence_id(row["Event_baznat"])
    visit_detail_id = ''
    if visit_occurrence_id != '' :
        visit_detail_id = is_exsit_visit_detail_id(visit_occurrence_id)

    value_as_number = ''
    value_as_string = ''
    value_as_concept_id = ''
    unit_concept_id = MATERNITY_CLINIC

    if str(row["סיבה עיקרית"]) and row["סיבה עיקרית"] != '-1' :
        if row["סיבה עיקרית"] == 'מעקב הריון עודף':
            observation_concept_id = 22281000119101
        else:
            match_visit_occurrence = df_terms_table.loc[df_terms_table['sourceCode'] == row["סיבה עיקרית"]]
            value = match_visit_occurrence.values[0][1]
            list_observation = value.split('+')
            index_concepts = 0
            while len(list_observation) > index_concepts :
                observation_concept_id = list_observation[index_concepts]
                add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                            value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id ,
                            visit_detail_id , unit_concept_id)
                index_concepts += 1
                index += 1

#### 25 table ###
source_table = pd.read_csv("25.csv")

EHR_CONCEPT_ID = 32817
DATE_OF_LAST_NORMAL_PERIOD = 4088445
SPONTANEOUS = 4196694
FETUS = 40567571
PREGNANCY_AGE = 444135009
PREGNANCY_AGE_BY_WEEK = 366323009


class Preganancy_age_enum(Enum) :
    TWENTY = 23464008
    TWENTY_ONE = 41438001
    TWENTY_TWO = 65035007
    TWENTY_THREE = 86883006
    TWENTY_FOUR = 313179009
    TWENTY_FIVE = 72544005
    TWENTY_SIX = 48688005
    TWENTY_SEVEN = 46906003
    TWENTY_EIGHT = 90797000
    TWENTY_NINE = 45139008
    THIRTY = 71355009
    THIRTY_ONE = 64920003
    THIRTY_TWO = 7707000
    THIRTY_THREE = 78395001
    THIRTY_FOUR = 13763000
    THIRTY_FIVE = 84132007
    THIRTY_SIX = 57907009
    THIRTY_SEVEN = 43697006
    THIRTY_EIGHT = 13798002
    THIRTY_NINE = 80487005
    FORTY = 46230007
    FORTY_ONE = 63503002
    FORTY_TWO = 36428009
    FORTY_THREE = 90968009
    FORTY_FOUR = 90968009


for index_row , row in source_table.iterrows() :
    if is_exsit_person_id(row['ID_BAZNAT']) == True:
        person_id = row["ID_BAZNAT"]
    else:
        continue

    try :
        date = datetime.strptime(row["Record_Date"] , '%d/%m/%Y %H:%M:%S')
    except :
        date = datetime.strptime(row["Record_Date"] , '%m/%d/%Y %H:%M:%S')
    observation_date = date.date()
    observation_datetime = date

    visit_occurrence_id = is_exsit_visit_occurrence_id(row["Event_baznat"])
    visit_detail_id = ''
    if visit_occurrence_id != '' :
        visit_detail_id = is_exsit_visit_detail_id(visit_occurrence_id)
    unit_concept_id = MATERNITY_CLINIC

    value_as_string = ''
    value_as_number = ''
    value_as_concept_id = ''

    ############## Date of last normal period #############################
    if row['Last_Period_Date'] :
        observation_concept_id = DATE_OF_LAST_NORMAL_PERIOD
        if type(row['Last_Period_Date']) == str :
            value_as_string = str(row['Last_Period_Date'])
            value_as_number = ''
            value_as_concept_id = ''
            add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                        value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                        unit_concept_id)
            index += 1
    ############## Spontaneous #############################

    if not math.isnan(row['Spontaneous']) :
        observation_concept_id = SPONTANEOUS
        value_as_number = int(row['Spontaneous'])
        value_as_string = ''
        value_as_concept_id = ''
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1
    ############## Fetus Count #############################
    if not math.isnan(row['Fetus_Count']) :
        observation_concept_id = FETUS
        value_as_number = int(row['Fetus_Count'])
        value_as_string = ''
        value_as_concept_id = ''
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1
    ############## Pregnancy Age #############################
    if row['Pregnancy_Age'] and type(row['Pregnancy_Age']) != float :
        observation_concept_id = PREGNANCY_AGE
        value_as_string = str(row['Pregnancy_Age'])
        value_as_number = ''
        value_as_concept_id = ''
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

        observation_concept_id = PREGNANCY_AGE_BY_WEEK
        week = row['Pregnancy_Age'].split('+')[0]
        if int(week) > 20 :
            week_in_words = num2words(week).upper().replace('-' , '_')
            value_as_concept_id = Preganancy_age_enum[week_in_words].value
            value_as_number = ''
            value_as_string = ''
            add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                        value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id ,
                        visit_detail_id ,
                        unit_concept_id)
            index += 1

#### 26 table ###
source_table = pd.read_csv("26.csv")

NUMBER_OF_PREVIOUS_PREGNANCIES = 4078008
NUMBER_OF_BIRTHS_P = 118212000
NUMBER_OF_ABORTIONS_A = 248989003
NUMBER_OF_EP_EP = 440537001
NUMBER_OF_CAESARS_CS = 4092787
NUMBER_OF_LIVE_CHILDREN_LC = 248991006
VBAC = 237313003

for index_row , row in source_table.iterrows() :
    if is_exsit_person_id(row['ID_BAZNAT']) == True:
        person_id = row["ID_BAZNAT"]
    else:
        continue

    try :
        date = datetime.strptime(row["Record_Date"] , '%d/%m/%Y %H:%M:%S')
    except :
        date = datetime.strptime(row["Record_Date"] , '%m/%d/%Y %H:%M:%S')
    observation_date = date.date()
    observation_datetime = date

    visit_occurrence_id = is_exsit_visit_occurrence_id(row["Event_baznat"])
    visit_detail_id = ''
    if visit_occurrence_id != '' :
        visit_detail_id = is_exsit_visit_detail_id(visit_occurrence_id)

    value_as_number = ''
    value_as_string = ''
    value_as_concept_id = ''
    unit_concept_id = MATERNITY_CLINIC

    ############## NumOfPregnancies_G #############################
    if not math.isnan(row['NumOfPregnancies_G']) :
        observation_concept_id = NUMBER_OF_PREVIOUS_PREGNANCIES
        value_as_number = int(row['NumOfPregnancies_G'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1
    ############## NumOfBirths_P #############################

    if not math.isnan(row['NumOfBirths_P']) :
        observation_concept_id = NUMBER_OF_BIRTHS_P
        value_as_number = int(row['NumOfBirths_P'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1
    ############## NumOfAbortions_A #############################
    if not math.isnan(row['NumOfAbortions_A']) :
        observation_concept_id = NUMBER_OF_ABORTIONS_A
        value_as_number = int(row['NumOfAbortions_A'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1
    ############## NumOfEp_EP #############################
    if not math.isnan(row['NumOfEp_EP']) :
        observation_concept_id = NUMBER_OF_EP_EP
        value_as_number = int(row['NumOfEp_EP'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1
    ############## NumOfCaesars_CS #############################
    if not math.isnan(row['NumOfCaesars_CS']) :
        observation_concept_id = NUMBER_OF_CAESARS_CS
        value_as_number = int(row['NumOfCaesars_CS'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1
    ############## NumOfLiveChildren_LC #############################
    if not math.isnan(row['NumOfLiveChildren_LC']) :
        observation_concept_id = NUMBER_OF_LIVE_CHILDREN_LC
        value_as_number = int(row['NumOfLiveChildren_LC'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1
    ############## VBAC #############################
    if not math.isnan(row['VBAC']) :
        observation_concept_id = VBAC
        value_as_number = int(row['VBAC'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

unit_concept_id = ''

#### 52 table ###
source_table = pd.read_csv("52.csv")

amniotic_fluid_table = pd.read_csv("amniotic_fluid.csv")
df_amniotic_fluid = pd.DataFrame(amniotic_fluid_table , columns=['מי שפיר' , 'concept'])

membranes_rupture_table = pd.read_csv("membranes_rupture.csv")
df_membranes_rupture_table = pd.DataFrame(membranes_rupture_table , columns=['אופן פקיעת קרומים' , 'concept'])

AMNIOTIC_FLUID_CONCEPT_ID = 40454100
RUPTURED_MEMBRANES_CONCEPT_ID = 4224704

for index_row , row in source_table.iterrows() :
    if is_exsit_person_id(row['ID_BAZNAT']) == True:
        person_id = row["ID_BAZNAT"]
    else:
        continue

    if row["זמן בדיקה"] and type(row["זמן בדיקה"]) == str :
        try :
            dateT = datetime.strptime(row["זמן בדיקה"] , '%m/%d/%Y %H:%M')
        except :
            dateT = datetime.strptime(row["זמן בדיקה"] , '%m/%d/%Y %H:%M:%S %p')

    observation_date = dateT.date()
    observation_datetime = dateT
    visit_occurrence_id = is_exsit_visit_occurrence_id(row["Event_baznat"])
    visit_detail_id = ''
    if visit_occurrence_id != '' :
        visit_detail_id = is_exsit_visit_detail_id(visit_occurrence_id)

    value_as_concept_id = ''
    if row["זמן פקיעת קרומים"] and type(row["זמן פקיעת קרומים"]) == str :
        try :
            value_as_string = datetime.strptime(row["זמן פקיעת קרומים"] , '%m/%d/%Y %H:%M')
        except :
            value_as_string = datetime.strptime(row["זמן פקיעת קרומים"] , '%m/%d/%Y %H:%M:%S %p')

    value_as_number = ''
    ################################## אופן פקיעת קרומים #################################
    if str(row["אופן פקיעת קרומים"]) :
        value_as_string = ''
        observation_concept_id = RUPTURED_MEMBRANES_CONCEPT_ID
        match = df_membranes_rupture_table.loc[
            df_membranes_rupture_table['אופן פקיעת קרומים'] == row["אופן פקיעת קרומים"]]
        if match.shape[0] > 0 :
            value = match.values[0][1]
            list_observation = value.split('+')
            index_concepts = 0
            while len(list_observation) > index_concepts :
                value_as_concept_id = list_observation[index_concepts]
                add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                            value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id ,
                            visit_detail_id ,
                            unit_concept_id)
                index_concepts += 1
                index += 1

    ######################################### מי שפיר #####################################
    if str(row["מי שפיר"]) :
        observation_concept_id = AMNIOTIC_FLUID_CONCEPT_ID
        match = df_amniotic_fluid.loc[df_amniotic_fluid['מי שפיר'] == row["מי שפיר"]]
        if match.shape[0] > 0 :
            value_as_concept_id = match.values[0][1]
            add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                        value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id ,
                        visit_detail_id ,
                        unit_concept_id)
            index += 1

#### 59 table ###
source_table = pd.read_csv("59.csv")

EHR_CONCEPT_ID = 32817
HINGES_START_TIME = 249123005
FULL_OPENING_TIME = 249160009
DURATION_OF_PERIOD_1 = 169821004
FETAL_DEPARTURE_TIME = 397836004
DURATION_OF_PERIOD_2 = 169822006
PLACENTAL_EXIT_TIME = 249169005
DURATION_OF_PERIOD_3 = 169823001
MEMBRANES_TIME = 289251005

for index_row , row in source_table.iterrows() :
    if is_exsit_person_id(row['ID_BAZNAT']) == True:
        person_id = row["ID_BAZNAT"]
    else:
        continue
    if row["Record_Date"] and type(row["Record_Date"]) == str :
        try :
            dateT = datetime.strptime(row["Record_Date"] , '%m/%d/%Y %H:%M')
        except :
            dateT = datetime.strptime(row["Record_Date"] , '%m/%d/%Y %H:%M:%S %p')

        observation_date = dateT.date()
        observation_datetime = dateT

    visit_occurrence_id = is_exsit_visit_occurrence_id(row["Event_baznat"])
    visit_detail_id = ''
    if visit_occurrence_id != '' :
        visit_detail_id = is_exsit_visit_detail_id(visit_occurrence_id)

    unit_concept_id = ''
    value_as_number = ''
    value_as_concept_id = ''
    ################################## זמן תחילת צירים #################################
    if str(row["זמן תחילת צירים"]):
        observation_concept_id = HINGES_START_TIME
        if row["זמן תחילת צירים"] and type(row["זמן תחילת צירים"]) == str :
            try :
                value_as_string = datetime.strptime(row["זמן תחילת צירים"] , '%m/%d/%Y %H:%M')
            except :
                value_as_string = datetime.strptime(row["זמן תחילת צירים"] , '%m/%d/%Y %H:%M:%S %p')

            add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                        value_as_number , str(value_as_string) , value_as_concept_id , visit_occurrence_id ,
                        visit_detail_id ,
                        unit_concept_id)
            index += 1

    ################################## זמן פתיחה מלאה #################################
    if str(row["זמן פתיחה מלאה"]):
        observation_concept_id = FULL_OPENING_TIME
        if row["זמן פתיחה מלאה"] and type(row["זמן פתיחה מלאה"]) == str :
            try :
                value_as_string = datetime.strptime(row["זמן פתיחה מלאה"] , '%m/%d/%Y %H:%M')
            except :
                value_as_string = datetime.strptime(row["זמן פתיחה מלאה"] , '%m/%d/%Y %H:%M:%S %p')
            add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                        value_as_number , str(value_as_string) , value_as_concept_id , visit_occurrence_id ,
                        visit_detail_id ,
                        unit_concept_id)
            index += 1

    ################################## משך תקופה 1 #################################
    if str(row["משך תקופה 1"]) :
        observation_concept_id = DURATION_OF_PERIOD_1
        value_as_string = row["משך תקופה 1"]
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , str(value_as_string) , value_as_concept_id , visit_occurrence_id ,
                    visit_detail_id ,
                    unit_concept_id)
        index += 1

    ################################## זמן יציאת עובר #################################
    if str(row["זמן יציאת עובר"]):
        observation_concept_id = FULL_OPENING_TIME
        if row["זמן יציאת עובר"] and type(row["זמן יציאת עובר"]) == str :
            try :
                value_as_string = datetime.strptime(row["זמן יציאת עובר"] , '%m/%d/%Y %H:%M')
            except :
                value_as_string = datetime.strptime(row["זמן יציאת עובר"] , '%m/%d/%Y %H:%M:%S %p')
            add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , str(value_as_string) , value_as_concept_id , visit_occurrence_id ,
                    visit_detail_id ,
                    unit_concept_id)
            index += 1

    ################################## משך תקופה 2 #################################
    if str(row["משך תקופה 2"]) :
        observation_concept_id = DURATION_OF_PERIOD_2
        value_as_string = row["משך תקופה 2"]
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , str(value_as_string) , value_as_concept_id , visit_occurrence_id ,
                    visit_detail_id ,
                    unit_concept_id)
        index += 1

    ################################## זמן יציאת שלייה #################################
    if str(row["זמן יציאת שלייה"]):
        observation_concept_id = FULL_OPENING_TIME
        if row["זמן יציאת שלייה"] and type(row["זמן יציאת שלייה"]) == str :
            try :
                value_as_string = datetime.strptime(row["זמן יציאת שלייה"] , '%m/%d/%Y %H:%M')
            except :
                value_as_string = datetime.strptime(row["זמן יציאת שלייה"] , '%m/%d/%Y %H:%M:%S %p')
            add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                        value_as_number , str(value_as_string) , value_as_concept_id , visit_occurrence_id ,
                        visit_detail_id ,
                        unit_concept_id)
            index += 1

    ################################## משך תקופה 3 #################################
    if str(row["משך תקופה 3"]) :
        observation_concept_id = DURATION_OF_PERIOD_3
        value_as_string = row["משך תקופה 3"]
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , str(value_as_string) , value_as_concept_id , visit_occurrence_id ,
                    visit_detail_id ,
                    unit_concept_id)
        index += 1

    ################################## משך תקופה 3 #################################
    if str(row["משך תקופה מזמן פקיעת קרומים עד יציאת עובר"]) :
        observation_concept_id = MEMBRANES_TIME
        value_as_string = row["משך תקופה מזמן פקיעת קרומים עד יציאת עובר"]
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , str(value_as_string) , value_as_concept_id , visit_occurrence_id ,
                    visit_detail_id ,
                    unit_concept_id)
        index += 1

#### 61 table ###
source_table = pd.read_csv("61_new.csv")

#######display#####
display_table = pd.read_csv("display.csv")
df_display_table = pd.DataFrame(display_table , columns=['display' , 'concept'])

#######delivery way#####
delivery_way_table = pd.read_csv("delivery_way.csv")

# 1 MINUTE AFGAR
ONE_MINUTE_APGAR_HEART_RATE = 3027152
ONE_MINUTE_APGAR_COLOR = 3026329
ONE_MINUTE_APGAR_MUSCLE_TONE = 3013445
ONE_MINUTE_APGAR_SCORE = 3016704
ONE_MINUTE_APGAR_RESPIRATORY_EFFORT = 3023275
ONE_MINUTE_APGAR_REFLEX_IRRITABILITY = 3027666

# 5 MINUTE AFGAR
FIVE_MINUTE_APGAR_HEART_RATE = 3026961
FIVE_MINUTE_APGAR_COLOR = 3025592
FIVE_MINUTE_APGAR_MUSCLE_TONE = 3027494
FIVE_MINUTE_APGAR_SCORE = 3004221
FIVE_MINUTE_APGAR_RESPIRATORY_EFFORT = 3024292
FIVE_MINUTE_APGAR_REFLEX_IRRITABILITY = 3028332

# 10 MINUTE AFGAR
TEN_MINUTE_APGAR_HEART_RATE = 3007503
TEN_MINUTE_APGAR_COLOR = 3005021
TEN_MINUTE_APGAR_MUSCLE_TONE = 3006474
TEN_MINUTE_APGAR_SCORE = 3016162
TEN_MINUTE_APGAR_RESPIRATORY_EFFORT = 3025485
TEN_MINUTE_APGAR_REFLEX_IRRITABILITY = 3022387

# others
BIRTH_WEIGHT = 4264825
UMBILICAL_CORD_NORMAL = 289315001
ABSENT_BLOOD_VESSEL_IN_UMBILICAL_CORD = 302945005
UMBILICUS_FINDING = 4096860
PRESENTATION = 4084388
PATTERN_OF_DELIVERY = 4126390
DEATH_DIAGNOSIS = 4052310

for index_row , row in source_table.iterrows() :
    if is_exsit_person_id(row['ID_BAZNAT']) == True:
        person_id = row["ID_BAZNAT"]
    else:
        continue

    try :
        date = datetime.strptime(row["זמן לידה"] , '%m/%d/%Y %H:%M')
    except :
        date = datetime.strptime(row["זמן לידה"] , '%m/%d/%Y %H:%M:%S %p')
    observation_date = dateT.date()
    observation_datetime = dateT

    visit_occurrence_id = is_exsit_visit_occurrence_id(row["Event_baznat"])
    visit_detail_id = ''
    if visit_occurrence_id != '' :
        visit_detail_id = is_exsit_visit_detail_id(visit_occurrence_id)

    unit_concept_id = ''
    value_as_string = ''
    value_as_number = ''
    observation_concept_id = DEATH_DIAGNOSIS
    match_visit_occurrence = df_terms_table.loc[df_terms_table['sourceCode'] == row["סיבת המוות"]]
    index_concept = 0
    while match_visit_occurrence.values.shape[0] > index_concept :
        value_as_concept_id = match_visit_occurrence.values[index_concept][1]
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index_concept += 1
        index += 1

    value_as_concept_id = ''
    # --------------------- 1 min Apgar ----------------------#
    if not math.isnan(row['אפגר 1 - סכום ערכים']) :
        observation_concept_id = ONE_MINUTE_APGAR_SCORE
        value_as_number = int(row['אפגר 1 - סכום ערכים'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 1 - דופק']) :
        observation_concept_id = ONE_MINUTE_APGAR_HEART_RATE
        value_as_number = int(row['אפגר 1 - דופק'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 1 - נשימה']) :
        observation_concept_id = ONE_MINUTE_APGAR_RESPIRATORY_EFFORT
        value_as_number = int(row['אפגר 1 - נשימה'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 1 - צבע']) :
        observation_concept_id = ONE_MINUTE_APGAR_COLOR
        value_as_number = int(row['אפגר 1 - צבע'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 1 - טונוס']) :
        observation_concept_id = ONE_MINUTE_APGAR_MUSCLE_TONE
        value_as_number = int(row['אפגר 1 - טונוס'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 1 - תגובה']) :
        observation_concept_id = ONE_MINUTE_APGAR_REFLEX_IRRITABILITY
        value_as_number = int(row['אפגר 1 - תגובה'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    # --------------------- 5 min Apgar ----------------------#
    if not math.isnan(row['אפגר 5 - סכום ערכים']) :
        observation_concept_id = FIVE_MINUTE_APGAR_SCORE
        value_as_number = int(row['אפגר 5 - סכום ערכים'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 5 - דופק']) :
        observation_concept_id = FIVE_MINUTE_APGAR_HEART_RATE
        value_as_number = int(row['אפגר 5 - דופק'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 5 - נשימה']) :
        observation_concept_id = FIVE_MINUTE_APGAR_RESPIRATORY_EFFORT
        value_as_number = int(row['אפגר 5 - נשימה'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 5 - צבע']) :
        observation_concept_id = FIVE_MINUTE_APGAR_COLOR
        value_as_number = int(row['אפגר 5 - צבע'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 5 - טונוס']) :
        observation_concept_id = FIVE_MINUTE_APGAR_MUSCLE_TONE
        value_as_number = int(row['אפגר 5 - טונוס'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 5 - תגובה']) :
        observation_concept_id = FIVE_MINUTE_APGAR_REFLEX_IRRITABILITY
        value_as_number = int(row['אפגר 5 - תגובה'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    # --------------------- 10 min Apgar ----------------------#
    if not math.isnan(row['אפגר 10 - סכום ערכים']) :
        observation_concept_id = TEN_MINUTE_APGAR_SCORE
        value_as_number = int(row['אפגר 10 - סכום ערכים'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 10 - דופק']) :
        observation_concept_id = TEN_MINUTE_APGAR_HEART_RATE
        value_as_number = int(row['אפגר 10 - דופק'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 10 - נשימה']) :
        observation_concept_id = TEN_MINUTE_APGAR_RESPIRATORY_EFFORT
        value_as_number = int(row['אפגר 10 - נשימה'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 10 - צבע']) :
        observation_concept_id = TEN_MINUTE_APGAR_COLOR
        value_as_number = int(row['אפגר 10 - צבע'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 10 - טונוס']) :
        observation_concept_id = TEN_MINUTE_APGAR_MUSCLE_TONE
        value_as_number = int(row['אפגר 10 - טונוס'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    if not math.isnan(row['אפגר 10 - תגובה']) :
        observation_concept_id = TEN_MINUTE_APGAR_REFLEX_IRRITABILITY
        value_as_number = int(row['אפגר 10 - תגובה'])
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    # --------------------- others terms ------------------#
    # weight
    if not math.isnan(row['משקל']) :
        observation_concept_id = BIRTH_WEIGHT
        value_as_number = row['משקל']
        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    # umbilical_cord
    if row['חבל טבור עם 3 כלי דם'] :
        observation_concept_id = UMBILICUS_FINDING
        value_as_number = ''
        if row['חבל טבור עם 3 כלי דם'] == 'כן' :
            value_as_concept_id = UMBILICAL_CORD_NORMAL
        else :
            value_as_concept_id = ABSENT_BLOOD_VESSEL_IN_UMBILICAL_CORD

        add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                    value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id , visit_detail_id ,
                    unit_concept_id)
        index += 1

    # display
    if row['מצג'] :
        observation_concept_id = PRESENTATION
        value_as_number = ''
        match_display = df_display_table.loc[df_display_table['display'] == row['מצג']]
        if match_display.shape[0] > 0 :
            value_as_concept_id = match_display.values[0][1]
            add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                        value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id ,
                        visit_detail_id ,
                        unit_concept_id)
            index += 1

    # df_delivery_table
    if row['אופן הלידה'] :
        value_as_number = ''
        observation_concept_id = PATTERN_OF_DELIVERY
        match_delivery = delivery_way_table.loc[delivery_way_table['delivery_way'] == row['אופן הלידה']]
        if match_delivery.shape[0] > 0 :
            value_as_concept_id = match_delivery.values[0][2]
            add_to_data(index , person_id , observation_concept_id , observation_date , observation_datetime ,
                        value_as_number , value_as_string , value_as_concept_id , visit_occurrence_id ,
                        visit_detail_id ,
                        unit_concept_id)
            index += 1

df_result = pd.DataFrame(data ,
                         columns=["observation_id" , "person_id" , "observation_concept_id" , "observation_date" ,
                                  "observation_datetime" , "observation_type_concept_id" ,
                                  "value_as_number" , "value_as_string" , "value_as_concept_id" ,
                                  "qualifier_concept_id" , "unit_concept_id" , "provider_id" , "visit_occurrence_id" ,
                                  "visit_detail_id" ,
                                  "observation_source_value" , "observation_source_concept_id" , "unit_source_value" ,
                                  "qualifier_source_value" , "value_source_value" , "observation_event_id" ,
                                  "obs_event_field_concept_id"])

df_result.to_csv('observation.csv' , encoding='utf-8' , index=False)
