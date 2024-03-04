
try:

    f=open("demo2.txt","r")
    f.write("gyzuyfgg")
    print(f.read())
    f.close()
except FileNotFoundError as exe:
    print("File Not Found",exe)    
except(Exception) as e:
    print(e)

finally:
    print("Always Executed")    

#g=open("E:/28914_Somesh Kshirsagar/Python/Files/demo.txt","r")
#g.read()
#print(g.read())
