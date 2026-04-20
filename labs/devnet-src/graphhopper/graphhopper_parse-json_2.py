import requests
import urllib.parse

# Configuración inicial
route_url = "https://graphhopper.com/api/1/route?"
loc1 = "Washington, D.C."
loc2 = "Baltimore, Maryland"
key = "1bce2606-0a44-48f5-895d-72aa4474a7e9" 

def geocoding (location, key):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q":location, "limit": "1", "key":key})
    
    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code
    
    # Paso 9.b: La declaración de impresión se eliminó de aquí y se movió abajo
    
    if json_status == 200:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]
        
        # Paso 9.c: Verificación de País
        if "country" in json_data["hits"][0]:
            country = json_data["hits"][0]["country"]
        else:
            country = ""
            
        # Paso 9.c: Verificación de Estado
        if "state" in json_data["hits"][0]:
            state = json_data["hits"][0]["state"]
        else:
            state = ""
            
        # Formateo del nombre de la ubicación (new_loc)
        if len(state) != 0 and len(country) != 0:
            new_loc = name + ", " + state + ", " + country
        elif len(country) != 0:
            new_loc = name + ", " + country
        else:
            new_loc = name
            
        print("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")\n" + url)
    else:
        lat = "null"
        lng = "null"
        new_loc = location
        
    # Paso 9.c: Ahora retornamos 4 valores en la tupla
    return json_status, lat, lng, new_loc

# Llamadas a la función (Paso 9.d)
orig = geocoding(loc1, key)
print(orig)

dest = geocoding(loc2, key)
print(dest)