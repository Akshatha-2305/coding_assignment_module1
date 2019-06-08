#program to print the sum of digits of the entered number
num = int(input("Enter a Number: "))
result = 0
number=num
#usage of while loop
while num > 0:
    rem = num % 10
    result = result + rem
    num = int(num/10)
print("Sum of all digits of", number, "is: ", result)
