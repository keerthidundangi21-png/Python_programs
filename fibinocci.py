#fibinocci series
a=0
b=1
c=0
n=int(input("enter number:"))   
for i in range(n+1):
    print(a,",",end=" ")
    c=a+b
    a=b
    b=c

    