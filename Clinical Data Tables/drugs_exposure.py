import pandas as pd
from googletrans import Translator
import numpy as np
from datetime import timedelta
from datetime import datetime , date
import re

drug_names = pd.read_csv('drugs_names.csv')
drug_cols = drug_names.columns
drugs_and_concepts_numbers = []
for drug_text in drug_cols:
    if drug_text == "Drug_Name" or drug_text == "counts":
        continue
    else:
        names_and_concept_list=res = re.findall(r'\w+', drug_text)
        drugs_and_concepts_numbers.append(names_and_concept_list)

# _________________________________table 58_________________________________________
source_table = pd.read_csv('58.csv')
data = []

source_table_doc = source_table.rename(columns={"שם תרופה":"Drug_Name","למשך":"for_how_long","מינון":"amount"})
source_table_doc = source_table_doc[["ID_BAZNAT",'Event_baznat',"Drug_Name", "days_supply", "Record_Date", "quantity"]]

source_table = source_table.rename(columns={"שם תרופה":"Drug_Name","למשך":"days_supply","Record_Date":"drug_exposure_start_datetime","ID_BAZNAT": "person_id",'Event_baznat':'visit_occurrence_id',"מינון":"quantity"})
source_table = source_table[["person_id","visit_occurrence_id", "Drug_Name", "days_supply", "drug_exposure_start_datetime", "quantity"]]
drug_exposure_id = 0
source_table['drug_concept_id'] = 0
source_table['drug_source_value'] = ""
source_table["drug_exposure_end_date"] = None
source_table['drug_exposure_id'] = 0
source_table['drug_exposure_start_date'] = None
source_table['drug_exposure_end_datetime'] = None
source_table['verbatim_end_date'] = None
source_table['drug_type_concept_id'] = 32838  ## EHR prescription
source_table['stop_reason'] = 0
source_table['refills'] = 0
source_table['route_concept_id'] = 0
source_table['lot_number'] = 0
source_table['provider_id'] = 0
source_table['visit_detail_id'] = 0
source_table['drug_source_concept_id'] = 0
source_table['route_source_value'] = 0
source_table['dose_unit_source_value'] = 0
source_table['sig'] = None

source_table['drug_exposure_start_date'] = pd.to_datetime(source_table['drug_exposure_start_datetime']).dt.date


for index_row, row in source_table.iterrows():
    try:
        en_text = ''
        split_words = row['days_supply'].split(' ')
        if len(split_words) == 11:
            if split_words[10] == 'שבועות':
                en_text = split_words[9] + ' weeks'
            elif split_words[10] == 'חודשים' or split_words[10] == 'חודש':
                en_text = split_words[9] + ' months'
            else:
                en_text = split_words[9] + ' days'
        else:
            if split_words[9] == 'שבועות':
                en_text = split_words[8] + ' weeks'
            elif split_words[9] == 'חודשים' or split_words[9] == 'חודש':
                en_text = split_words[8] + ' months'
            else:
                en_text = split_words[8] + ' days'
        # source_table.loc[index_row, 'days_supply'] = en_text

        new_value = 0
        string_date = en_text
        split_words = string_date.split(' ')
        if split_words[1] == "days":
            new_value = int(split_words[0])

        elif split_words[1] == "weeks":
            new_value = int(split_words[0]) * 7
        else:
            new_value = int(split_words[0]) * 30
        source_table_doc.loc[index_row, 'days_supply'] = new_value
    except:
        print('e')
        continue

    is_exist = False
    for lst in drugs_and_concepts_numbers:
        for elem in lst:
             if any(map(str.isdigit, elem)):
                 break
             elif len(elem)>1:
                 # elem.lower() in row["Drug_Name"].lower():
                if row["Drug_Name"].find(elem) != -1:
                    row['drug_concept_id'] = int(lst[-1])
                    is_exist = True
                    break
                else:
                    continue
             else:
                continue
        if is_exist == True:
            break

    if is_exist == False:
        row['drug_concept_id'] = 0

    try:
        time_to_add = timedelta(days=new_value)
        days_supply = new_value
        datetime = datetime.strptime(row["drug_exposure_start_datetime"], "%m/%d/%Y  %I:%M:%S %p")
        new_val = row["quantity"].split(' ')
        quantity = new_val[0]
        dose_unit = new_val[1]
        end_datetime = datetime + time_to_add
        end_date = end_datetime.date()
        drug_name = row["Drug_Name"]

        data.append([drug_exposure_id, row["person_id"],  row['drug_concept_id'], row["drug_exposure_start_date"],
                     row["drug_exposure_start_datetime"],
                     end_datetime, end_date, row['verbatim_end_date'], row['refills'],
                     row['drug_type_concept_id'], row['stop_reason'], quantity, days_supply, row["sig"],
                     row['route_concept_id'], row['lot_number'], row['provider_id'], row['visit_occurrence_id'],
                     row['visit_detail_id'],
                     drug_name, row['drug_source_concept_id'], row['route_source_value'],
                     dose_unit])

        drug_exposure_id += 1
    except:
        print('e')
        continue

