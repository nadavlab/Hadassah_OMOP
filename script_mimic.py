
import pandas as pd
from sqlalchemy import create_engine , text
import os


user = 'postgres'
password = 'ayalonA3'
hostname = '132.72.65.168'
database_name = 'Hadassah'

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{hostname}/{database_name}', echo=True)

path = r'C:\Users\ayalon\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\home\ayalonaz\mimic-omop\1_omop_data_csv'
files = os.listdir(path)

for file in files:
    if file.endswith('sql'):continue
    df = pd.read_csv(f'{path}/{file}',low_memory=False)

    try:
        table_name = file[:-4]
        l = [x for x in df.keys() if  df[x].dtype.name == 'int64']
        with engine.connect() as conn :
            for c in l:
               conn.execute(text(f'ALTER TABLE mimic.{table_name} ALTER COLUMN {c} SET DATA TYPE BIGINT;'))

        df.to_sql(file[:-4],index=False, con=engine, schema='mimic', if_exists='append')
    except Exception as e:
        print(e)

