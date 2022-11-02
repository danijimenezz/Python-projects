# Ex 1: Print First 10 natural numbers using while loop
num = 1
while num <= 10:
    print(num)
    num += 1
    
    
# Ex 2: Write a program to print the number pyramid pattern using a loop.
n = int(input("Enter the size of the pyrimid: "))
cont = 1
for i in range(1, n+1):
    for j in range(1, cont+1):
        print(j, end=" ")
    print()
    cont += 1
    
    
# Ex 3: Calculate the sum of all numbers from 1 to a given number
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num+1):
    sum += i
print("The sum of the numbers from 1 to", num, "is:", sum)


# Ex 4: Write a program to print multiplication table of a given number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", i*num)


# Ex 5: Write a program to display only those numbers from a list that satisfy the following conditions
# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop
numbers = [12, 75, 150, 180, 145, 525, 50]
valid_nums = []

for number in numbers:
    # If num is < 500
    if number > 500:
        break
    # if number is divisible by 5 and < 150
    if number % 5 == 0 and number <= 150:
        valid_nums.append(number)

print(valid_nums)
    
        
# Ex 6: Count the total number of digits in a number
num = int(input("Enter a number: "))
str_num = str(num)
digits = 0
for i in str_num:
    digits += 1
print("The number", num, "has", digits, "digits")


# Ex 7: Write a program to use for loop to print the following reverse number pyramid pattern
num = int(input("Enter a number: "))
cont = num
for i in range(num):
    for j in range(cont, 0, -1):
        print(j, end=" ")
    print()
    cont -= 1


# Ex 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]