df_result = pd.DataFrame(data, columns=["drug_exposure_id", "person_id", 'drug_concept_id',"drug_exposure_start_date",'drug_exposure_start_datetime','drug_exposure_end_datetime',"drug_exposure_end_date",'verbatim_end_date', 'refills',
'drug_type_concept_id', 'stop_reason', 'quantity', "days_supply", "sig",'route_concept_id','lot_number', 'provider_id', 'visit_occurrence_id', 'visit_detail_id', 'drug_source_value', 'drug_source_concept_id', 'route_source_value', 'dose_unit_source_value'])


source_table_doc.to_csv(r'C:\Users\ayalon\Desktop\data of project\data_white_rabbit\58.csv', encoding='utf-8', index=False)##musttttttttt


# //___________________table 78________________________________________

source_table = pd.read_csv('78.csv')
data = []
source_table_doc = source_table.rename(columns={"שם תרופה":"Drug_Name","למשך":"for_how_long","מינון":"amount"})
source_table_doc = source_table_doc[["ID_BAZNAT",'Event_baznat',"Drug_Name", "days_supply", "Record_Date", "quantity"]]

source_table = source_table.rename(columns={"שם תרופה":"Drug_Name","למשך":"days_supply","Record_Date":"drug_exposure_start_datetime","ID_BAZNAT": "person_id",'Event_baznat':'visit_occurrence_id',"מינון":"quantity"})
source_table = source_table[["person_id","visit_occurrence_id", "Drug_Name", "days_supply", "drug_exposure_start_datetime", "quantity"]]
drug_exposure_id = 0
source_table['drug_concept_id'] = 0
source_table['drug_source_value'] = ""
source_table["drug_exposure_end_date"] = None
source_table['drug_exposure_id'] = 0
source_table['drug_exposure_start_date'] = None
source_table['drug_exposure_end_datetime'] = None
source_table['verbatim_end_date'] = None
source_table['drug_type_concept_id'] = 32838  ## EHR prescription
source_table['stop_reason'] = 0
source_table['refills'] = 0
source_table['route_concept_id'] = 0
source_table['lot_number'] = 0
source_table['provider_id'] = 0
source_table['visit_detail_id'] = 0
source_table['drug_source_concept_id'] = 0
source_table['route_source_value'] = 0
source_table['dose_unit_source_value'] = 0
source_table['sig'] = None

source_table['drug_exposure_start_date'] = pd.to_datetime(source_table['drug_exposure_start_datetime']).dt.date


