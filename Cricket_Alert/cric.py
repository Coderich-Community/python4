import requests
import json
response_API = requests.get('https://api.cricapi.com/v1/series?apikey=80f10c47-820e-428c-941e-e5332f784b59')
print(response_API.status_code)

data = response_API.text

json.loads(data)

print(data)