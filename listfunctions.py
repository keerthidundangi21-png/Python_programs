#creating list
mylist=[]
print(mylist)
mylist=input("Enter the list elements separated by comma: ").split(',')
print("The list is: ", mylist)
#accessing list elements
print("The first element of the list is: ", mylist[0])
print("The last element of the list is: ", mylist[-1])
#slicing list
print("The first three elements of the list are: ", mylist[:3])
print("The last three elements of the list are: ", mylist[-3:])
#modifying list
mylist[0]="new value"
print("The modified list is: ", mylist)
#appending to list
mylist.append("new element")
print("The list after appending is: ", mylist)
