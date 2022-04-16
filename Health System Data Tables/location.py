# Location
#
# Parameters:
#
# Tables:
#
#  OMP table - locaion

import pandas as pd

data=[]
#Ein Kerem
location_id = 1
address_1=''
address_2=''
city='Jerusalem'
state=''
zip=''
county = 'Israel'
location_source_value=''
country_concept_id=41995088 #source value of israel
country_source_value='Israel'
latitude=''
longitude=''
data.append([location_id ,address_1,address_2,city,state,zip,county,location_source_value,country_concept_id,country_source_value,latitude,longitude])

#Har HaTsofim
location_id = 2
address_1=''
address_2=''
city='Jerusalem'
state=''
zip=''
county = 'Israel'
location_source_value=''
country_concept_id=''
country_source_value=''
latitude=''
longitude=''
data.append([location_id ,address_1,address_2,city,state,zip,county,location_source_value,country_concept_id,country_source_value,latitude,longitude])

df_result = pd.DataFrame(data, columns=['location_id' ,'address_1','address_2','city','state','zip','county,location_source_value','country_concept_id','country_source_value','latitude,longitude'])
df_result.to_csv('location.csv', encoding='utf-8', index=False)
