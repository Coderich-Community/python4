import requests
import json

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
    cric_api_key = config_data.get("CRIC_API_KEY")

response_API = requests.get(f'https://api.cricapi.com/v1/series?apikey={cric_api_key}')
print(response_API.status_code)

data = response_API.text

json.loads(data)

print(data)