for index_row, row in source_table.iterrows():
    try:
        en_text = ''
        split_words = row['days_supply'].split(' ')
        if len(split_words) == 11:
            if split_words[10] == 'שבועות':
                en_text = split_words[9] + ' weeks'
            elif split_words[10] == 'חודשים' or split_words[10] == 'חודש':
                en_text = split_words[9] + ' months'
            else:
                en_text = split_words[9] + ' days'
        else:
            if split_words[9] == 'שבועות':
                en_text = split_words[8] + ' weeks'
            elif split_words[9] == 'חודשים' or split_words[9] == 'חודש':
                en_text = split_words[8] + ' months'
            else:
                en_text = split_words[8] + ' days'
        # source_table.loc[index_row, 'days_supply'] = en_text

        new_value = 0
        string_date = en_text
        split_words = string_date.split(' ')
        if split_words[1] == "days":
            new_value = int(split_words[0])

        elif split_words[1] == "weeks":
            new_value = int(split_words[0]) * 7
        else:
            new_value = int(split_words[0]) * 30
        source_table_doc.loc[index_row, 'days_supply'] = new_value
    except:
        print('e')
        continue

    is_exist = False
    for lst in drugs_and_concepts_numbers:
        for elem in lst:
            if any(map(str.isdigit, elem)):
                break
            elif len(elem) > 1:
                # elem.lower() in row["Drug_Name"].lower():
                if row["Drug_Name"].find(elem) != -1:
                    row['drug_concept_id'] = int(lst[-1])
                    is_exist = True
                    break
                else:
                    continue
            else:
                continue
        if is_exist == True:
            break

    if is_exist == False:
        row['drug_concept_id'] = 0

    try:
        time_to_add = timedelta(days=new_value)
        days_supply = new_value
        datetime = datetime.strptime(row["drug_exposure_start_datetime"], "%m/%d/%Y  %I:%M:%S %p")
        new_val = row["quantity"].split(' ')
        quantity = new_val[0]
        dose_unit = new_val[1]
        end_datetime = datetime + time_to_add
        end_date = end_datetime.date()
        drug_name = row["Drug_Name"]

        data.append([drug_exposure_id, row["person_id"], row['drug_concept_id'], row["drug_exposure_start_date"],
                     row["drug_exposure_start_datetime"],
                     end_datetime, end_date, row['verbatim_end_date'], row['refills'],
                     row['drug_type_concept_id'], row['stop_reason'], quantity, days_supply, row["sig"],
                     row['route_concept_id'], row['lot_number'], row['provider_id'], row['visit_occurrence_id'],
                     row['visit_detail_id'],
                     drug_name, row['drug_source_concept_id'], row['route_source_value'],
                     dose_unit])

        drug_exposure_id += 1
    except:
        print('e')
        continue

df_result_78 = pd.DataFrame(data, columns=["drug_exposure_id", "person_id", 'drug_concept_id',"drug_exposure_start_date",'drug_exposure_start_datetime','drug_exposure_end_datetime',"drug_exposure_end_date",'verbatim_end_date', 'refills',
'drug_type_concept_id', 'stop_reason', 'quantity', "days_supply", "sig",'route_concept_id','lot_number', 'provider_id', 'visit_occurrence_id', 'visit_detail_id', 'drug_source_value', 'drug_source_concept_id', 'route_source_value', 'dose_unit_source_value'])


source_table_doc.to_csv(r'C:\Users\ayalon\Desktop\data of project\data_white_rabbit\78.csv', encoding='utf-8', index=False)##musttttttttt

df_result = df_result.append(df_result_78, ignore_index=True)


# //___________________table 85________________________________________


source_table = pd.read_csv('85.csv')
data = []
source_table_doc = source_table.rename(columns={"שם תרופה":"Drug_Name","למשך":"for_how_long","מינון":"amount"})
source_table_doc = source_table_doc[["ID_BAZNAT",'Event_baznat',"Drug_Name", "days_supply", "Record_Date", "quantity"]]

source_table = source_table.rename(columns={"שם תרופה":"Drug_Name","למשך":"days_supply","Record_Date":"drug_exposure_start_datetime","ID_BAZNAT": "person_id",'Event_baznat':'visit_occurrence_id',"מינון":"quantity"})
source_table = source_table[["person_id","visit_occurrence_id", "Drug_Name", "days_supply", "drug_exposure_start_datetime", "quantity"]]
drug_exposure_id = 0
source_table['drug_concept_id'] = 0
source_table['drug_source_value'] = ""
source_table["drug_exposure_end_date"] = None
source_table['drug_exposure_id'] = 0
source_table['drug_exposure_end_datetime'] = None
source_table['verbatim_end_date'] = None
source_table['drug_type_concept_id'] = 32838  ## EHR prescription
source_table['stop_reason'] = 0
source_table['refills'] = 0
source_table['route_concept_id'] = 0
source_table['lot_number'] = 0
source_table['provider_id'] = 0
source_table['visit_detail_id'] = 0
source_table['drug_source_concept_id'] = 0
source_table['route_source_value'] = 0
source_table['dose_unit_source_value'] = 0
source_table['sig'] = None

