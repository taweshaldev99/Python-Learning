#polymorphism -> same obj , diff class
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak (self):
        print("Bark")
animal = [Cat(), Dog()]
for animals  in animal:
    animals.speak()
    
#exception handling -> try , catch ,else and finally
try:
  a
except NameError:
    print("Error")
except IndentationError:
    print("IndentationError occures")

else:
    print("No idea")
finally:
    print("error solved")


import requests

def GetWeather(city):
   url = f"https://api.weatherapi.com/v1/current.json?key=9c9940e9e1bf4e4ca6013952243112&q={city}&aqi=yes"
   data = requests.get(url)
   toJsons = data.json()
   location = toJsons['location']['name']
   temp= toJsons['current']['temp_c']
   print(f"location : {location}")
   print(f"temp: {temp}")
GetWeather("Kathmandu")
GetWeather("Butwal")
GetWeather("Janakpur")
GetWeather("Sarlahi")