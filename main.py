import requests
import json
import sys

params = {
    'linkurl': sys.argv[1]
}

response = requests.get(
    'https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/linkdetails',
    params=params,
)

print(json.loads(response.text[5:])[3][6])
