import pandas as pd
from scripts.dataframe_cleanup import add_patient_id_to_dataframe


def test_add_patient_id_column():
    data = {
            "resourceType": ["CareTeam"],
            "id": ["b64b9c8b-ec81-e122-8565-7ab90eeb1420"],
            "subject": ['{"reference": "urn:uuid:6fa23508-960e-ff22-c3d0-0519a036543b"}']
        }

    encounter_df = pd.DataFrame(data)

    result_df = add_patient_id_to_dataframe(encounter_df)

    assert 'patient_id' in result_df.columns
    assert result_df['patient_id'][0] == '6fa23508-960e-ff22-c3d0-0519a036543b'
