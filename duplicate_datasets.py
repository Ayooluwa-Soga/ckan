import ckanapi

ckan_api_url = "https://www.ckan_site.org/"
api_key = "api_key"

# ID of the dataset to duplicate
dataset_id = "dataset-to-duplicate"

# New title for the duplicated dataset
new_title = "new-title-for-duplicated-dataset"

client = ckanapi.RemoteCKAN(ckan_api_url, apikey=api_key)
original_dataset = client.action.package_show(id=dataset_id)

# Create a copy of the metadata for the new dataset
new_dataset_dict = original_dataset.copy()
new_dataset_dict["name"] = new_title
new_dataset_dict["id"] = None  # Generate a new unique ID
new_dataset = client.action.package_create(**new_dataset_dict)

# Print the new dataset's information
print("Done!")