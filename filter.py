# filtering the DOIs for datasets relating to a particular scientist/ORCID

import requests
import json
import os
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
dois = []

for i in range(len(dataset_info_raw)):
    doi = dataset_info_raw[i]['identifier']
    dois.append(doi)



# Retrieve detailed information for each dataset
# for dataset_id in dataset_ids:
#     response = requests.get(
#         f"{ckan_url}/api/3/action/package_show",
#         params={"id": dataset_id},
#         headers={"Authorization": f"Bearer {API_KEY}"} if API_KEY else {}
#     )
#     response.raise_for_status()

#     dataset_info = response.json()
#     print(f"Dataset Title: {dataset_info['title']}")
#     # Access other relevant dataset details as needed

# Create a file to store the results
with open("scientist_datasets.json", "w") as file:
    # Save all dataset information in a JSON format
    json.dump(dois, file, indent=4)