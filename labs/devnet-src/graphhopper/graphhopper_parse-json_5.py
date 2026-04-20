import requests
import urllib.parse

# Configuración inicial
route_url = "https://graphhopper.com/api/1/route?"
key = "1bce2606-0a44-48f5-895d-72aa4474a7e9" 
vehicles = ["car", "bike", "foot"]

def geocoding (location, key):
    while location == "":
        location = input("Enter the location again: ")
        
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q":location, "limit": "1", "key":key})
    
    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code
    
    if json_status == 200 and len(json_data["hits"]) != 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]
        
        if "country" in json_data["hits"][0]:
            country = json_data["hits"][0]["country"]
        else:
            country = ""
            
        if "state" in json_data["hits"][0]:
            state = json_data["hits"][0]["state"]
        else:
            state = ""
            
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
        if json_status != 200:
            print("Geocode API status: " + str(json_status) + "\nError message: " + json_data["message"])
        
    return json_status, lat, lng, new_loc

# --- BUCLE PRINCIPAL DE LA APLICACIÓN ---
while True:
    print("\n" + "=" * 49)
    loc1 = input("Starting Location: ")
    if loc1 == "quit" or loc1 == "q":
        break
    orig = geocoding(loc1, key)

    loc2 = input("Destination: ")
    if loc2 == "quit" or loc2 == "q":
        break
    dest = geocoding(loc2, key)

    # Selección de Vehículo
    print("-" * 30)
    print("Select vehicle: Car, Bike, Foot")
    v_input = input("Vehicle: ").lower()
    
    if v_input in vehicles:
        vehicle = v_input
    else:
        vehicle = "car"
        print("Unknown vehicle, defaulting to Car")
    print("-" * 30)

    print("=" * 49)
    if orig[0] == 200 and dest[0] == 200:
        op = "&point=" + str(orig[1]) + "%2C" + str(orig[2])
        dp = "&point=" + str(dest[1]) + "%2C" + str(dest[2])
        
        paths_url = route_url + urllib.parse.urlencode({"key":key, "vehicle":vehicle}) + op + dp
        
        paths_status = requests.get(paths_url).status_code
        paths_data = requests.get(paths_url).json()
        
        print("Routing API Status: " + str(paths_status) + "\nRouting API URL:\n" + paths_url)
        
        print("=" * 49)
        print("Directions from " + orig[3] + " to " + dest[3] + " by " + vehicle)
        print("=" * 49)
        
        if paths_status == 200:
            miles = (paths_data["paths"][0]["distance"])/1000/1.61
            km = (paths_data["paths"][0]["distance"])/1000
            sec = int(paths_data["paths"][0]["time"]/1000%60)
            min = int(paths_data["paths"][0]["time"]/1000/60%60)
            hr = int(paths_data["paths"][0]["time"]/1000/60/60)
            
            print("Distance Traveled: {0:.1f} miles / {1:.1f} km".format(miles, km))
            print("Trip Duration: {0:02d}:{1:02d}:{2:02d}".format(hr, min, sec))
            
            # PASO 5.b y 5.c: Bucle for con índice para instrucciones
            print("=============================================")
            for each in range(len(paths_data["paths"][0]["instructions"])):
                path = paths_data["paths"][0]["instructions"][each]["text"]
                distance = paths_data["paths"][0]["instructions"][each]["distance"]
                print("{0} ( {1:.1f} km / {2:.1f} miles )".format(path, distance/1000, distance/1000/1.61))
            
            print("=============================================")