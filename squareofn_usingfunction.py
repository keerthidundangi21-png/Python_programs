"""Write a Python function, find_square() that acceptsan integer number n 
and returns the square of n.
Invoke the function and display the square of the number."""
def square(n):
    result=n**2
    return result
num=int(input("Enter a number: "))
print(square(num))