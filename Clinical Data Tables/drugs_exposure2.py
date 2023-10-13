import argparse
import pandas as pd
#from googletrans import Translator
import numpy as np
from datetime import timedelta, datetime , date
import re
import sys
import os
import warnings
from collections import defaultdict

'''
Execute:
python3 ./Hadassah_OMOP/Clinical\ Data\ Tables/drugs_exposure2.py 31 43 44 57 69 75 82 58 78 85 > drugs_exposure2_2023_10_09.log 2>&1
Took about 30 minutes.
Then upload using:
BEGIN; \COPY omop_demo.drug_exposure FROM '/tmp/drug_exposure.tsv' with delimiter E'\t' CSV header;
ROLLBACK; BEGIN; \COPY omop_demo.drug_exposure FROM '/tmp/drug_exposure.tsv' with delimiter E'\t' CSV header;


SELECT drug_exposure_id, count(*) FROM omop_demo.drug_exposure GROUP BY drug_exposure_id HAVING COUNT(*) > 1 ORDER BY COUNT(*) DESC;
'''

OMOP_SOURCE_DIR = '/Users/nadavrap/Dropbox (BGU)/Documents/Students/Hadassah_OBGYN/' # './'
ORG_SOURCE_DIR = OMOP_SOURCE_DIR + 'CSVs/'
OUT_DIR = '/tmp/'


route2concept = {
    "ORAL": 4132161,
    "VAGIN": 4057765, #Vaginal route
    "I.M": 4302612, # Intramuscular route,
    "S.C": 4142048, # Subcutaneous route	
    "RESPIR": 40486069,
    "I.V": 4171047,
    "CUTAN": 40490507,
    "RECTAL": 4290759,
    "S.L": 4292110,
    "DERMAL": 4262099, # Transdermal route
    "OPHTALM": 4263689, # Topical route
    "P.G": 4132161,
    "TOPIC": 4263689,
    "PERCUT": 4177987,
    "INJ-NOT-IV": 4302612, #Intramuscular route
    "NASAL": 4262914,
    "P.J": 4132161, #Levothyroxine
    "OTIC-HAD": 4023156, # CILOXAN
    "OTIC": 4023156,
    "NA's": None,
    "I.V DRIP": 4171047,  #IV
    "I.V-SLOW": 4171047,
    "X-CORPOR": 37018288, #	Extracorporeal route
     "INTRAGLUTEALLY": 4302612, #	Intramuscular route
     "C.L": 0, 
    "EPIDUR": 4225555, # Epidural route
    "P.Z": 4132161,
    "I.V BOLUS": 4171047,  #IV
    "ORO": 4132161, #Oral
     "I-ARTIC": 4006860, # Intra-articular route,
     "I.T": 4302612, # Intramuscular route
     "CONJUNC": 40486444, # Conjunctival route,
     "I-UTER": 4269621, # Intrauterine route
    "I-AMNI": 4163767, # Intraamniotic route
    "I-OCUL": 4157760, # Intraocular route
    "NB-PERIPH": 4262099, # Transdermal route
    "TOPICAL--SCALP": 4263689, # Topical route
    '': None,
    np.nan: None
}

person_table = pd.read_csv(OMOP_SOURCE_DIR + 'person.csv')
visit_occurrence_table = pd.read_csv(OMOP_SOURCE_DIR + 'visit_occurrence.csv')
visit_detail_table = pd.read_csv(OMOP_SOURCE_DIR + 'visit_detail.csv')
visit_detail_table['visit_detail_start_datetime'] = pd.to_datetime(visit_detail_table['visit_detail_start_datetime'])
visit_detail_table['visit_detail_end_datetime'] = pd.to_datetime(visit_detail_table['visit_detail_end_datetime'])

#concepts_table = pd.read_csv(OUT_DIR + 'concept_snomed.csv')

