import pandas as pd
from googletrans import Translator
import numpy as np
from datetime import timedelta



df_43 = pd.read_excel(r'43.xlsx')
df_58 = pd.read_excel(r'58.xlsx')
df_78 = pd.read_excel(r'78.xlsx')
df_85 = pd.read_excel(r'85.xlsx')

df_57 = pd.read_excel(r'57.xlsx')
df_69 = pd.read_excel(r'69.xlsx')
df_75 = pd.read_excel(r'75.xlsx')
df_82 = pd.read_excel(r'82.xlsx')


df_57.drop('Event_baznat.1', inplace=True, axis=1)
frames = [df_58, df_78, df_85]
frames_2 = [df_57, df_69, df_75, df_82]



result = pd.concat(frames)
result2 = pd.concat(frames_2)
result2['days_supply'] = 0
result2 = result2.dropna(subset=['Stop_Date'])
result2_for_doctors = result2

# print(result2.shape[0])

result_43 = df_43.rename(columns={"שם תרופה":"Drug_Name", 'מינון':"quantity",'אופן מתן':"sig" })
result = result.rename(columns={"שם תרופה":"Drug_Name", 'מינון':"quantity",'אופן מתן':"sig","למשך":"days_supply","Record_Date":"drug_exposure_start_date","ID_BAZNAT": "person_id"})
result2_for_doctors = result2_for_doctors.rename(columns={"Drugs_Text": "Drug_Name"})
result2 = result2.rename(columns={"ID_BAZNAT": "person_id", "Start_Date": "drug_exposure_start_date", "Stop_Date": "drug_exposure_end_date" })


def isfloat(num):
    try:
        float(num)
        return True

    except ValueError:
        return False


def is_precent(num):
    try:
        if "%" in num or "/" in num:
            return True
        else:
            return False
    except ValueError:
        return False





result_for_doctors = result[["Drug_Name"]]##one table that i n eed to saend to doctors
result2_for_doctors = result2_for_doctors[["Drug_Name"]]
print(result2_for_doctors)
frame_3 = [result_for_doctors, result2_for_doctors]
unit_tables = pd.concat(frame_3)
lst_of_drugs = []
drug = ""
for index, row in unit_tables.iterrows():
    lst_of_drugs = str(row['Drug_Name']).split(" ")
    for elem in lst_of_drugs:
        if (elem.isdigit() == False or isfloat(elem) == False or is_precent(elem) == False ):
            drug = drug + " " + elem

        else:
            unit_tables.loc[index, 'Drug_Name'] = drug
            drug = ""
            lst_of_drugs = []

            break

result_for_table = result[["person_id", "Drug_Name", "quantity", "sig", "days_supply", "drug_exposure_start_date"]]





group_by_drug_name = unit_tables.groupby(['Drug_Name']).size().reset_index(name='counts')
# print(group_by_drug_name.head(10))
group_by_drug_name = group_by_drug_name.sort_values(by=['counts'], ascending=False) ##table to send to doctors
# print(group_by_drug_name.head(10))

# group_by_drug_name.to_excel(r'C:\Users\ayalon\Desktop\drugs_names1`.xlsx')##musttttttttt


result_for_table_drop_na = result_for_table.dropna()


for index, row in result_for_table_drop_na.iterrows():
    try:
        en_text = ''
        split_words = row['days_supply'].split(' ')
        if len(split_words) == 11:
            if split_words[10] == 'שבועות':
                en_text = split_words[9]+' weeks'
            elif split_words[10] == 'חודשים' or split_words[10] == 'חודש':
                en_text = split_words[9] + ' months'
            else:
                en_text = split_words[9] + ' days'
        else:
            if split_words[9] == 'שבועות':
                en_text = split_words[8]+' weeks'
            elif split_words[9] == 'חודשים' or split_words[9] == 'חודש':
                en_text = split_words[8] + ' months'
            else:
                en_text = split_words[8] + ' days'
        result_for_table_drop_na.loc[index, 'days_supply'] = en_text

    except:

        continue
counter = 0
for index, row in result_for_table_drop_na.iterrows():
    try:
        new_value = 0
        string_date = str(row['days_supply'])
        split_words = string_date.split(' ')
        if split_words[1] == "days":
            new_value = split_words[0]
            counter += 1
        elif split_words[1] == "weeks":
            new_value = int(split_words[0])*7
            new_value = str(new_value)
            counter += 1
        else:
            new_value = int(split_words[0])*30
            new_value = str(new_value)
            counter += 1
        result_for_table_drop_na.loc[index, 'days_supply'] = new_value
    except:

        continue


data = []
data1 = []
drug_exposure_id = ''


