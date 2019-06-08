#function for binary search (using recursion)
def binary_search(user_list, start, end, key):
    
    if not start < end:
        return -1
 
    mid = (start + end)//2
    if user_list[mid] < key:
        return binary_search(user_list, mid + 1, end, key)
    elif user_list[mid] > key:
        return binary_search(user_list, start, mid, key)
    else:
        return mid
 
#main program
user_list = [] 
n = int(input("Enter number of elements : "))  
for i in range(0, n): 
    ele = int(input()) 
  
    user_list.append(ele) # adding the element 
      
print("the entered list is",user_list) 
key= int(input('The number to search for: '))
index = binary_search(user_list, 0, len(user_list), key)#calling the function
if index < 0:
    print("the number is not found")
else:
    print("the number is found at index:",index)
