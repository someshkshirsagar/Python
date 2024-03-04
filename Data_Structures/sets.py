set1=set()
#<class 'set'>
print(type(set1))


#Sets Are Mutable
set1.add(2)
set1.add(3)
set2=set([2,3])
set3={2,3}


#All three are same

print(set1)
print(set2)
print(set3)
print(set1 == set2 == set3)

set1.remove(2)
print(set1)

print(2 in set2)
set4={1,2,2,3,4,5}
#Hashable -> Meaning duplicates will not exists
print(set4)

#Elements of sets must be immuatble/hasbale    
# {[1,2,3],'abc'}#Throws Error

#Combined
set5 = set2 | set4
print(set5)

#Intersection -> only common elements
set6=set2 & set4
print(set6)


#Differnce -> only non-common elements
set7=set4-set2
print(set7)


#Symmetric Diff
(set4 - set2)|(set2-set4)
set2.symmetric_difference(set4)

