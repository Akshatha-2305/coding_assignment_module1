#program to convert comma separated numbers to list and tuple
values=input("enter some comma separated numbers:")
list=values.split(",")
tuple=tuple(list)
print("List:",list)
print("Tuple:",tuple)