new_df = result_for_table_drop_na
new_df["drug_exposure_end_date"] = ""
new_df["drug_exposure_end_date"] = np.nan
new_df['drug_exposure_id'] = 0
new_df['drug_concept_id'] = 0
new_df['drug_exposure_start_datetime'] = 0
new_df['drug_exposure_end_datetime'] = 0
new_df['verbatim_end_date'] = 0
new_df['drug_type_concept_id'] = 32838 ## EHR prescription
new_df['stop_reason'] = 0
new_df['refills'] = 0

new_df['route_concept_id'] = 0
new_df['lot_number'] = 0
new_df['provider_id'] = 0
new_df['visit_occurrence_id'] = 0
new_df['visit_detail_id'] = 0
new_df['drug_source_value'] = 0
new_df['drug_source_concept_id'] = 0
new_df['route_source_value'] = 0
new_df['dose_unit_source_value'] = 0


result2['drug_exposure_id'] = 0
result2['drug_concept_id'] = 0
result2['drug_exposure_start_datetime'] = 0
result2['drug_exposure_end_datetime'] = 0
result2['verbatim_end_date'] = 0
result2['drug_type_concept_id'] = 32829 ## EHR inpatient note
result2['stop_reason'] = 0
result2['refills'] = 0
result2['quantity'] = 0
result2['days_supply'] = 0
result2['sig'] = 0
result2['route_concept_id'] = 0
result2['lot_number'] = 0
result2['provider_id'] = 0
result2['visit_occurrence_id'] = 0
result2['visit_detail_id'] = 0
result2['drug_source_value'] = 0
result2['drug_source_concept_id'] = 0
result2['route_source_value'] = 0
result2['dose_unit_source_value'] = 0





counter = 1
for index, row in new_df.iterrows():
    try:
        end_date = row["drug_exposure_start_date"] + timedelta(days=int(row['days_supply']))
        data.append([counter, row["person_id"], row['drug_concept_id'], row["drug_exposure_start_date"], row['drug_exposure_start_datetime'],
        row['drug_exposure_end_datetime'], end_date, row['verbatim_end_date'], row['refills'], row['drug_type_concept_id'], row['stop_reason'],row['quantity'], row["days_supply"], row["sig"],
        row['route_concept_id'], row['lot_number'], row['provider_id'], row['visit_occurrence_id'], row['visit_detail_id'],
        row['drug_source_value'], row['drug_source_concept_id'], row['route_source_value'],
        row['dose_unit_source_value']])
        counter += 1
    except :
        print("e")

counter = 4759
for index, row in result2.iterrows():
    try:

        data1.append([counter, row["person_id"], row['drug_concept_id'], row["drug_exposure_start_date"], row['drug_exposure_start_datetime'],
        row['drug_exposure_end_datetime'], row["drug_exposure_end_date"], row['verbatim_end_date'], row['refills'], row['drug_type_concept_id'], row['stop_reason'], row['quantity'], row["days_supply"], row["sig"],
        row['route_concept_id'], row['lot_number'], row['provider_id'], row['visit_occurrence_id'], row['visit_detail_id'],
        row['drug_source_value'], row['drug_source_concept_id'], row['route_source_value'],
        row['dose_unit_source_value']])
        counter += 1
    except :
        print("e")
print(counter)



final_result = pd.DataFrame(data, columns=["drug_exposure_id", "person_id", 'drug_concept_id',"drug_exposure_start_date",'drug_exposure_start_datetime','drug_exposure_end_datetime',"drug_exposure_end_date",'verbatim_end_date', 'refills',
'drug_type_concept_id', 'stop_reason', 'quantity', "days_supply", "sig",'route_concept_id','lot_number', 'provider_id', 'visit_occurrence_id', 'visit_detail_id', 'drug_source_value', 'drug_source_concept_id', 'route_source_value', 'dose_unit_source_value'])


final_result1 = pd.DataFrame(data1, columns=["drug_exposure_id", "person_id", 'drug_concept_id',"drug_exposure_start_date",'drug_exposure_start_datetime','drug_exposure_end_datetime',"drug_exposure_end_date",'verbatim_end_date', 'refills',
'drug_type_concept_id', 'stop_reason', 'quantity', "days_supply", "sig",'route_concept_id','lot_number', 'provider_id', 'visit_occurrence_id', 'visit_detail_id', 'drug_source_value', 'drug_source_concept_id', 'route_source_value', 'dose_unit_source_value'])


final_result2 = pd.concat([final_result, final_result1])

final_result2.to_excel(r'C:\Users\ayalon\Desktop\drug_data.xlsx')##musttttttttt




# print(counter)
# print(new_df.End_Date.to_string(index=False))
# print(new_df.drug_exposure_id.to_string(index=False))

