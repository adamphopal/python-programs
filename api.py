import urllib.parse
import requests
import os

main_api = 'https://maps.googleapis.com/maps/api/geocode/json?'


API_KEY = os.environ.get('GEOCODE_API')

while True:
    address = input('Adress: ')

    if address =='quit' or address =='q':
        break

    url = main_api + urllib.parse.urlencode({'address': address, 'key': API_KEY})
    print(url)

    json_data = requests.get(url).json()

    json_status = json_data['status']
    print('API Status: ' + json_status)

    if json_status == 'OK':
        for each in json_data['results'][0]['address_components']:
            print(each['long_name'])

        
        formatted_address = json_data['results'][0]['formatted_address']
        print()
        print(formatted_address)

#https://maps.googleapis.com/maps/api/geocode/json?address=lhr&key=AIzaSyAIJiD2GRhF-J_FCAgtlQk-WFmhaC0ySI8
