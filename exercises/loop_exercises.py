import math

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
    #range(start, stop, step)
    for j in range(cont, 0, -1):
        print(j, end=" ")
    print()
    cont -= 1


# Ex 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]

# Solution 1:
# range(start, stop, step)
for i in range(len(list1)-1, -1, -1):
    print(list1[i])
    
# Solution 2:
rev_list = reversed(list1)
for item in list1:
    print(item)


# Ex 9: Display numbers from -10 to -1 using for loop
for num in range(-10, 0, 1):
    print(num)
    
    
# Ex 10: Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
#Else statement executes if loop finsih without errors
else: 
    print("Finished!!!")
    
    
# Ex 11: Write a program to display all prime numbers within a range
def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i==0:
            return False
    return True

print("Enter a range")
start = int(input("From: "))
stop = int(input("To: "))

for num in range(start, stop+1):
    if isPrime(num):
        print(num)
else: 
    print("Finished!")
    
    
# Ex 12: Display Fibonacci series up to 10 terms
long = int(input("How long do you want the Fibonacci series to be? : "))
last = 1
llast = 0
for i in range(long):
    if i<2:
        print(i, end=" ")
    else:
        num = last + llast
        print(num, end=" ")
        llast = last
        last = num
        

# Ex 13: Find the factorial of a given number
num = int(input("Enter a number: "))
fact = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        fact *= i

print(num, "! =", fact)


# Ex 14: Reverse a given integer number
def reverse(str):
    return str[::-1]

num = 12345
print("The reversed number of", num, "is:", reverse(str(num)))

print("Your reversed number is:", int(reverse(input("Enter a number: "))))


# Ex 15: Use a loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(my_list)):
    if i % 2 != 0 and i>0:
        print(my_list[i])
        
    
# Ex 16: Calculate the cube of all numbers from 1 to a given number
num = int(input("Enter a number: "))

for i in range(1, num+1, 1):
    print(i, "to the cube is:", i**3)


# Ex 17: Find the sum of the series upto n terms
num = int(input("Enter a number: "))
terms = int(input("Enter the number of terms of the series: "))
str_n = str(num)
str_tot = str_n
sum = 0

for i in range(terms):
    sum += num
    str_tot += str_n
    num = int(str_tot)

print("The total sum of the series is:", sum)
    
    
