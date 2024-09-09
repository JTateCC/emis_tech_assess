from scripts import json_extraction, database_population
from db.models import *
from pathlib import Path
import os

def main():
    directory_path = os.path.join(Path.cwd() / 'data')
    all_resource_dataframes = json_extraction.extract_all_json_to_dataframes(directory_path)
    df_encounter = all_resource_dataframes['Encounter']
    df_encounter = df_encounter.drop('resourceType', axis=1)

    db_url = 'postgresql+pg8000://admin:emistest!@postgres:5432/emis'
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    database_population.insert_dataframe_to_db(session, df_encounter, Encounter)
