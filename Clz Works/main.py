# ternary operator ->
a= 10
ab = " greater than 18 years" if (a> 18)  else "none below 18"
print(ab)

if (a>18):
    print("greatrer than 18 years")
else:
    print("Less than")


    #Wap in ternary operator to print if the number is even or odd

n = 5
num = "Even" if (n % 2 == 0) else "Odd"
print(num)  


#identifier is, is not  :binary = True ? Fasle

a=10
b=20
c="10"
d=10

print(a is b)
print(a is not b)   #true
print(c is d)
print(a is d)


#list , tuple , set , dictionery

array=[1,2,3,4,5]

#certain index change
array[0]=0
print(array)

#methods in-build
array.append(1)     # add value to the end of array
print(array)
print(array.index(1))
array.pop()
print(array)

array.remove(0)
print(array)

b= array.copy()

array.clear()
print(array)
print(b)

b.insert(0,1)  #kun index maa kun valur halne
b.reverse()
print(b)


#  tuple

tup= (1,2,3,4,5,5)
print(tup)
print(tup[0])
  #tup[0]=0     #can't add another value to tuples
#print(tup)

ab= tup.count(5)
print(ab)
bc= tup.index(1)
print(bc)

#type conversion
#string, float, int
a=10
b=float(a)
print(b)
b=str(a)
print(type(b))
b=bool(a)
print(b)

#tuple -> list

cd=list(tup)
cd.append(6)
cd.insert(0,0)

#list -> tuple
ef=tuple(cd)     #tuple = type conversion  .... tup= variable
print(ef)

#set ->
set1={1,3,4,5,6,7}
print(set1)

set1.add(9)
print(set1)

set1.pop()
print(set1)

set2=set1.copy()
print(set2,"Set2")
set2= {4,5,6,7,8}
#set1.clear()
#print(set1)
print(set1.difference(set2))
print()
print(set1.union(set2))
print()
print(set1.intersection(set2))

#dict

dict1= {
    "name" : "hari",
    "age" : 4
}
print(dict1.items())
print()
print(dict1.keys())
print()
print(dict1.values())
print()

#print(dict1.clear())

for keys,values in dict1.items():
    print(keys, values)

#print set

for i in set2:
    print(i)
print()
for i in tup:
    print(i)
print()
for i in set2:
    print(i)

# print tuple
for cde in cd:
    print(cde)


print()

#set -> list
print()