source_table['drug_exposure_start_date'] = pd.to_datetime(source_table['drug_exposure_start_datetime']).dt.date


for index_row, row in source_table.iterrows():
    try:
        en_text = ''
        split_words = row['days_supply'].split(' ')
        if len(split_words) == 11:
            if split_words[10] == 'שבועות':
                en_text = split_words[9] + ' weeks'
            elif split_words[10] == 'חודשים' or split_words[10] == 'חודש':
                en_text = split_words[9] + ' months'
            else:
                en_text = split_words[9] + ' days'
        else:
            if split_words[9] == 'שבועות':
                en_text = split_words[8] + ' weeks'
            elif split_words[9] == 'חודשים' or split_words[9] == 'חודש':
                en_text = split_words[8] + ' months'
            else:
                en_text = split_words[8] + ' days'
        # source_table.loc[index_row, 'days_supply'] = en_text

        new_value = 0
        string_date = en_text
        split_words = string_date.split(' ')
        if split_words[1] == "days":
            new_value = int(split_words[0])

        elif split_words[1] == "weeks":
            new_value = int(split_words[0]) * 7
        else:
            new_value = int(split_words[0]) * 30
        source_table_doc.loc[index_row, 'days_supply'] = new_value
    except:
        print('e')
        continue

    is_exist = False
    for lst in drugs_and_concepts_numbers:
        for elem in lst:
            if any(map(str.isdigit, elem)):
                break
            elif len(elem) > 1:
                # elem.lower() in row["Drug_Name"].lower():
                if row["Drug_Name"].find(elem) != -1:
                    row['drug_concept_id'] = int(lst[-1])
                    is_exist = True
                    break
                else:
                    continue
            else:
                continue
        if is_exist == True:
            break

    if is_exist == False:
        row['drug_concept_id'] = 0

    try:
        time_to_add = timedelta(days=new_value)
        days_supply = new_value
        datetime = datetime.strptime(row["drug_exposure_start_datetime"], "%m/%d/%Y  %I:%M:%S %p")
        new_val = row["quantity"].split(' ')
        quantity = new_val[0]
        dose_unit = new_val[1]
        end_datetime = datetime + time_to_add
        end_date = end_datetime.date()
        drug_name = row["Drug_Name"]

        data.append([drug_exposure_id, row["person_id"], row['drug_concept_id'], row["drug_exposure_start_date"],
                     row["drug_exposure_start_datetime"],
                     end_datetime, end_date, row['verbatim_end_date'], row['refills'],
                     row['drug_type_concept_id'], row['stop_reason'], quantity, days_supply, row["sig"],
                     row['route_concept_id'], row['lot_number'], row['provider_id'], row['visit_occurrence_id'],
                     row['visit_detail_id'],
                     drug_name, row['drug_source_concept_id'], row['route_source_value'],
                     dose_unit])

        drug_exposure_id += 1
    except:
        print('e')
        continue


df_result_85 = pd.DataFrame(data, columns=["drug_exposure_id", "person_id", 'drug_concept_id',"drug_exposure_start_date",'drug_exposure_start_datetime','drug_exposure_end_datetime',"drug_exposure_end_date",'verbatim_end_date', 'refills',
'drug_type_concept_id', 'stop_reason', 'quantity', "days_supply", "sig",'route_concept_id','lot_number', 'provider_id', 'visit_occurrence_id', 'visit_detail_id', 'drug_source_value', 'drug_source_concept_id', 'route_source_value', 'dose_unit_source_value'])


source_table_doc.to_csv(r'C:\Users\ayalon\Desktop\data of project\data_white_rabbit\85.csv', encoding='utf-8', index=False)##musttttttttt


df_result = df_result.append(df_result_85, ignore_index=True)


