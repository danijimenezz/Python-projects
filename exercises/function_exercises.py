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
## 