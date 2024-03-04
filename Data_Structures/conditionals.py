income=35000
if income <10000:
    tax_percentage=0.0
elif income <20000:
    tax_percentage=0.2    
elif income<30000:
    tax_percentage=0.3
else:
    tax_percentage=0.4        

tax= income*tax_percentage
print("I will need to pay",tax,"as tax.")    

if tax>10000:
    quanlifier="a lot"
else:
    quanlifier="not too much"   
 #One Liner
quantifier="a lot" if tax>10000 else "not too much"
print("That's ",quanlifier, ".",sep='')


