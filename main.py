from pathlib import Path
import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scripts import json_extraction, database_population, dataframe_cleanup
import db.models as models
from tqdm import tqdm

# this serves as the entry point and performs the full routine of creating tables, extracting json and inserting into dh

def main():
    engine = create_engine(get_db_url())
    models.Base.metadata.create_all(engine)
    all_resource_dataframes = json_extraction.extract_all_json_to_dataframes(os.path.join(Path.cwd() / 'data'))
    clean_dataframes(all_resource_dataframes)
    populate_database(engine, all_resource_dataframes)

def clean_dataframes(dataframes):
    ## example of cleaning dataframes - further work to complete all tables
    # remove resourcetype column from all dataframes and drop duplicate ids
    for df in dataframes.values():
        dataframe_cleanup.drop_resourceType_column(df)
        dataframe_cleanup.remove_duplicate_ids(df)

    ## add patient id to the encounter df
    dataframe_cleanup.add_patient_id_to_dataframe(dataframes['Encounter'])

    ## add encounter id to tables with encounters
    dataframes_with_encounters = ['Condition', 'DiagnosticReport', 'Observation']
    for x in dataframes_with_encounters:
        dataframe_cleanup.add_encounter_id_to_dataframe(dataframes[x])


def populate_database(engine, dataframes):
    ## Inserts data from dataframes into database
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Inserting Dataframe Data to Postgres")
    try:
        for k, df in tqdm(dataframes.items()):
            try:
                AlchemyClass = getattr(models, k)
                database_population.insert_dataframe_to_db(session, df, AlchemyClass)
                print(f"Inserted {k} Data")
            except AttributeError as e:
                print(f"Model class for {k} not found: {e}") # to replace with better logging
        session.commit()

    ## Not ideal - Error handling as furhter work
    except Exception as e:
        # Rollback in case of error
        session.rollback()
        print(f"Failed to populate the database: {e}")
    finally:
        session.close()

def get_db_url():
    load_dotenv(dotenv_path=Path('.env'))
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')
    db_url = f'postgresql+pg8000://{db_user}:{db_password}@postgres:5432/{db_name}'
    return db_url

if __name__ == '__main__':
    main()
