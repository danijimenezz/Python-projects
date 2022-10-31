# Ex: Write a function to return True if the first and last number of
# a given list is the same. If numbers are different then return False.


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]


def equal(lista):
    for i in lista:
        first = lista[0]
        last = lista[len(lista) - 1]
        if first == last:
            return True
        else:
            return False


print(equal(numbers_x))
print(equal(numbers_y))


# Ex: Iterate a given list of numbers and
# print only those numbers which are divisible by 5

numbers = [10, 20, 33, 46, 55, 60, 75, 2]


def divisible(num, lista):
    print("The numbers divisible by " + str(num) + " are:")
    for i in range(len(lista)):
        if lista[i] % num == 0:
            print(lista[i])


divisible(5, numbers)


# Ex: Write a program to find how many times substring appears in a given string
str_x = "Dani es muy bueno en programacion"
word = "Dani"
times = str_x.count(word)
print("The word " + word + " appeared " + str(times) + " times")


# Ex: Write a ramp pattern given a number

num = int(input("Enter a number:"))


def print_ramp(number):
    cont = 1
    # Loop for printing 'num' lines
    for i in range(num):
        # Loop for each line
        for j in range(cont):
            print(str(cont), end=" ")
        # Jump to new line
        print()
        # Next number in next line
        cont += 1


print_ramp(num)


# Ex: Write a program to check if the given number is a palindrome number.

num = int(input("Enter a number:"))


def reverse_num(n):
    strg = str(n)
    r_str = strg[::-1]
    r_num = int(r_str)
    return r_num


def is_palindrome(n, r_num):
    if n == r_num:
        print("Number " + str(n) + " is a palindrome!")
        return True
    else:
        print("Number " + str(n) + " is NOT a palindrome!")
        return False


rev_n = reverse_num(num)
print("The reversed number is: " + str(rev_n))
is_palindrome(num, rev_n)


# Ex: Given a two list of numbers, write a program to create a new list such that
# the new list should contain odd numbers from the first list and
# even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]


# Dado una lista, devuelve nueva lista con los impares
def odd_list(lista):
    odd_lst = []
    for i in lista:
        if i % 2 != 0: # if odd
            odd_lst.append(i)
    return odd_lst


# Dado una lista, devuelve nueva lista con los pares
def even_list(lista):
    evn_lst = []
    for i in lista:
        if i == 0 or i % 2 == 0:  # if 0 or even
            evn_lst.append(i)
    return evn_lst


new_list = odd_list(list1) + even_list(list2)
print(new_list)


# Ex: Write a Program to extract each digit from an integer
# in the reverse order.
num = int(input("Enter a number: "))

strg = str(num)
rev_str = strg[::-1]
cont = 0

for i in rev_str:
    print(rev_str[cont], end=" ")
    cont += 1


# Ex: Calculate income tax for the given income by applying:
# nothing to first 10.000, 10% to next 10.000 and 20% to the remaining

total = int(input("Enter your taxable income: "))


def apply_tax(num):
    pay_tax = 0
    if num > 10000:
        first_tx = num - 10000
        if first_tx >= 10000:
            snd_tx = first_tx - 10000
            pay_tax += (10000 * 0.1) + (snd_tx * 0.2)
        else:
            pay_tax += (first_tx * 0.1)
    print("You have to pay $" + str(pay_tax) + " in taxes")
    return pay_tax


apply_tax(total)


# Ex: Print multiplication table form 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end=" ")
    print()


# Ex: Print downward Half-Pyramid Pattern with Star
num = int(input("Enter a number: "))
cont = num
for i in range(num):
    for j in range(cont):
        print("*", end=" ")
    print()
    cont -= 1


# Ex: Exercise 15: Write a function called exponent(base, exp)
# that returns an int value of base raises to the power of exp.

def exponent(base, exp):
    if exp < 0:
        print("Error: Exponent must be positive int")
    else:
        result = base ** exp
        print("Base " + str(base) + " to the power of " + str(exp) + " is = " + str(result))
        return result


exponent(5, 2)  # 25
exponent(5, -2)  # Error
exponent(5, 4)  # 625
exponent(0, 2)  # 0
exponent(-2, 2)  # 25








