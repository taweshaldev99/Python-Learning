print("Helo Worold")
# r->
# w ->
#append ->
# with

let = open("details.txt","r")   # im read mode file should exist already or shows error
const = let.read()
print(const)
let.close()


# w -> write    #even file doesn't exist it works  #override ni hunxa haii

file = open("example.txt","w")
file.write("Hello from 2nd last bench")   # takes string
file = open("example.txt","r")
details = file. read()   #readlines takes all
print(details)
print()


# a -> append mode
file = open("example.txt",mode="a")
file.write(f"\n{const}")
file = open ("example.txt",mode="r")
details = file.read()
print(details)
print()

"""
# os
import os 
os.remove("requirements.txt")
"""

#with operator in python
with open("example.txt", "r") as  files:
    details = files.read()
    print(details)
    files.close()

with open("example.txt",mode="w+") as file:

    file.write("HEyyyy")
    details = file.read()
    print(details)

#djano-admin startprojecr core .
# MVC -> laravel
#MVT -> model view templates

#python manage.py runserver