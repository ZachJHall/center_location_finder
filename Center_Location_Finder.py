import requests
import json

#This program uses the MapQuest OpenGeocoding API
#https://developer.mapquest.com/documentation/open/geocoding-api/


KEY = '' #Put the Consumer Key in between quotes in the KEY variable

address = []

city = []

def establishCoordinates():
    n = 0

    longitudeTotal = 0
    latitudeTotal = 0
    addressCount = 0

    placeCount = int(input("How many locations are you going to enter?: "))

    while n < placeCount:



        address.append(input("Enter a address without the city or state: "))
        city.append(input("Enter the corresponding city, state: "))

        url = 'http://open.mapquestapi.com/geocoding/v1/address?key='+  KEY + '&location=' + address[addressCount] + ',' + city[addressCount]
        response = requests.post(url)
        json_data = response.json()

        latitude = (json_data['results'][0]['locations'][0]['displayLatLng']['lat'])
        longitude = (json_data['results'][0]['locations'][0]['displayLatLng']['lng'])

        latitude = float(latitude)
        longitude = float(longitude)

        latitudeTotal += latitude
        longitudeTotal += longitude


        n += 1
        addressCount += 1


        print()

    latitudeAverage = (latitudeTotal) / placeCount

    longitudeAverage = (longitudeTotal) / placeCount

    return latitudeAverage, longitudeAverage

def centerCoordinateToAddress(latitudeAverage, longitudeAverage):
    url = 'http://open.mapquestapi.com/geocoding/v1/reverse?key='+  KEY + '&location=' + latitudeAverage + ',' + longitudeAverage
    response = requests.post(url)
    json_data = response.json()
    street = (json_data['results'][0]['locations'][0]['street'])
    city = (json_data['results'][0]['locations'][0]['adminArea5'])
    state = (json_data['results'][0]['locations'][0]['adminArea3'])

    print()
    print("The exact center is (", latitudeAverage, ",", longitudeAverage, ")")
    print()
    print("The address is: ", street + ",", city + ",", state)



#This is where the functions begin get executed


latitudeAverage, longitudeAverage = establishCoordinates()

latitudeAverage = str(latitudeAverage)
longitudeAverage = str(longitudeAverage)

centerCoordinateToAddress(latitudeAverage, longitudeAverage)
