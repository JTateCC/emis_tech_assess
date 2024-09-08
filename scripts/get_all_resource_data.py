import json
import os


def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except UnicodeDecodeError as e:
        print(f"Error Reading {file_path}: {e}")
        return None


def extract_resources(data):

    resources = {}

    if 'entry' not in data:
        return resources

    for entry in data['entry']:
        resource_data = entry['resource']  # Extract the resource object
        resource_type = resource_data['resourceType']  # Get the resource type
        resource_keys = [key for key in resource_data.keys() if key != 'resourceType']  # Extract the keys from the resource

        # If this resource type is already in the dictionary, append the keys to the list
        if resource_type not in resources:
            resources[resource_type] = resource_keys

    return resources


def process_files(directory):
    all_resources = {}

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            json_data = load_json(file_path)
            if json_data:
                extracted_resources = extract_resources(json_data)
                # Update all_resources dictionary
                for resource_type, resource_list in extracted_resources.items():
                    if resource_type not in all_resources.keys():
                        all_resources[resource_type] = resource_list  # Add new resource type

    return all_resources

directory_path = 'C:\Programming\Projects\exa-data-eng-assessment\data'
full_resources = process_files(directory_path)


# for resource_type, resource_keys_list in full_resources.items():
#     print(f"Resource Type: {resource_type}")
#     for resource_keys in resource_keys_list:
#         print(resource_keys)

for resource_type in full_resources.keys():
    print(f"Resource Type: {resource_type}")
