import requests
import json


url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    with open("data_input/api_raw_data.json", "w" ) as file:
        json.dump(data, file)
    print("data has been saved")