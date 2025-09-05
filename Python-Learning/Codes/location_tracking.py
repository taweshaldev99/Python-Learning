import phonenumbers
from phonenumbers import geocoder

phone_number = phonenumbers.parse("+977 9823348580")

location = geocoder.description_for_number(phone_number,"en")

print("Location: ",location)