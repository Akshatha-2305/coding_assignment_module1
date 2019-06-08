#program to convert comma separated numbers to list and tuple
values=input("enter some comma separated numbers:")
#converting comma separated numbers to list
list=values.split(",")
#converting comma separated numbers to tuple
tuple=tuple(list)
#printing of list and tuple
print("List:",list)
print("Tuple:",tuple)
