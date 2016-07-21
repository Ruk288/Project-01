e=input("enter start value")
f=input("enter end value")
e=int(e)
f=int(f)
a=range(e,f)
for i in a:
    if i%7==0:
        print(i)
