n=int(input("Enter a number: "))
sum=0
digit=len(str(n))
for i in range(digit):
    remain=n%10
    sum+=remain
    n//=10
print(sum)