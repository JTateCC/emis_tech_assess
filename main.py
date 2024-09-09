from pathlib import Path
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scripts import json_extraction, database_population
import db.models as models

directory_path = os.path.join(Path.cwd() / 'data')
db_url = 'postgresql+pg8000://admin:emistest!@postgres:5432/emis'
def create_database_tables():

    engine = create_engine(db_url)
    models.Base.metadata.create_all(engine)

def populate_database():
    all_resource_dataframes = json_extraction.extract_all_json_to_dataframes(directory_path)
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    for k,v in all_resource_dataframes.items():
        v.drop('resourceType', axis=1, inplace=True)
        try:
            AlchemyClass = getattr(models, k)
            database_population.insert_dataframe_to_db(session, v, AlchemyClass)
        except AttributeError as e:
            print(f"Model class for {k} not found: {e}")
        except Exception as e:
            print(f"Exception occured {e}")


