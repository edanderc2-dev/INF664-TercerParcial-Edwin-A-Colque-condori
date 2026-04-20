import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"
loc1 = "Washington, D.C."
loc2 = "Baltimore, Maryland"
key = "1bce2606-0a44-48f5-895d-72aa4474a7e9" 

url = geocode_url + urllib.parse.urlencode ({"q": loc1, "limit": "1", "key": key})
replydata = requests.get(url)
json_data = replydata.json()
json_status = replydata.status_code
print(json_data)