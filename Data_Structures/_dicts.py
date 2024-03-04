dict1=dict(A=1, B=2)
dict2=dict([('A',1),('B',2)])
dict5={'A':1,'B':2}
print(dict1)


dict8={
    'h':1,
    'e':2,
    'l':3,
}
dict={}
print(dict8)
print(dict8.keys())
print(dict8.values())
print(dict8.items())
print(dict)





print('h' in dict8.keys())
#same as above dont use above method
print('h'in dict8)

print(1 in dict8.values())

print((('l',3))in dict8.items())





#Randomly removed since dictionaries are unordered
poppedItem=dict5.popitem()
print(poppedItem)
print(dict5)

poppedValue=dict8.pop('h')
print(poppedValue)
print(dict8)

#popping a key that does not exist errors out, but It is possible to set a default value
poppedValue=dict8.pop('key-does-not-exist','default-value111')
print(poppedValue)
print(dict8)

#Retrieving a key that does not exist would error out,
#but get returns 'None' in this scenarios
retrivedValue=dict8.get('key-does-not-exist')
print(retrivedValue)



print(len(dict8))
del(dict8['e'])
print(len(dict8))







