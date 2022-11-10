# Ex 1: Create a function in Python that takes two arguments, name and age, and print their value.
def person(name, age):
    print("Hi", name, "you are", age, "years old")
    
person("Dani", 22)


######################### Diferencia entre tupla y lista ############################
# las tuplas no pueden ser modificadas directamente y las listas si (append o insert)
#####################################################################################


# Ex 2: Write a program to create function func1() to accept 
# a variable length of arguments and print their value.

# numbers se guarda en una tupla
def fun1(*numbers):
    # Convertimos a lista para poder añadir elementos
    num_list = list(numbers)
    print("Printing values...")
    num_list.append(999)
    for i in num_list:
        print(i)
    

fun1(1, 2, 3, 4, 5)


# Ex 3: Write a program to create function calculation() such that it can accept two variables 
## and calculate addition and subtraction. 
## Also, it must return both addition and subtraction in a single return call.
def calculation(a, b):
    return a+b, a-b

# Para guardar los return, separamos variables con coma tambien.
suma, resta = calculation(10, 3)
print("La suma es:", suma)
print("La resta es:", resta)


# Ex 4: Create a function with a default argument
## create a function show_employee() that accept the employee’s name and salary and display both.
## If the salary is missing in the function call then assign default value 9000 to salary

# For default value use '=' in argumet definition. 
## That value will be used only if no argument is passed
def showEmployee(name, salary = 9000):
    print(name, "salary is:", salary)
    

showEmployee("Ben", 12000)
showEmployee("Jessa")


# Ex 5: Create an inner function to calculate the addition in the following way:
## Create an outer function that will accept two parameters, a and b
## Create an inner function inside an outer function that will calculate the addition of a and b
## At last, an outer function will add 5 into addition and return it

def out_fun(a, b):
    # inner function
    def in_fun(a, b):
        return a+b
    return in_fun(a, b) + 5

print(out_fun(5, 10))


# Ex 6: Create a recursive function to calculate the sum of numbers from 0 to 10
## A recursive function is a function that calls itself again and again.
def sum(num):
    # if num > 0
    if num:
        return num + sum(num-1)
    else:
        return 0
    
    
print(sum(10))


# Ex 7: Assign a different name to function and call it through the new name
## Below is the function display_student(name, age). 
## Assign a new name show_student(name, age) to it and call it using the new name.

def display_student(name, age):
    print(name, age)

display_student("Emma", 26)

# Give a new name to the function (creting a new function and asigning the previous func functionality to it)
show_student = display_student
show_student("Emma", 26)

# We can still use the previous name
display_student("Dani", 22)


# Ex 8: Generate a list of all the even numbers within a range
def generateEvenlist(first, last):
    even_list = []
    for i in range(first, last+1, 1):
        # if even --> add to list
        if i % 2 == 0:
            even_list.append(i)
    return even_list


print(generateEvenlist(4, 30))

### Simpler way: Store numbers in range 4-30 with step=2 in a list and print
print(list(range(4, 30, 2)))
## Same list, but reversed
print(list(reversed(range(4, 30, 2))))


# Ex 9: Find the largest item from a given list
def findLargest(list):
    largest = 0
    for i in list:
        if i > largest:
            largest = i
    return largest


x = [4, 6, 8, 24, 12, 2]
print(findLargest(x))

## A simpler way is to use the built-in max() function
print(max(x))
