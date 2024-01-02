# filtering the DOIs for datasets relating to a particular scientist/ORCID

import requests
import json
import os
import yaml
from ckanapi import RemoteCKAN


# CKAN instance URL and API key (if required)
ckan_url = "http://172.30.2.41"
API_KEY = "3d392f00-cb97-4de3-b330-0aa56f6ae673"  

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"
HEADERS = {'User-Agent': user_agent}


# Scientist's name (adjust for your desired filtering method)
scientist_name = "Badu-Apraku, Baffour"

# or use ORCID
orcid = "0000-0003-0113-5487"

# Choose the appropriate filtering method:
filtering_method = "creator"  # Options: "author", "tag", "organization"
filtering_method_orcid = "creator_id"  # Options: for the orcid
# Construct search query based on filtering method
query = f"{filtering_method}:{scientist_name}"
query_orcid = f"{filtering_method_orcid}:{orcid}"

# Make the search API request
response = requests.get(
    f"{ckan_url}/api/3/action/package_search",
    params={"q": query_orcid},
    headers={"Authorization": f"Bearer {API_KEY}"} if API_KEY else {}
)

response.raise_for_status()  # Raise an exception if API request fails

# Extract dataset IDs from the response
# dataset_ids = [result["id"] for result in response.json()["result"]]

dataset_ids = response.json()["result"]
print(len(dataset_ids))
print(type(dataset_ids))
print(dataset_ids)
dataset_info_raw = response.json()['result']['results'] # returns a list of dicts(datasets)
creator_name = dataset_info_raw[1]['creator']
dois = []

for i in range(len(dataset_info_raw)):
    doi = dataset_info_raw[i]['identifier']
    title = dataset_info_raw[i]['title']  
    dict_item = {
        "Dataset Title": title,
        "DOI": doi
    }
    dois.append(dict_item)

# Create a file to store the results
with open(f"{creator_name}_datasets.json", "w") as file:
    json.dump(dois, file, indent=4)

with open(f"{creator_name}_datasets.json", 'r') as json_file:
    json_data = json.load(json_file)

yaml_format = yaml.dump(json_data, default_flow_style=False)

with open(f"{creator_name}_output_file.yaml", 'w') as yaml_file:
    yaml_file.write(yaml_format)