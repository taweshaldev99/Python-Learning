#OOP IN Python
#it's a programming paradigm
# real life example lai liyera class & object maa convert garinxa

# properties 
# Class 
# Object
# Methods
# self -> this
# 4 pillars -> encapsulation, inheritance , polymorphism, abstraction
# dunder methods
# class meta
# abstract class


# Class -> it's a blueprint
# Object -> instance of a class

let = 20

class Colony:
    #Properties , Fields
    let = 60
    name = "Dev"
house1 =  Colony()
print(house1.let)
print(house1.name)
print()

House2 = Colony()
House2.let = 80
print(House2.let)
name= "Kist"
print(House2.name)
print()

class Kist:
    Name = "Kist College"
    Address = "Pualisadak"
    Number = "9233485800 "
obj = Kist()
print(obj.Name)
print(obj.Address)
print(obj.Number)
print()

class Nist:
    def __init__(self,batch,name):   # constructor  ,,, self = this
        self.name = name
        self.batch = batch
        print(f"{name} and {batch}")

studentone = Nist("5","JAS")
print()
#constructor -> it's called when " Object" is called

class Nists:
    def __init__(self):   # constructor  ,,, self = this
      
        print(f"Called itself")

studentone = Nists()
print()


#normal methods
class add:
    def __init__(self,a , b):
        self.a = a
        self.b = b
        print(a+b)
    def AddNumber(self,c):
        print(self.a+self.b+c)

add1 = add(5,7)
add1.AddNumber(60)
print()

# WAP in OOP about the class name Students with thr following 
# options need to make a constructor with the value of name , age
# gender & batch , need to make 3 methods which will add two
# number to add a,b 
# 2nd methods which print name and last one print the gender and batch ok

class Students:
    def __init__(self,name,age,gender, batch):
        self.name = name
        self.age = age
        self.gender = gender
        self.batch = batch
stud= Students("Taweshal", "20","Male","2023")
print(stud.name)
print(stud.age)
print(stud.gender)
print(stud.batch)

print()

#static Class -> cls
#static methods

class One:
    @staticmethod
    def abc (a,b):
        return a+b
print(One.abc(10,20))
print()
class Two:
    ab = 200
    bc =30
    @classmethod   
    def cdf (cls , b):
        cls.bc= b
        print(cls.ab + b)
Two.cdf(30)

class age:
    @staticmethod
    def Ages(Ages):
        if Ages > 18:
            print("Cn Drive")
        else:
            print("Can't Drive")
age.Ages(8)
age.Ages(20)