# sourceCode,sourceName,sourceFrequency,sourceAutoAssignedConceptIds,matchScore,mappingStatus,equivalence,statusSetBy,
# statusSetOn,conceptId,conceptName,domainId,mappingType,comment,createdBy,createdOn,assignedReviewer
source_to_concept_table = pd.read_csv(OMOP_SOURCE_DIR + 'drugs_mapping.csv')
#source_to_concept_table = source_to_concept_table[source_to_concept_table['mappingStatus'] == 'APPROVED'][["sourceName", "conceptId"]]
source_to_concept_dict = defaultdict(list)
for index, row in source_to_concept_table.iterrows():
    source_to_concept_dict[row['source_code']].append(row['target_concept_id'])

#drug_names = pd.read_csv(OUT_DIR + 'drugs_names.csv')
#drug_cols = drug_names.columns
drugs_and_concepts_numbers = []

""" def change_code_to_id(code):
    code=int(code)
    match_concepts = concepts_table.loc[concepts_table['concept_code'] == code]
    if match_concepts.shape[0] > 0:
        concept_id = match_concepts.values[0][0]
        return concept_id
    else:
        warnings.warn(f"Could not find a concept id matching code {code}")
 """

def source_to_concept(source):
    '''
    Map source value to concept id (there are no codes for drugs).
    If no mapping exists, raise a warning and return zero.
    One source value can be mapped to more than one concept.
    '''
    if source in source_to_concept_dict:
        return source_to_concept_dict[source]
    else:
        warnings.warn(f"Source: {source} - could not find a concept id.")
        return [0]


""" for drug_text in drug_cols:
    if drug_text == "Drug_Name" or drug_text == "counts":
        continue
    else:
        names_and_concept_list = re.findall(r'\w+', drug_text)
        concept_id = change_code_to_id(names_and_concept_list[-1])
        names_and_concept_list[-1]=str(concept_id)
        drugs_and_concepts_numbers.append(names_and_concept_list)
 """


def is_exist_visit_occurrence_id(event_baznat):
    match_visit_occurrence = visit_occurrence_table.loc[visit_occurrence_table['visit_occurrence_id'] == event_baznat]
    if match_visit_occurrence.shape[0] > 0:
        return event_baznat
    else:
        return ''


def is_exist_person_id(id_baznat):
    match_person = person_table.loc[person_table['person_id'] == id_baznat]
    if match_person.shape[0] > 0:
        return True
    else:
        return False

def is_exist_visit_detail(id_baznat,record_date):
    match_visit_detail = visit_detail_table.loc[visit_detail_table['visit_occurrence_id'] == id_baznat]
    index_visit_detail = 0

    if match_visit_detail.shape[0] > 0:
        while match_visit_detail.values.shape[0]>index_visit_detail:
            date_start_vd = datetime.strptime(match_visit_detail.values[index_visit_detail][4], '%Y-%m-%d %H:%M:%S')
            date_end_vd = datetime.strptime(match_visit_detail.values[index_visit_detail][6], '%Y-%m-%d %H:%M:%S')
            start_date = datetime.strptime(record_date, "%Y-%m-%dT%H:%M:%S")
            if date_start_vd <= start_date and start_date <= date_end_vd :
                return match_visit_detail.values[index_visit_detail][0]
            index_visit_detail += 1
    else:
        return ''


def get_days_supply(str):
    if pd.isnull(str):
        return None
    nums = re.findall(r'\d+', str)
    if len(nums) == 0:
        raise Exception(f'No duration number found in {str}')
    elif len(nums) > 1:
        raise Exception(f'Multiple number may be the duration in {str}')
    duration = int(nums[0])

    if 'שבועות' in str or 'week' in str:
        duration = duration * 7
    elif 'חודש' in str or 'month' in str:
        duration = duration * 30
    return duration

