import requests
import json
APIkey = "d0ae8818b2d3e21a9e7ee62e7fc0bcd1"
cityname = input("Syötä haluamasi kaupungin nimi: ")
pyynto = "https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={APIkey}"
vastaus = requests.get(pyynto).json()
print(json.dumps(vastaus, indent=2))