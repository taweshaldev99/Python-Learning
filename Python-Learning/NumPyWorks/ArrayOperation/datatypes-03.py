##     Data Types of Numpy   ##
"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type
"""
import numpy as np
arr=np.array([1,2,3,4,5])
fruit=np.array(['apple','bananaaaaaa','cherry'])   
print(arr[1])

print(fruit.dtype)  #<u11 as banananaaa has max length 11
print(arr.dtype)    #int64
print()

one=np.array([2,4,6,8], dtype='S')
print(one)
print(one.dtype)   #|S1 ->S indicates string 
print()

two=np.array([1,3,5,7,9], dtype='i4')
print(two)
print(two.dtype)
print()

##  Converting Data Type on Existing Arrays  ##

three=np.array([1.1,2.3,4.6,8.2])
print(three)
print(three.dtype)
newthree=three.astype('bool')   #  astype make copy of the array   #tya comma maa j halxa tei anusar change hunxa
print(newthree)