# //___________________table 57________________________________________

source_table = pd.read_csv('57.csv')
source_table.drop('Event_baznat.1', inplace=True, axis=1)
data = []


source_table_doc = source_table.dropna(subset=['Stop_Date'])
source_table_doc = source_table_doc[["ID_BAZNAT", 'Event_baznat', "Drugs_Text", "DosageOrder", "Start_Date", "Stop_Date"]]

source_table = source_table.rename(columns={"ID_BAZNAT": "person_id", "Start_Date": "drug_exposure_start_datetime", "Stop_Date": "drug_exposure_end_datetime", 'Event_baznat':'visit_occurrence_id', "DosageOrder":"quantity"})
source_table = source_table.dropna(subset=['drug_exposure_end_datetime'])
source_table = source_table[["person_id", "Drugs_Text", "drug_exposure_start_datetime", "drug_exposure_end_datetime", "visit_occurrence_id","quantity"]]

source_table['drug_concept_id'] = 0
source_table['drug_source_value'] = ""
source_table["days_supply"] = 0
source_table['drug_exposure_id'] = 0

source_table['verbatim_end_date'] = None
source_table['drug_type_concept_id'] = 32829  ## EHR inpatient note
source_table['stop_reason'] = 0
source_table['refills'] = 0
source_table['days_supply'] = 0
source_table['sig'] = None
source_table['route_concept_id'] = 0
source_table['lot_number'] = 0
source_table['provider_id'] = 0
source_table['visit_detail_id'] = 0
source_table['drug_source_concept_id'] = 0
source_table['route_source_value'] = 0
source_table['dose_unit_source_value'] = 0


source_table['drug_exposure_start_date'] = pd.to_datetime(source_table['drug_exposure_start_datetime']).dt.date
source_table['drug_exposure_end_date'] = pd.to_datetime(source_table['drug_exposure_end_datetime']).dt.date


for index_row, row in source_table.iterrows():
    try:
        is_exist = False
        for lst in drugs_and_concepts_numbers:
            for elem in lst:
                if any(map(str.isdigit, elem)):
                    break
                elif len(elem) > 1:

                    if row["Drugs_Text"].find(elem) != -1:
                        row['drug_concept_id'] = int(lst[-1])
                        is_exist = True
                        break
                    else:
                        continue
                else:
                    continue
            if is_exist == True:
                break

        if is_exist == False:
            row['drug_concept_id'] = 0

        new_val = row["quantity"].split(' ')
        quantity = new_val[0]
        dose_unit = new_val[1]
        drug_name = row["Drugs_Text"]
        data.append([drug_exposure_id, row["person_id"], row['drug_concept_id'], row["drug_exposure_start_date"], row['drug_exposure_start_datetime'],
        row['drug_exposure_end_datetime'], row["drug_exposure_end_date"], row['verbatim_end_date'], row['refills'], row['drug_type_concept_id'], row['stop_reason'],quantity, row["days_supply"], row["sig"],
        row['route_concept_id'], row['lot_number'], row['provider_id'], row['visit_occurrence_id'], row['visit_detail_id'],
        drug_name, row['drug_source_concept_id'], row['route_source_value'],
        dose_unit])
        drug_exposure_id += 1
    except :
        print("e")
        continue

df_result_57 = pd.DataFrame(data, columns=["drug_exposure_id", "person_id", 'drug_concept_id',"drug_exposure_start_date",'drug_exposure_start_datetime','drug_exposure_end_datetime',"drug_exposure_end_date",'verbatim_end_date', 'refills',
'drug_type_concept_id', 'stop_reason', 'quantity', "days_supply", "sig",'route_concept_id','lot_number', 'provider_id', 'visit_occurrence_id', 'visit_detail_id', 'drug_source_value', 'drug_source_concept_id', 'route_source_value', 'dose_unit_source_value'])

source_table_doc.to_csv(r'C:\Users\ayalon\Desktop\data of project\data_white_rabbit\57.csv', encoding='utf-8', index=False)##musttttttttt


df_result = df_result.append(df_result_57, ignore_index=True)


# //___________________table 69________________________________________


