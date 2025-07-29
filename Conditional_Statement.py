# if else code
""" 
age=int(input("Enter age: "))
if age>=18:
    print("You're eligible to vote")
else:
    print("You're not eligible to vote")

# even odd 
num=int(input("Enter value: "))
if num%2==0:
    print("it is even number")
else:
    print("It's odd")
    """
""" 
#prime number
num=int(input("Enter value: "))
if num

"""

#Password Strenght Checker
""" Condition->
Problem: Write a program to check the strength of a password:

Weak: Length < 6
Moderate: Length 6-10 with alphanumeric characters
Strong: Length > 10 with at least one special character


password=input("Enter password: ")
lenght= len(password)
if lenght<6 :
    print("Weak password")
elif lenght>6 and lenght<10 and password.isalnum() :
    print("Moderate Password")
else :
    print("Strong Password")

    """
#pallindrome by slicing technique
num=input("Enter number: ")
if num== num[::-1]:
    print("Pallindrome")
else:
    print("not pallindrome")
