import pytest
import os
from pathlib import Path
from scripts.json_extraction import extract_all_json_to_dataframes
from scripts.database_population import insert_dataframe_to_db
import db.models as models

def test_insert_dataframe_to_db(session):


    all_resource_dataframes = extract_all_json_to_dataframes(os.path.join(Path.cwd() / 'data'))
    patient_df = all_resource_dataframes['Patient']

    # Insert the DataFrame to DB
    AlchemyClass = getattr(models, 'Patient')
    insert_dataframe_to_db(session, patient_df, AlchemyClass)

    # Query the database to check if the patient was inserted
    inserted_patient = session.query(models.Patient).first()
    assert inserted_patient is not None