source_table = pd.read_csv('69.csv')
data = []

source_table_doc = source_table.dropna(subset=['Stop_Date'])
source_table_doc = source_table_doc[["ID_BAZNAT", 'Event_baznat', "Drugs_Text", "DosageOrder", "Start_Date", "Stop_Date"]]

source_table = source_table.rename(columns={"ID_BAZNAT": "person_id", "Start_Date": "drug_exposure_start_datetime", "Stop_Date": "drug_exposure_end_datetime", 'Event_baznat':'visit_occurrence_id', "DosageOrder":"quantity"})
source_table = source_table.dropna(subset=['drug_exposure_end_datetime'])
source_table = source_table[["person_id", "Drugs_Text", "drug_exposure_start_datetime", "drug_exposure_end_datetime", "visit_occurrence_id","quantity"]]

source_table['drug_concept_id'] = 0
source_table['drug_source_value'] = ""
source_table["days_supply"] = 0
source_table['drug_exposure_id'] = 0

source_table['verbatim_end_date'] = None
source_table['drug_type_concept_id'] = 32829  ## EHR inpatient note
source_table['stop_reason'] = 0
source_table['refills'] = 0
source_table['days_supply'] = 0
source_table['sig'] = None
source_table['route_concept_id'] = 0
source_table['lot_number'] = 0
source_table['provider_id'] = 0
source_table['visit_detail_id'] = 0
source_table['drug_source_concept_id'] = 0
source_table['route_source_value'] = 0
source_table['dose_unit_source_value'] = 0


source_table['drug_exposure_start_date'] = pd.to_datetime(source_table['drug_exposure_start_datetime']).dt.date
source_table['drug_exposure_end_date'] = pd.to_datetime(source_table['drug_exposure_end_datetime']).dt.date


for index_row, row in source_table.iterrows():
    try:
        is_exist = False
        for lst in drugs_and_concepts_numbers:
            for elem in lst:
                if any(map(str.isdigit, elem)):
                    break
                elif len(elem) > 1:
                    # elem.lower() in row["Drug_Name"].lower():
                    if row["Drugs_Text"].find(elem) != -1:
                        row['drug_concept_id'] = int(lst[-1])
                        is_exist = True
                        break
                    else:
                        continue
                else:
                    continue
            if is_exist == True:
                break

        if is_exist == False:
            row['drug_concept_id'] = 0


        new_val = row["quantity"].split(' ')
        quantity = new_val[0]
        dose_unit = new_val[1]
        drug_name = row["Drugs_Text"]
        data.append([drug_exposure_id, row["person_id"], row['drug_concept_id'], row["drug_exposure_start_date"], row['drug_exposure_start_datetime'],
        row['drug_exposure_end_datetime'], row["drug_exposure_end_date"], row['verbatim_end_date'], row['refills'], row['drug_type_concept_id'], row['stop_reason'],quantity, row["days_supply"], row["sig"],
        row['route_concept_id'], row['lot_number'], row['provider_id'], row['visit_occurrence_id'], row['visit_detail_id'],
        drug_name, row['drug_source_concept_id'], row['route_source_value'],
        dose_unit])
        drug_exposure_id += 1
    except :
        print("e")
        continue

df_result_69 = pd.DataFrame(data, columns=["drug_exposure_id", "person_id", 'drug_concept_id',"drug_exposure_start_date",'drug_exposure_start_datetime','drug_exposure_end_datetime',"drug_exposure_end_date",'verbatim_end_date', 'refills',
'drug_type_concept_id', 'stop_reason', 'quantity', "days_supply", "sig",'route_concept_id','lot_number', 'provider_id', 'visit_occurrence_id', 'visit_detail_id', 'drug_source_value', 'drug_source_concept_id', 'route_source_value', 'dose_unit_source_value'])

source_table_doc.to_csv(r'C:\Users\ayalon\Desktop\data of project\data_white_rabbit\69.csv', encoding='utf-8', index=False)##musttttttttt


df_result = df_result.append(df_result_69, ignore_index=True)

# //___________________table 75________________________________________

source_table = pd.read_csv('75.csv')
data = []

