"""Write a Python function, find_sum() that accepts an integer n 
and returns the sum of first n numbers.
Invoke the function and display the sum of first n numbers."""
def sum(n):
 one=0
    
 for i in range(1,n+1):
     one+=i
 return one
n=int(input("enter yor number:"))
print(sum(n))

    

