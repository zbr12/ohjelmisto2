import requests
import json
cityname = input("Syötä haluamasi kaupungin nimi: ")
pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=d0ae8818b2d3e21a9e7ee62e7fc0bcd1&units=metric"
vastaus = requests.get(pyynto).json()
print(vastaus["weather"][0]["description"])
print(str(vastaus["main"]["temp"]) + " Celsiusta.")