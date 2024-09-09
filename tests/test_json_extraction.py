import pytest
import pandas as pd
import json
from scripts.json_extraction import extract_json_to_dataframe, flatten_resource, extract_all_json_to_dataframes


mock_json_data_1 = {
    "entry": [
        {
            "resource": {
                "resourceType": "Patient",
                "id": "123",
                "name": [{"use": "official", "family": "Doe", "given": ["John"]}],
                "gender": "male",
                "birthDate": "1980-01-01"
            }
        },
        {
            "resource": {
                "resourceType": "Observation",
                "id": "obs1",
                "status": "final",
                "code": {"text": "Blood Pressure"},
                "valueQuantity": {"value": 120, "unit": "mmHg"}
            }
        }
    ]
}

mock_json_data_2 = {
    "entry": [
        {
            "resource": {
                "resourceType": "Patient",
                "id": "456",
                "name": [{"use": "official", "family": "Smith", "given": ["Jane"]}],
                "gender": "female",
                "birthDate": "1990-05-15"
            }
        }
    ]
}


@pytest.fixture
def mock_flatten_resource():

    return {
        "resourceType": "Patient",
        "id": "123",
        "name": json.dumps([{"use": "official", "family": "Doe", "given": ["John"]}]),
        "gender": "male",
        "birthDate": "1980-01-01"
    }


def test_flatten_resource():
    resource_data = {
        "resourceType": "Patient",
        "id": "123",
        "name": [{"use": "official", "family": "Doe", "given": ["John"]}],
        "gender": "male",
        "birthDate": "1980-01-01"
    }
    flattened = flatten_resource(resource_data)
    assert isinstance(flattened, dict)
    assert flattened["id"] == "123"
    assert "name" in flattened
    assert isinstance(flattened["name"], str)


def test_extract_json_to_dataframe():
    """Test extracting a single JSON object into DataFrames."""
    resource_tables = extract_json_to_dataframe(mock_json_data_1)


    assert "Patient" in resource_tables
    assert "Observation" in resource_tables

    # Check the DataFrame structure for Patient
    patient_df = resource_tables["Patient"]
    assert isinstance(patient_df, pd.DataFrame)
    assert len(patient_df) == 1
    assert "id" in patient_df.columns
    assert "name" in patient_df.columns
    assert patient_df.iloc[0]["id"] == "123"

    # Check the DataFrame structure for Observation
    observation_df = resource_tables["Observation"]
    assert isinstance(observation_df, pd.DataFrame)
    assert len(observation_df) == 1
    assert observation_df.iloc[0]["id"] == "obs1"
    assert observation_df.iloc[0]["status"] == "final"


def test_concatenate_json_to_dataframe():
    """Test extracting and concatenating JSON data across multiple files."""

    resource_tables_1 = extract_json_to_dataframe(mock_json_data_1)

    resource_tables_2 = extract_json_to_dataframe(mock_json_data_2)

    all_resource_tables = {}


    for resource_type, df in resource_tables_1.items():
        if resource_type in all_resource_tables:
            all_resource_tables[resource_type] = pd.concat(
                [all_resource_tables[resource_type], df], ignore_index=True
            )
        else:
            all_resource_tables[resource_type] = df

    for resource_type, df in resource_tables_2.items():
        if resource_type in all_resource_tables:
            all_resource_tables[resource_type] = pd.concat(
                [all_resource_tables[resource_type], df], ignore_index=True
            )
        else:
            all_resource_tables[resource_type] = df

    patient_df = all_resource_tables["Patient"]
    assert len(patient_df) == 2
    assert patient_df.iloc[0]["id"] == "123"
    assert patient_df.iloc[1]["id"] == "456"