source_table_doc = source_table.dropna(subset=['Stop_Date'])
source_table_doc = source_table_doc[["ID_BAZNAT", 'Event_baznat', "Drugs_Text", "DosageOrder", "Start_Date", "Stop_Date"]]

source_table = source_table.rename(columns={"ID_BAZNAT": "person_id", "Start_Date": "drug_exposure_start_datetime", "Stop_Date": "drug_exposure_end_datetime", 'Event_baznat':'visit_occurrence_id', "DosageOrder":"quantity"})
source_table = source_table.dropna(subset=['drug_exposure_end_datetime'])
source_table = source_table[["person_id", "Drugs_Text", "drug_exposure_start_datetime", "drug_exposure_end_datetime", "visit_occurrence_id","quantity"]]

source_table['drug_concept_id'] = 0
source_table['drug_source_value'] = ""
source_table["days_supply"] = 0
source_table['drug_exposure_id'] = 0

source_table['verbatim_end_date'] = None
source_table['drug_type_concept_id'] = 32829  ## EHR inpatient note
source_table['stop_reason'] = 0
source_table['refills'] = 0
source_table['days_supply'] = 0
source_table['sig'] = None
source_table['route_concept_id'] = 0
source_table['lot_number'] = 0
source_table['provider_id'] = 0
source_table['visit_detail_id'] = 0
source_table['drug_source_concept_id'] = 0
source_table['route_source_value'] = 0
source_table['dose_unit_source_value'] = 0


source_table['drug_exposure_start_date'] = pd.to_datetime(source_table['drug_exposure_start_datetime']).dt.date
source_table['drug_exposure_end_date'] = pd.to_datetime(source_table['drug_exposure_end_datetime']).dt.date


for index_row, row in source_table.iterrows():
    try:
        is_exist = False
        for lst in drugs_and_concepts_numbers:
            for elem in lst:
                if any(map(str.isdigit, elem)):
                    break
                elif len(elem) > 1:
                    # elem.lower() in row["Drug_Name"].lower():
                    if row["Drugs_Text"].find(elem) != -1:
                        row['drug_concept_id'] = int(lst[-1])
                        is_exist = True
                        break
                    else:
                        continue
                else:
                    continue
            if is_exist == True:
                break

        if is_exist == False:
            row['drug_concept_id'] = 0

        new_val = row["quantity"].split(' ')
        quantity = new_val[0]
        dose_unit = new_val[1]
        drug_name = row["Drugs_Text"]
        data.append([drug_exposure_id, row["person_id"], row['drug_concept_id'], row["drug_exposure_start_date"], row['drug_exposure_start_datetime'],
        row['drug_exposure_end_datetime'], row["drug_exposure_end_date"], row['verbatim_end_date'], row['refills'], row['drug_type_concept_id'], row['stop_reason'],quantity, row["days_supply"], row["sig"],
        row['route_concept_id'], row['lot_number'], row['provider_id'], row['visit_occurrence_id'], row['visit_detail_id'],
        drug_name, row['drug_source_concept_id'], row['route_source_value'],
        dose_unit])
        drug_exposure_id += 1
    except :
        print("e")
        continue


df_result_75 = pd.DataFrame(data, columns=["drug_exposure_id", "person_id", 'drug_concept_id',"drug_exposure_start_date",'drug_exposure_start_datetime','drug_exposure_end_datetime',"drug_exposure_end_date",'verbatim_end_date', 'refills',
'drug_type_concept_id', 'stop_reason', 'quantity', "days_supply", "sig",'route_concept_id','lot_number', 'provider_id', 'visit_occurrence_id', 'visit_detail_id', 'drug_source_value', 'drug_source_concept_id', 'route_source_value', 'dose_unit_source_value'])

source_table_doc.to_csv(r'C:\Users\ayalon\Desktop\data of project\data_white_rabbit\75.csv', encoding='utf-8', index=False)##musttttttttt


# df_result = df_result.append(df_result_75, ignore_index=True)

# //___________________table 82________________________________________

source_table = pd.read_csv('82.csv')
data = []

