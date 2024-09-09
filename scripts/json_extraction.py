import json
from pathlib import Path
import os
import logging
import pandas as pd



logger = logging.getLogger(__name__)

pd.set_option('display.max_rows', None)    # Display all rows
pd.set_option('display.max_columns', None) # Display all columns
pd.set_option('display.width', None)       # No truncation of columns

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except UnicodeDecodeError as e:
        print(f"Error Reading {file_path}: {e}")
        return None
def extract_json_to_dataframe(data):
    resource_tables = {}

    for entry in data['entry']:
        resource_data = entry.get('resource', {})
        resource_type = resource_data.get('resourceType')

        if not resource_type:
            continue

        flat_data = flatten_resource(resource_data)

        if resource_type not in resource_tables:
            resource_tables[resource_type] = pd.DataFrame([flat_data])
        else:
            resource_tables[resource_type] = pd.concat([resource_tables[resource_type], pd.DataFrame([flat_data])], ignore_index=True)

    logger.debug("Resource Table Created")
    return resource_tables

def flatten_resource(resource):
    flattened = {}
    for key, value in resource.items():
        if isinstance(value, dict) or isinstance(value, list):
            flattened[key] = json.dumps(value)
        else:
            flattened[key] = value
    return flattened

def extract_all_json_to_dataframes(directory_path:str):
    all_resource_tables = {}
    i=0
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            json_data = load_json(file_path)
            if json_data:
                resource_tables = extract_json_to_dataframe(json_data)
                i+=1
                for resource_type, df in resource_tables.items():
                    if resource_type in all_resource_tables:
                        all_resource_tables[resource_type] = pd.concat(
                            [all_resource_tables[resource_type], df], ignore_index=True
                        )
                    else:
                        all_resource_tables[resource_type] = df
        if i > 10:
            break
    return all_resource_tables


patient_table = all_resource_dataframes['Encounter']
patient_table = patient_table.drop('resourceType', axis=1)
print(patient_table)
print(patient_table.columns.tolist())