def get_colname(col, columns, prefix):

    match col:
        case 'drug':
            source_cols = ("Drugs_Text", "שם הוראה", "שם תרופה", 'Description_Text') # "Generic_Name"
        case 'startdatetime':
            source_cols = ("Start_Date",'Record_Date')
        case 'enddatetime':
            source_cols = ("End_Date",)
        case 'quantity':
            source_cols = ('מינון', 'DosageOrder')
        case 'supply':
            source_cols = ('למשך', )
        case 'route':
            source_cols = ('אופן מתן', 'Way_Of_Giving')
        case _:
            return None

    is_equal = [i in source_cols for i in columns]
    if not any(is_equal):
        warnings.warn(f"File {prefix} has no column for {col}.")
        return None
    if sum(is_equal) > 1:
        if prefix in ('57', '69', '75', '82') and col == 'startdatetime': # These files have the same structure with next date fields: Date_Planned, Date, Start_Date, Record_Date
            return ['Record_Date']
        raise Exception(f"File {prefix} has more than single column for {col}.")
    source_col = columns[is_equal]
    return(source_col)


def get_visit_occrrence(person_id, visit_occurrence_id):
    vot = visit_occurrence_table[visit_occurrence_table['person_id'] == person_id]
    if not vot.size:
        warnings.warn(f'Person id {person_id} not found in visit_occurrence table.')
        return None
    vot = vot[vot['visit_occurrence_id'] == visit_occurrence_id]
    if not vot.size:
        warnings.warn(f'visit_occurrence_id {visit_occurrence_id} not found in visit_occurrence table for person id {person_id}.')
        return None
    return vot


def get_visit_detail(person_id, visit_occurrence_id, datetime):
    '''
    Look for the visit_detail_id based on person id, visit occurrence id and datetime
    If not found, return None
    '''
    vot = get_visit_occrrence(person_id, visit_occurrence_id)
    vdt = visit_detail_table[visit_detail_table['person_id'] == person_id]
    if not vdt.size:
        warnings.warn(f'Person id {person_id} not found in visit_detail_table table.')
        return None
    vdt = vdt[vdt['visit_occurrence_id'] == visit_occurrence_id]
    if not vdt.size:
        warnings.warn(f'visit_occurrence_id {visit_occurrence_id} not found in visit_detail_table table for person id {person_id}.')
        return None
    
    for i, r in vdt.iterrows():
        if r['visit_detail_start_datetime'] <= datetime and datetime <= r['visit_detail_end_datetime']:
            return r['visit_detail_id']
    return None


