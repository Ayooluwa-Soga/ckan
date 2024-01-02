# filtering the DOIs for datasets relating to a particular scientist/ORCID

import requests
import json
import os
from ckanapi import RemoteCKAN


# CKAN instance URL and API key (if required)
ckan_url = "172.30.2.41/api/3/action/"
api_key = ""  

# Scientist's name (adjust for your desired filtering method)
scientist_name = "Marie Curie"

# or use ORCID
orcid = ""

# Choose the appropriate filtering method:
filtering_method = "author"  # Options: "author", "tag", "organization"

# Construct search query based on filtering method
query = f"{filtering_method}:{scientist_name}"

# Make the search API request
response = requests.get(
    f"{ckan_url}/api/3/action/package_search",
    params={"q": query},
    headers={"Authorization": f"Bearer {api_key}"} if api_key else {}
)

response.raise_for_status()  # Raise an exception if API request fails

# Extract dataset IDs from the response
dataset_ids = [result["id"] for result in response.json()["result"]]

# Retrieve detailed information for each dataset
for dataset_id in dataset_ids:
    response = requests.get(
        f"{ckan_url}/api/3/action/package_show",
        params={"id": dataset_id},
        headers={"Authorization": f"Bearer {api_key}"} if api_key else {}
    )
    response.raise_for_status()

    dataset_info = response.json()
    print(f"Dataset Title: {dataset_info['title']}")
    # Access other relevant dataset details as needed
