import os

# Ex 1: Write a program to accept two numbers from the user and calculate multiplication
def mult():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number to multiply: "))
    product = num1 * num2
    print("The result of multiplying " +str(num1)+ " and " +str(num2)+ " is: " + str(product))
    
    
mult()


# Ex 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
print('My', 'name', 'is', sep='**')


# Ex 3: Convert Decimal number to octal using print() output formatting
print(oct(int(input("Enter a decimal number: "))))


# Ex 4: Display float number with 2 decimal places
num = float(input("Enter a float number"))
print('%.2f' % num)


# Ex 5: Accept a list of n float numbers as an input from the user

def createList(len):
    floatList = []
    for i in range(len):
        floatList.append(float(input("Enter number at index " +str(i)+ ": "))) 
    print(floatList)
    
    
len = int(input("Enter the length of your list of float numbers: "))
createList(len)


# Ex 6: Write all content of a given file into a new file by skipping line number 5

# Ex 7: Write a program to take three names as input from a user in the single input() function call.
str = input("Enter three names separated by a spaceline: ").split(" ")
cont = 0
for i in str:
    print("Name", cont, ":", i)
    cont += 1
    
    

    
    
        