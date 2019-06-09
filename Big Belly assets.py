"""
This script makes a list of the assets of a city with Big Belly waste containers
This script is written in the API doc, more info https://clean.bigbelly.com
You need a token for this script
"""

# make sure you install the requests package
import requests

# the url of the API
url = "https://api.bigbelly.com/api/v2?objectType=assets&action=load"

querystring = {"objectType":"accounts","action":"load"}

# you need a token at // token here //
headers = {'X-Token': "// token here //", 'Cache-Control': "no-cache"}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
