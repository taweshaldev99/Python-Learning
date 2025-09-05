#slicing => extract subpart
# Slicing Array
import numpy as np
arr=np.array([1,2,3,5,6,7,8,9])
matrix=np.array([[1,3,5,7,9],[2,4,6,8,10]])
print(arr)
print( )
#Slicing
print(arr[1:5])  #print from 1-4 index i.e "start: end-1"
print( )
print(arr[0:7:3])  # print in the gap of 3 "start:end:step" 1,5,8

#negative slicing
print(arr[-5:-2])  #5,6,7
print( )

#working with 2-D Array
print(matrix[0:3,2]) #2tai ko 2nd index ko value print garxa
print( )

print(matrix[1, 2:4])  #2nd row ko value create hunxa
print( )

print(matrix[0:3, 1:3])  #2tai ko print garxa