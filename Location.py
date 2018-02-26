import urllib  # urllib is imported to open and read urls of API
import json    # json is required for data serialization

user_address = raw_input("Please enter an address: ")  # Request user for an address to find it's geolocation

#  Defining a fall-back function to find geolocation

def HEREapi(address):

    #  HERE API URL format

    url1 = "https://geocoder.cit.api.here.com/6.2/geocode.json?app_id="
    App_id = "u3DTqqeDLgFOsTQFMtec&"
    url2 = "app_code="
    App_code = "yQcL7HRtcjecTwat9uRiYQ"
    url3 = "&searchtext="

    #  Reading URL

    file = urllib.urlopen(url1 + App_id + url2 + App_code + url3 + address).read()

    #  Extracting data in json format

    data = json.loads(file)

    #  Sending get request and saving the response as response object

    results = data.get('Response')

    #  Extracting latitude and longitude of the first matching location

    location = results["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]

    lat = location["Latitude"]
    lng = location["Longitude"]
    lat_lng = [lat, lng]

    return lat_lng

#  Defining a function to find geolocation

def Googleapi(address):

    #  Google API URL format

    url1 = "https://maps.googleapis.com/maps/api/geocode/json?key="
    API_key = "AIzaSyB3Y6Wul6SONJK2TraLYWCpNgcQszHv9qk"
    url2 = "&address="

    #  Reading URL

    file = urllib.urlopen(url1 + API_key + url2 + address).read()

    #  Extracting data in json format

    data = json.loads(file)

    #  Sending get request and saving the response as response object

    results = data.get('results')

    #  Checking status to decide for fall-back api

    status = data.get('status')

    #  proxy condition

    if status == "OK":

        #  Extracting latitude and longitude of the first matching location

        location = results[0]['geometry']['location']
        lat = location["lat"]
        lng = location["lng"]
        lat_lng = [lat, lng]

        return lat_lng

    else:
        print "Since GOOGLE API is not is available, your location is being received from HERE API"

        # Calling fall-back API

        return HEREapi(address)

location = Googleapi(user_address)

#  Printing the output in [latitude, longitude] format

print location
