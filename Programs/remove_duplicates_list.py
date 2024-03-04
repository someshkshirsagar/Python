list1=[1,2,3,4,5,4,4,]
set1= set(list1)
res_list=list(set1)
print(res_list)



def remove_duplicates(list):
    unique=[]
    for val in list:
        if val not in unique:
            unique.append(val)
    return unique        


print(str(remove_duplicates(list1)))