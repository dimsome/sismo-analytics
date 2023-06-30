# fetch_data_plausible.py

# Import necessary libraries
import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


def fetch_data_aggregate(site_id, period, interval, metrics):
    # Define the URL and headers
    url = f'https://plausible.io/api/v1/stats/aggregate?site_id={site_id}&period={period}&metrics={metrics}&interval={interval}'
    headers = {"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}

    # Send the GET request and fetch the data
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(
            f"GET request to {url} failed with status {response.status_code}")

    # Load the data into a JSON object
    data = response.json()

    return data


def fetch_data_aggregate_many(site_ids, period="day", interval="date", metrics="visitors,visits,pageviews"):
    # Loop through the site ids and fetch the data
    data = []
    for site_id in site_ids:
        # Fetch the data for each site id and add site id to the data
        data.append(
            {**fetch_data_aggregate(site_id, period, interval, metrics), "site_id": site_id})

    return data

# GET /api/v1/stats/timeseries


def fetch_data_timeseries(site_id, period, interval, metrics):
    # Define the URL and headers
    url = f'https://plausible.io/api/v1/stats/timeseries?site_id={site_id}&interval={interval}&period={period}&metrics={metrics}'
    headers = {"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}

    # Send the GET request and fetch the data
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(
            f"GET request to {url} failed with status {response.status_code}")

    # Load the data into a JSON object
    data = response.json()

    return data


def fetch_data_timeseries_many(site_ids, period="30d", interval="date", metrics="visitors,visits,pageviews"):
    # Loop through the site ids and fetch the data
    data = []
    for site_id in site_ids:
        # Fetch the data for each site id and add site id to the data
        data.append(
            {**fetch_data_timeseries(site_id, period, interval, metrics), "site_id": site_id})

    return data
