import phonenumbers
from test import number
from phonenumbers import carrier
from phonenumbers import geocoder
import opencage
from opencage.geocoder import OpenCageGeocode
import folium
# a = input("Enter Victim's Phone Number : ")
pepnumber = phonenumbers.parse(number)
# phone_number = phonenumbers.parse(a)
location= geocoder.country_name_for_number(pepnumber,'en')
print(location)
serviceprovider=phonenumbers.parse(number)
# print (geocoder.country_name_for_number(serviceprovider,'en'))
# print(geocoder.description_for_number(serviceprovider,'en'))
print(carrier.name_for_number(serviceprovider,'en'))

key = '944709d076f94d72977655a555f0a479'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("mylocation.html")
input(" Enter To Exit")
