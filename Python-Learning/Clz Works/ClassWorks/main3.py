# Conditions and loops
if False:
    print("Condition is true")
else:
    print("Condition is false")

condition = True
if (condition):
    print("Condition is true")
else:
    print("Condition is false")


#WAp to check if the user is above 18
""" 
age= 7
age1= 17

if age> 18:
    print("She is eligible to marry")
elif age1== 18:
    print("She is 18")
elif age1 <=10:
    print("Can't count")
else:
    print("Not elgible")


#match(x) case1:            same as  switch case
abc=int(input("Enter a number: "))  #bydefault goes to string if not provided data type
print(type(abc))

match( abc):
 case 1:
        print("user enter value 1: ")
 case 2:
        print("user enter value 2")
        """ 

"""
  # Wap to chekc if the given string is vowel or not

str= (input("Enter a string"))
if str == ('a','e', 'i','o','u'):
   print("The string is vowel")
else:
    print("It's not vowel")
 

  # qn:2
check= int((input("Enter a string")))
if check%2==0:
    print("Number is odd")
else:
    print("its odd")

""" 
"""
print()


#qn 3
#wAP using match to check what day is today

day = input("Ente")

"""
"""
#qn 4 : leap year or not

year= int(input("Enter a year number"))
if year%100==0:
    print("It is leap year")
else:
    print("It's not a leap year")

"""
"""
#qn 5 : Prime or not

#qn6 : Identify which month is today

Month= int(input("Enter a year number"))

"""
"""
#qn 7
number = int(input("Enter a number: "))
if number >=0:
    print("its is +ve number")
elif number <= 0 :
    print("Its is -ve number")
else:
    print("Enter a valid number")
"""

""" 
#loops ->  For , While
for i in range (0,11):
    print(i)
print()
for i in range (0,11):
    if(i%2==0):
        print(i)

#while loop
ab = 0
while ab >= 10:
    print(ab)
    ab+=1
print()
# break statement -> break ,continue and pass
for i in range (0,11):
      print(i)
      if(i==5):
        break
        print(i)
print("")
print("Pass")
for i in range (0,11):
    pass
print("hello pass")

 # Qn : print("print numbers from 1-10")
for i in range (1,11):
    print(i)


#qn : Print all  even numbeers btn 2 value a and b
a= int(input("Enter 1st value:"))
b= int(input("Enter 2nd value:"))

for i in range (a,b):
    if i%2==0 :
        print(i)

#qn : Print all  ODD numbeers btn 2 value a and b
a= int(input("Enter 1st value:"))
b= int(input("Enter 2nd value:"))

for i in range (a,b):
    if i%2==1 :
        print(i)

"""
""" 
#QN : Print value btween 0 to 100 but not 50

num1=(int(input("Enter 1st range: ")))
num2=(int(input("Enter 2nd range: ")))
for  i in range (num1,num2):
    if( i == 50):
        continue
    print(i)
"""
#qn: Given number is prime  or not

num = int(input("Enter a number"))
if 
    print("Number is Prime")
else:
    print("The number is Not a prime")