def parse_file(prefix):
    '''
    16 - תינוקות - הוראות לתרופות
    30 - מיון מיילדותי - קבלה - תרופות שלא במאגר
    31 - Not 30
    32 - מיון מיילדותי - קבלה - תרופות קבועות - Free text for drugs and reason and diagnosis - all mixed.
    # 34 - מיון מיילדותי - קבלה - רגישות לתרופות
    42 - מיון מיילדותי - הריון נוכחי - תרופות מיוחדות
    43 - מיון מיילדותי - הריון נוכחי - תרופות במהלך ההריון
    44 - מיון מיילדותי - הריון נוכחי - תרופות במהלך ההריון שלא במאגר
    
    57 - מיון מיילדותי - סיכום והוראות - Medication Orders
    58 - מיון מיילדותי - סיכום והוראות - תרופות מומלצות
    69 - חדר לידה - מהלך לידה - Medication Orders
    75 - יולדות - אשפוז - Medications orders
    78 - יולדות - שחרור - תרופות מומלצות
    82 - סיבוכי הריון - אשפוז - Medications Orders
    85 - סיבוכי הריון - שחרור - תרופות מומלצות

    '''
    columns_58={"שם תרופה":"Drug_Name","למשך":"days_supply","Record_Date":"drug_exposure_start_datetime",
            "ID_BAZNAT": "person_id",'Event_baznat':'visit_occurrence_id',"מינון":"quantity"}

    '''Drug type concept id
    Delineate between prescriptions written vs. prescriptions dispensed (32825) vs. medication history vs. patient-reported exposure (32865), etc.
    '''
    if prefix in ('16', '58', '78', '85'):
        drug_type_concept_id = 32838  ## EHR prescription
    elif prefix in ('57', '69', '75', '82'):
        drug_type_concept_id = 32829  ## EHR inpatient note
    elif prefix in ('31', '32', '42', '43', '44'):
        drug_type_concept_id = 32865  ## Patient self-report

    refills = None # pd.na
    stop_reason = None
    lot_number = None
    provider_id = None
    drug_source_concept_id = None

    source_table = pd.read_csv(ORG_SOURCE_DIR + prefix + '.csv')
    data = []

    drug_source_col = get_colname('drug', source_table.columns, prefix)
    start_date_col = get_colname('startdatetime', source_table.columns, prefix)
    source_table['start_datetime'] = pd.to_datetime(source_table[start_date_col].iloc[:, 0])
    source_table['start_date'] = source_table['start_datetime'].dt.date
    end_date_col = get_colname('enddatetime', source_table.columns, prefix)
    if end_date_col:
        source_table['end_datetime'] = pd.to_datetime(source_table[end_date_col].iloc[:, 0])
        source_table['end_date'] = source_table['end_datetime'].dt.date

    quantity_col = get_colname('quantity', source_table.columns, prefix)
    quantity = np.nan
    dose_unit_source_value = pd.NA

    supply_col = get_colname('supply', source_table.columns, prefix)

    route_col = get_colname('route', source_table.columns, prefix)

    for index_row, row in source_table.iterrows():
        person_id = row['ID_BAZNAT']

        drug_source_value = row[drug_source_col].item()
        drug_concept_ids = source_to_concept(drug_source_value)
        #if not np.isnan(drug_source_value):
        if type(drug_source_value) == type(''):
            drug_source_value = re.sub(r'\n', ' ', drug_source_value)
            if not np.any(drug_concept_ids):
                drug_concept_ids = source_to_concept(drug_source_value)

        if (drug_concept_ids[0] == 0 and "Generic_Name" in row and row["Generic_Name"] in source_to_concept_dict):
            drug_source_value = row["Generic_Name"]
            source_to_concept(drug_source_value)
            drug_concept_ids = "Generic_Name"

        visit_occurrence_id = row['Event_baznat']
        if pd.isnull(row['start_date']) and prefix == '85': # No start date, and source table is drugs from discharge orders.
            vot = get_visit_occrrence(person_id, visit_occurrence_id)
            if not vot.empty:
                row['start_datetime'] = datetime.strptime(vot['visit_end_datetime'].item(), '%Y-%m-%d %H:%M:%S')
                row['start_date'] = row['start_datetime'].date()
                
        quantity = None
        dose_unit_source_value = None
        if not quantity_col is None and not quantity_col.empty:
            quantity = row[quantity_col].item()
            if quantity and type(quantity) == type(''):
                vals = quantity.split()
                if re.search('\d', vals[0]):
                    quantity = float(vals[0])
                    if len(vals) > 1:
                        dose_unit_source_value = vals[1]
                    else:
                        dose_unit_source_value = row[quantity_col].item()
                else:
                    quantity = ''
                    dose_unit_source_value = vals[0]

        if supply_col is None:
            days_supply = None
        else:           
            days_supply = get_days_supply(row[supply_col].item())

        if end_date_col: # and not end_date_col.empty:
            end_date = row['end_date']
            end_datetime = row['end_datetime']
            verbatim_end_date = row['end_date_col']
        elif days_supply:
            time_to_add = timedelta(days=days_supply)
            end_date = row['start_date'] + time_to_add
            end_datetime = row['start_datetime'] + time_to_add
            verbatim_end_date = None
        else:
            end_date = row['start_date']
            end_datetime, verbatim_end_date = (None, None)
        if days_supply:
            days_supply = str(days_supply)

        sig = ' '.join([re.sub(r'\n', ' ', str(x)) for x in row.values]) # row # This is the verbatim instruction for the drug as written by the provider.

        if route_col is None:
            route_source_value = None
            route_concept_id = None
        else:
            route_source_value = row[route_col].item()
            route_concept_id = route2concept[route_source_value]
            if route_concept_id:
                route_concept_id = str(route_concept_id) # Without it, it is stored as float.


        visit_detail_id = get_visit_detail(person_id, visit_occurrence_id, datetime=row['start_datetime'])
        if visit_detail_id:
            visit_detail_id = str(visit_detail_id)

        # One drug can be mapped to more than one concept
        for drug_concept_id in drug_concept_ids:
            data.append([parse_file.drug_exposure_id, person_id,  drug_concept_id, 
                        row['start_date'], row['start_datetime'], 
                        end_date, end_datetime, verbatim_end_date,
                        drug_type_concept_id,
                        stop_reason, refills,
                        quantity, days_supply, sig,
                        route_concept_id, lot_number, provider_id, visit_occurrence_id,
                        visit_detail_id,
                        drug_source_value, drug_source_concept_id, route_source_value,
                        dose_unit_source_value])

            parse_file.drug_exposure_id += 1

    data = pd.DataFrame(data, columns=["drug_exposure_id", "person_id", 'drug_concept_id',"drug_exposure_start_date",'drug_exposure_start_datetime',
                                       'drug_exposure_end_datetime',"drug_exposure_end_date",'verbatim_end_date', 
                                       'drug_type_concept_id', 'stop_reason', 'refills',
                                       'quantity', "days_supply", "sig",'route_concept_id','lot_number', 'provider_id', 'visit_occurrence_id',
                                       'visit_detail_id', 'drug_source_value', 'drug_source_concept_id', 'route_source_value', 'dose_unit_source_value'])
    data.to_csv(f'{OUT_DIR}drug_exposure_{prefix}.csv', encoding='utf-8', index=False, sep='\t')
    print(f'End table {prefix} with %i rows and %i col' % data.shape)
    return data

