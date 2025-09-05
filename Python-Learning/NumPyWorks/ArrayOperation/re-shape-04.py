## Shape - reshape on an ARRAY  ##
##  - returns a tuple with index having the number of corresponding elements.


import numpy as np
arr=np.array([[2,4,6,8],[1,3,5,7]])
print(arr.shape)   ## (2,4)  -> 2 ROW , 4 COLUMN
print()

one=np.array([1,2,3,4,5,7,8,6], ndmin=5)  #ndmin =  specifies the no of dimension
print(one)
print('Shape of array:',one.shape)
print()

#Reshape- changing the shape of an array , i.e
# if it's 1d Array it can change it in 2D-Array

#Reshape From 1-D to 2-D
three= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=three.reshape(4,3)
print(newarr)
print()

#Reshape of 1D-3D
four= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newar=four.reshape(2,3,2)
print(newar)
print()

#Flattening the array with (-1)
newarr=four.reshape(-1)   #normal maa lagdinxa
print(newarr)