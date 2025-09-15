## 1. Using Sorted() :    -> works only when all arrange in same alphabetical either capital or small
s1= "listen"
s2= "silent"
if sorted(s1) == sorted(s2):
    print("Yes Anagram")
else:
    print("Not Anagram")
