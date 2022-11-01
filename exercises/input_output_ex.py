# For operating with files
import os

# Ex 1: Write a program to accept two numbers from the user and calculate multiplication
def mult():
	num1 = int(input("Enter a number: "))
	num2 = int(input("Enter another number to multiply: "))
	product = num1 * num2
	print("The result of multiplying " +str(num1)+ " and " +str(num2)+ " is: " + str(product))


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
try:
	with open("file1.txt", "r") as file:
		lines = file.readlines()  #This method returns all lines from a file as a list
except FileNotFoundError:
	print("That file was not found!")
   
	
try:
	with open("newfile.txt", "w") as newfile:
		count = 0
		for line in lines:
			if count == 4:
				count += 1
				continue
			else:
				newfile.write(line)
			count += 1
except FileNotFoundError:
	print("That file was not found!")
	


# Ex 7: Write a program to take three names as input from a user in the single input() function call.
str = input("Enter three names separated by a spaceline: ").split(" ")
cont = 0
for i in str:
	print("Name", cont, ":", i)
	cont += 1


# Ex 8: Write a program to use string.format() method to format the following three variables as per the expected output
totalMoney = 1000
quantity = 3
price = 450

print("I have {} dollars so I can buy {} football for {:.2f} dollars".format(totalMoney, quantity, price))  


# Ex 9: Write a program to check if the given file is empty or not
size = os.stat("file1.txt").st_size
if size == 0:
	print('file is empty')
	

# Ex 10: Read line number 4 from the following file
try:
	with open("file1.txt", "r") as file:
		lines = file.readlines()  #This method returns all lines from a file as a list
		print(lines[2])
except FileNotFoundError:
	print("That file was not found!")
	
		