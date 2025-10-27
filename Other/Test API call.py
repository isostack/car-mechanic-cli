import requests
import json


ma = input("What is the make of the vehicle? ")
mo = input("What is the model? ")
ye = input("What is the model year? ")


def get_recall(make, model, model_year):
    url = "https://api.nhtsa.gov/recalls/recallsByVehicle"
    params = {
        "make": make,
        "model": model,
        "modelYear": model_year
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"Error": f"Failed to retrieve data, error code {response.status_code}"}


def format_data(car_info):
    if 'error' in car_info:
        print(car_info['error'])
    else:
        print(json.dumps(car_info, indent=2))

    if car_info['Count'] > 0:
        print("\nRecall information:\n")
        for result in car_info['results']:
            print(f"Manufacturer: {result['Manufacturer']}")
            print(f"Campaign Number: {result['NHTSACampaignNumber']}")
            print(f"Component: {result['Component']}")
            print(f"Summary: {result['Summary']}")
            print(f"Consequence: {result['Consequence']}")
            print(f"Remedy: {result['Remedy']}")
            print(f"Notes: {result['Notes']}")
            print(f"Model Year: {result['ModelYear']}")
            print(f"Make: {result['Make']}")
            print(f"Model: {result['Model']}")
            print(f"*********************************")


car_info = get_recall(ma, mo, ye)
format_data(car_info)
