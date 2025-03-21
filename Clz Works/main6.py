# Encapsulation -> the process of hiding the attributes in the class
# attributes in the class
#access modifier
# -> public, protected, private
#    a.       _a .      __a

class Encap:
    def __init__(self,a ,b,c):
        self._a = a   #protected
        self. __b= b  #private
        self.c = c    #public
    def getinfo(self):
        print(f"a= {self._a}, b= {self.__b}, c = {self.c}")
   #change value in get info
    def changeValue(self, b):
        self.__b = b

obj1 = Encap(10,20,30)
print(obj1._a)
print(obj1.c)
#print(obj1.__b)
obj1.changeValue(70)
obj1.getinfo()
print()

# Wap to add 3 number using OOP encapsulation make 2 
# variable private change in the value in at first anf then add
"""
class Calc:
    def __init__(self,a, b, c):
        self._a = a
        self._b= b
        self.__c = c
    def getInfo (self):
        print(f"a={self._a} , b={self._b}, c={self.__c}")
              
    def ADD(self):


"""
#abstraction
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def details( self):
        pass
class Ford (Car):
    def details(self):
        print("Car is Ford") 
        
obj2= Ford()
obj2.details()
print()

#inheritance -> parent propertied access by child class
class Parent:
    def details(self ):
        print("this is parent class")

class Child(Parent):
    def details(self):
        super().details()
        
obj4 = Child()
obj4.details()

# Practise Qn:
class Car:
    def details(self, name, age, model ):
        print("Car Starts")
        print(f"The{ name} is of{ age} model{ model} ")
    

class Nissan(Car):
    def __init__(self,name, age , model):
        self.name = name
        self.age= age
        self.model = model
        
    def details(self):
     super().details(self.name,self.age,self.model)
     print("started")

obj5 = Nissan(" Nissan"," 2023" ," Mdoel X")
obj5.details()

#Multilevel inheritance

class Cars:
    def show(self):
     print("this is parent 1 car class")
class Bike:
    def show(self):
        print("this is byike")

class Details(Cars, Bike):
    def showDetail(self):
        Cars.show(self)
        Bike.show(self)
        print("Hello all're abpbe")

obj6 =Details()
obj6.showDetail()


#miltilevel inheritance

class A:
    name= "Hari"
    def show1(self):
        print("parent level 1")

class B(A):
    name= "Sita"
    def show2(self):
        print("2nd levbel class")

class C(B):
    name="Laxman"
    def show3 (self):
        print("3rd level")

obj7= B()   #call
obj7.show1()
obj7.show2()

obj8 = C()
obj8.show1()
obj8.show2()
obj8.show3()


#hirearcial
# gp ->p -> c
class gp:
    last_name = "Thakur"
    def show (self):
        print("gp")

class p(gp):
    def shows(self):
        print("gp->p")
class c(gp):
    def showss(self):
        print("gp -> p -> c")
obj9 =p()
print(obj9.last_name)
obj10 =c()
print(obj10.last_name)