parse_file.drug_exposure_id = 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('prefixes', metavar='N', type=str, nargs='+',
                    help='Drug tables to parse', default=['43', '44', '57', '69', '75', '82', '58', '78', '85'])
    args = parser.parse_args()

    df_result = pd.DataFrame([], columns=["drug_exposure_id", "person_id", 'drug_concept_id',
                                            "drug_exposure_start_date",'drug_exposure_start_datetime',
                                            'drug_exposure_end_datetime',"drug_exposure_end_date", 'verbatim_end_date',
                                            'drug_type_concept_id', 'stop_reason', 'refills', 
                                            'quantity', "days_supply", "sig",
                                            'route_concept_id','lot_number', 'provider_id', 'visit_occurrence_id',
                                            'visit_detail_id', 'drug_source_value', 'drug_source_concept_id', 'route_source_value', 'dose_unit_source_value'])
    #df_result['route_concept_id'] = df_result['route_concept_id'].astype(int)

    """ for prefix in (#'16', # 16 is stop and expiration order for drugs 
        '31', 
        # '32', - Free text for drugs and reason and diagnosis - all mixed.
        # '42', - A questionair for 4 group of drugs.
        '43', '44', '57', '69', '75', '82', '58', '78', '85'
        ): """
    for prefix in args.prefixes:
        print(f'=============={prefix}===============')
        data = parse_file(prefix)
        #df_result = df_result.append(df_result_85, ignore_index=True)
        df_result = pd.concat([df_result, data], ignore_index=True)

    #df_result['route_concept_id'] = df_result['route_concept_id'].astype(int)

    df_result.to_csv(OUT_DIR + r'drug_exposure.csv', encoding='utf-8', index=False)##musttttttttt
    df_result.to_csv(f'{OUT_DIR}drug_exposure.tsv', encoding='utf-8', index=False, sep='\t')


    # //___________________table 58________________________________________
    # //___________________table 78________________________________________
    # //___________________table 85________________________________________
    # //___________________table 57________________________________________
    # //___________________table 69________________________________________
    # //___________________table 75________________________________________
    # //___________________table 82________________________________________

if __name__ == "__main__":
    #data = parse_file('44')
    main()
