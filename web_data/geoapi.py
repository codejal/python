import json
import urllib.request
import urllib.parse
import urllib.error
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address = 'Ann Arbor, MI'
    url = serviceurl+urllib.parse.urlencode({'address': address})
    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("retrieved", len(data), "characters")
    try:
        jso = json.loads(data)
    except:
        jso = None

    if not jso or'status' not in jso or jso['status'] != 'OK':
        print("=====faliure====")
        print(data)
        print(jso)
    else:
        print("====success====")
        print(data)
        print(jso)
    latitide = jso['results'][0]['geometry']['location']['lat']
    longitude = jso['results'][0]['geometry']['location']['lng']
    location = jso['results'][0]['formatted_address']
    print("latitude=", latitide)
    print("longitude=", longitude)
    print("location=", location)
