list1=[1,2,3,4,5]


def funct1(n):
    return n**2
square=map(funct1,list1)
for i in square:
    print(i)

# squares=map(lambda num:num**2,list1)

# for num in squares:
#     print(num)