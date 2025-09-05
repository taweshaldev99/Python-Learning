#  funcion-> funtion -> def 
def printName():
    print("HELLO World")

printName()
printName()
printName()
printName()
print()

def returnName():
    return "Hllo this is dev from  2nd fxn"
print(returnName())
print(returnName())
print(returnName())

print()
#using pass keyword
def passName():
    pass
print("Hello Dev")


#parameters in Fxn

def abc(a, b):
    print(a+b)
abc(10,20)    #arguments

#Fxn types
def abcd(a):
    print(a)
print(abcd(1))
print()


#even number print

def even (a, b):
    for i in range (a,b):
        if i%2==0 :
            print(f"even {i}")
even(10, 25)

#odd print
def odd ( a,b):
    for i in range (a,b):
        if i%2==1 :
            print (f"odd {i}")

odd(0,10)

#fxn type
# fxn with no parameter
# fxn with parameter
# fxn with return type but no parameter
# fxn with no return type

#fxn with no para np ret type
def printName():
    print('helo')
print()

# fxn with para no ret
def printName(a):
    print(a)
printName("Hello World")
print()

# fxn with return type but no parameter
def printName():
    return "HellO JAS"
print(printName())
print()

#fxn wwith  parameter and also have return type
def printName(a,b):
    return a+b
print(printName("Hari", "Shyam"))
print()

#parameter type in Python
#default 
#named
# *args
# **kwargs
#default
#positional arg  -> give valur to the arg as you 
                    #write in parameter


def abc(name,age):
    print(f"name={name} and age ={age}")
abc(27,"Shir")
print()

#named

def abc(name,age):
    print(f"name={name} and age ={age}")
abc(age=27,name="Shir")
print()

#default
def abc(name,age=70):
    print(f"name={name} and age ={age}")
abc("Shir")
abc("Shir",40)     # override 
print()

#
def abc(*name):
    for i in name:
        print(i)
print()

abc("Shiri","hari")

def abc(**details):
    for keys, values in details.items():
        print(keys, values)

abc(name="Sanoj",age=17, gender= "ismale")


print()
"""
#ALL Function Type:

def abc(a, b=10):   #default 
    print(f"a={10} and b={b}")
abc(1,2)

"""

def abcd():
    print("Hello")
    return "ok"  #return xa so tala ko print ignore garinxa .. understood dear !!!
    print("done")

print(abcd())

"""
#prime or not
def prime (num):
    if (num==0 & num== 1):
        flag = 0
        for i in range(2,100):
            elif i<= n/2:

for i =2 in  i <= n / 2:

if (num % i == 0) :
      flag = 1
      pass

"""
print()
#lambda function
let = lambda x,y: x+1
print(let(8, 9))
print()


#multiple of 5
def multiple(a=5):
    for i in range(1,11):
        print(a*i)
print(multiple())