n=input("Enter a string: ")
t=n
for i in n:
    if (t==(n[::-1])):
        print("reverse:", n[::-1])
        print("Palindrome")
        break
    else:
        print("reverse:", n[::-1])
        print("Not a Palindrome")
        break
        