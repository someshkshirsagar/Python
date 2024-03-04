names=['Karan','Amol','Nikita']



for position, name in enumerate(names):
    print(position,name)



from datetime import(date,timedelta)

today=date.today()
tommorrow= today + timedelta(days=1)
products=[
    {
        'name':"Apples",
        'price':120,
        'expiry_date':today,
    },
     {
        'name':"Oranges",
        'price':130,
        'expiry_date':today - timedelta(days=10),
    },
     {
        'name':"Grapes",
        'price':140,
       'expiry_date':today + timedelta(days=10),
    },
  
    
]

for product in products:
    
    if product['expiry_date']<today:
         product['expired']=True
         continue
    elif product['expiry_date']==today:
        product['price']-=product['price']*0.2 
    print(product['name'],'cost',product['price'])       
    

drivers={'Drogo':30,'Jon':12,'Sansa':11}
for name, age in drivers.items():
    if age>=18:
        can_drive=True
        print(name, "Is Allowed to Drive")
        break
    else:
        can_drive=False
if not can_drive:
    print("No one is Eligible to drive")       

#Can be better written as
for name, age in drivers.items():
    if age>=18:
        # can_drive=True
        print(name, "Is Allowed to Drive")
        break
    # else:
    #     can_drive=False
else:
    print("No one is Eligible to drive")       


#Prime Numbers upto 20
    # n=10
l=[]
for n in range(1,20):    
    for divisor in range(2,n):
        if n % divisor == 0:
            print(n,"is not prime number since it is divisible by",divisor)
            break
    else:
                      
         print(n,"is Prime")
         l.append(n)
print("Prime Numbers upto 20 are:",l)         

#need to convert each int to str first to use map()
print("The Prime numbers are -"," ,".join(map(str,l)))

