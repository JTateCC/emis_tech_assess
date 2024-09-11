import re
import pandas as pd


def drop_resourceType_column(df:pd.DataFrame):
        df.drop('resourceType', axis=1, inplace=True)


def remove_duplicate_ids(df:pd.DataFrame):
    df.drop_duplicates(subset=['id'],inplace=True)

# add the patient id based on the dataframe and then remove the patient column
def add_patient_id_to_dataframe(df:pd.DataFrame):
    key_lookup = None
    if 'subject' in df.columns:
        key_lookup = 'subject'
    elif 'patient' in df.columns:
        key_lookup = 'patient'
    if key_lookup:
        df['patient_id'] = df[key_lookup].apply(
            lambda x: extract_patient_id(x if pd.notnull(x) else None))
        df.drop([key_lookup], axis=1, inplace=True)

def extract_patient_id(reference):
    # Regular expression to capture UUID after 'urn:uuid:'
    match = re.search(r'urn:uuid:([a-zA-Z0-9\-]+)', reference)
    if match:
        return match.group(1)
    return None

# add the encounter id based on the dataframe and then remove the encounter column
def add_encounter_id_to_dataframe(df:pd.DataFrame):
    key_lookup = None
    if 'encounter' in df.columns:
        key_lookup = 'encounter'
    if key_lookup:
        df['encounter_id'] = df[key_lookup].apply(
            lambda x: extract_encounter_id(x if pd.notnull(x) else None))
        df.drop(key_lookup, axis=1, inplace=True)

def extract_encounter_id(reference):
    # Regular expression to capture UUID after 'urn:uuid:'
    match = re.search(r'urn:uuid:([a-zA-Z0-9\-]+)', reference)
    if match:
        return match.group(1)
    return None