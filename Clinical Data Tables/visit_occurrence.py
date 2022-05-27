import math
from datetime import datetime
import pandas as pd

source_table = pd.read_csv("89.csv")
d_table_89 = pd.DataFrame(source_table ,columns=['Event_baznat'])
### mark duplicte records as True ###
result = d_table_89.duplicated()
source_table["duplicates"] = result

table_92 = pd.read_csv("92.csv")
df_table_92 = pd.DataFrame(table_92 , columns=["ID_BAZNAT" , "Event_baznat" , "Department", "Department_Entry_Date" , "Department_Exit_Date"])

#### Person ####
dep_person = pd.read_csv("person.csv")
df_person = pd.DataFrame(dep_person ,columns=['person_id'])

#### Care Site ####
care_site_table = pd.read_csv("care_site.csv")
df_care_site = pd.DataFrame(care_site_table ,columns=["care_site_id" , "care_site_name" ])

### Concepts ####
INPATIENT_VISIT_CONCEPT_ID = 33022008
EHR_CONCEPT_ID = 32817

i=0
data = []
new_id = 1000
duplicates_dic = {}
for index_row, row in source_table.iterrows():
    ### case - event baznat is not nan ###
    if math.isnan(row['Event_baznat']):
        continue

    original_id = int(row['Event_baznat'])

    ### case - id baznat not in person table ###
    match_person = df_person.loc[df_person['person_id'] == row['ID_BAZNAT']]
    if match_person.shape[0]>0:
        person_id = int(row[0])
    else:
        continue

    match_event_baznat_92 = df_table_92.loc[df_table_92['Event_baznat'] == row['Event_baznat']]

    no_date_flag_start = True if type(row["HOSP_ENTRY_DATE"]) != str and math.isnan(row["HOSP_ENTRY_DATE"]) else False
    no_date_flag_end = True if type(row["HOSP_EXIT_DATE"]) != str and math.isnan(row["HOSP_EXIT_DATE"]) else False

    entry_date = ''
    exit_date = ''
    ### handle miss date
    if no_date_flag_start == True or no_date_flag_end == True: ### miss entry date & exit date ####
        entry_date_table_92 = True if match_event_baznat_92["Department_Entry_Date"].size > 0 else False
        exit_date_table_92 = True if  match_event_baznat_92["Department_Exit_Date"].size > 0 else False

        if no_date_flag_start and  no_date_flag_start:
            if  entry_date_table_92 and exit_date_table_92 and \
                    match_event_baznat_92["Department_Exit_Date"].values[0] != '-1' and match_event_baznat_92["Department_Exit_Date"].values[0] != '-1':
                entry_date = datetime.strptime(match_event_baznat_92["Department_Entry_Date"].values[0], '%d/%m/%Y %H:%M')
                exit_date = datetime.strptime(match_event_baznat_92["Department_Exit_Date"].values[0], '%d/%m/%Y %H:%M')

        elif no_date_flag_start : ### miss entry date only
           index_date = 0
           while match_event_baznat_92["Department_Entry_Date"].size > index_date and entry_date is '':
                if match_event_baznat_92["Department_Exit_Date"].values[index_date] != '-1' :
                    exit_date = datetime.strptime(match_event_baznat_92["HOSP_EXIT_DATE"] , '%d/%m/%Y %H:%M')
                    new_entry_date = datetime.strptime(row['Department_Entry_Date'].values[index_date] , '%d/%m/%Y %H:%M')
                    if exit_date > new_entry_date and 0 < (exit_date-new_entry_date).days < 30 :
                        entry_date = new_entry_date
                    index_date += 1

        else:  ### miss exit date only
           index_date = 0
           while match_event_baznat_92["Department_Exit_Date"].size > index_date and exit_date is '' :
               if match_event_baznat_92["Department_Exit_Date"].values[index_date] != '-1':
                   new_exit_date = datetime.strptime(match_event_baznat_92["Department_Exit_Date"].values[index_date] , '%d/%m/%Y %H:%M')
                   entry_date = datetime.strptime(row['HOSP_ENTRY_DATE'], '%d/%m/%Y %H:%M')
                   if new_exit_date > entry_date and 0 < (new_exit_date-entry_date).days < 30:
                       exit_date = new_exit_date
               index_date += 1

    else:
        entry_date = datetime.strptime(row['HOSP_ENTRY_DATE'] , '%d/%m/%Y %H:%M')
        exit_date = datetime.strptime(row['HOSP_EXIT_DATE'] , '%d/%m/%Y %H:%M')

    ### case - no entry date or exit date ###
    if entry_date is '' or exit_date is '' :
         continue

    preceding_visit_occurrence_id = ''

    ### case -duplicates ###
    match_source_table = source_table.loc[source_table['Event_baznat'] == row['Event_baznat']]
    if match_source_table.shape[0] > 1 and duplicates_dic.get(original_id) is None:
        duplicates_dic[original_id] = entry_date # the first appearance

    if row['duplicates'] == True: # case  - is duplicate -
        date_of_duplicate_id = duplicates_dic.get(original_id) # the secned time or more
        if (entry_date - date_of_duplicate_id).days >= 1: # more than 24 hours
            visit_occurrence_id = new_id
            preceding_visit_occurrence_id = original_id
            new_id += 1
            duplicates_dic[original_id] = entry_date
        else:
            duplicates_dic[original_id] = entry_date
            continue

    else:
        visit_occurrence_id = original_id

    visit_start_date = entry_date.date()
    visit_start_datetime = entry_date
    visit_end_date = exit_date.date()
    visit_end_datetime = exit_date
    visit_concept_id = INPATIENT_VISIT_CONCEPT_ID
    visit_type_concept_id = EHR_CONCEPT_ID
    provider_id = ''

    # handle care_site_id
    care_site_id = ''
    if match_event_baznat_92["Department"].size > 0 :
        care_site_name = match_event_baznat_92["Department"].values[0]
        match_care_site = df_care_site.loc[df_care_site["care_site_name"] == care_site_name]
        if match_care_site["care_site_id"].size > 0 :
            care_site_id = match_care_site["care_site_id"].values[0]

    visit_source_value = ''
    visit_source_concept_id = EHR_CONCEPT_ID
    admitted_from_concept_id = 0
    admitted_from_source_value = ''
    discharged_to_source_value = ''
    discharged_to_concept_id = ''

    data.append([visit_occurrence_id , person_id , visit_concept_id , visit_start_date , visit_start_datetime , visit_end_date ,
             visit_end_datetime , visit_type_concept_id , provider_id , care_site_id , visit_source_value , admitted_from_concept_id ,
             admitted_from_source_value , discharged_to_source_value , discharged_to_concept_id , preceding_visit_occurrence_id])

df_result = pd.DataFrame(data, columns=['visit_occurrence_id', 'person_id', 'visit_concept_id',  'visit_start_date' ,'visit_start_datetime','visit_end_date','visit_end_datetime',
                 'visit_type_concept_id','provider_id','care_site_id','visit_source_value','admitted_from_concept_id','admitted_from_source_value',
                 'discharged_to_source_value', 'discharged_to_concept_id','preceding_visit_occurrence_id'])

df_result.to_csv('visit_occurrence.csv', encoding='utf-8', index=False)