source_table_doc = source_table.dropna(subset=['Stop_Date'])
source_table_doc = source_table_doc[["ID_BAZNAT", 'Event_baznat', "Drugs_Text", "DosageOrder", "Start_Date", "Stop_Date"]]

source_table = source_table.rename(columns={"ID_BAZNAT": "person_id", "Start_Date": "drug_exposure_start_datetime", "Stop_Date": "drug_exposure_end_datetime", 'Event_baznat':'visit_occurrence_id', "DosageOrder":"quantity"})
source_table = source_table.dropna(subset=['drug_exposure_end_datetime'])
source_table = source_table[["person_id", "Drugs_Text", "drug_exposure_start_datetime", "drug_exposure_end_datetime", "visit_occurrence_id","quantity"]]

source_table['drug_concept_id'] = 0
source_table['drug_source_value'] = ""
source_table["days_supply"] = 0
source_table['drug_exposure_id'] = 0

source_table['verbatim_end_date'] = None
source_table['drug_type_concept_id'] = 32829  ## EHR inpatient note
source_table['stop_reason'] = 0
source_table['refills'] = 0
source_table['days_supply'] = 0
source_table['sig'] = None
source_table['route_concept_id'] = 0
source_table['lot_number'] = 0
source_table['provider_id'] = 0
source_table['visit_detail_id'] = 0
source_table['drug_source_concept_id'] = 0
source_table['route_source_value'] = 0
source_table['dose_unit_source_value'] = 0


source_table['drug_exposure_start_date'] = pd.to_datetime(source_table['drug_exposure_start_datetime']).dt.date
source_table['drug_exposure_end_date'] = pd.to_datetime(source_table['drug_exposure_end_datetime']).dt.date


for index_row, row in source_table.iterrows():
    try:
        is_exist = False
        for lst in drugs_and_concepts_numbers:
            for elem in lst:
                if any(map(str.isdigit, elem)):
                    break
                elif len(elem) > 1:
                    # elem.lower() in row["Drug_Name"].lower():
                    if row["Drugs_Text"].find(elem) != -1:
                        row['drug_concept_id'] = int(lst[-1])
                        is_exist = True
                        break
                    else:
                        continue
                else:
                    continue
            if is_exist == True:
                break

        if is_exist == False:
            row['drug_concept_id'] = 0

        new_val = row["quantity"].split(' ')
        quantity = new_val[0]
        dose_unit = new_val[1]
        drug_name = row["Drugs_Text"]
        data.append([drug_exposure_id, row["person_id"], row['drug_concept_id'], row["drug_exposure_start_date"], row['drug_exposure_start_datetime'],
        row['drug_exposure_end_datetime'], row["drug_exposure_end_date"], row['verbatim_end_date'], row['refills'], row['drug_type_concept_id'], row['stop_reason'], quantity, row["days_supply"], row["sig"],
        row['route_concept_id'], row['lot_number'], row['provider_id'], row['visit_occurrence_id'], row['visit_detail_id'],
        drug_name, row['drug_source_concept_id'], row['route_source_value'],
        dose_unit])
        drug_exposure_id += 1
    except :
        print("e")
        continue

df_result_82 = pd.DataFrame(data, columns=["drug_exposure_id", "person_id", 'drug_concept_id',"drug_exposure_start_date",'drug_exposure_start_datetime','drug_exposure_end_datetime',"drug_exposure_end_date",'verbatim_end_date', 'refills',
'drug_type_concept_id', 'stop_reason', 'quantity', "days_supply", "sig",'route_concept_id','lot_number', 'provider_id', 'visit_occurrence_id', 'visit_detail_id', 'drug_source_value', 'drug_source_concept_id', 'route_source_value', 'dose_unit_source_value'])

source_table_doc.to_csv(r'C:\Users\ayalon\Desktop\data of project\data_white_rabbit\82.csv', encoding='utf-8', index=False)##musttttttttt


df_result = df_result.append(df_result_82, ignore_index=True)


df_result.to_csv(r'C:\Users\ayalon\Desktop\data of project\data_white_rabbit\drug_exposure.csv', encoding='utf-8', index=False)##musttttttttt
