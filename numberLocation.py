
import phonenumbers

import folium

from myNumber import number

from phonenumbers import geocoder

key = '655abb7098e94d81a10fe1e6353758da'

a = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(a, 'en')
print(yourLocation)

# get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number, 'en')
print(carrier.name_for_number(service_provider,'en'))

# getting latitude and longitude of the number

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)

results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

# see location in map

myMap = folium.Map(location = [lat, lng], zoom_start = 9)

folium.Marker([lat, lng],popup = yourLocation).add_to(myMap)

# save map in html file

myMap.save("myLocation.html")




