# Ex 1A: Create a string made of the first, middle and last character
import string


def slicedString(str):
    res = str[0] + str[int(len(str)/2)] + str[len(str)-1]
    return res


print(slicedString("123456789"))  # Expected output: 159


# Ex 1B: Create a string made of the middle three characters
def middleStr(str):
    middle = int(len(str)/2)
    res = str[middle-1] + str[middle] + str[middle+1]
    return res


print(middleStr("JaSonAy"))  # Expected output: Son
print(middleStr("JhonDipPeta"))  # Expected output: Dip


# Ex 2: Given two strings, s1 and s2.
# Write a program to create a new string s3 by appending s2 in the middle of s1.
def appendMidlle(s1, s2):
    mid = int(len(s1)/2)
    s3 = s1[:mid:] + s2 + s1[mid:]
    return s3


print(appendMidlle("Ault", "Kelly"))  # Exp output: AuKellylt


# Ex 3: Create a new string made of the first, middle, and last characters of each input string
def mixStr(s1, s2):
    return s1[0] + s2[0] + s1[int(len(s1)/2)] + \
        s2[int(len(s2)/2)] + s1[len(s1)-1] + s2[len(s2)-1]


print(mixStr("America", "Japan"))  # Ex output: AJrpan


# Ex 4: Arrange string characters such that lowercase letters should come first
def lowerFirst(str):
    low = ""
    upp = ""
    for i in str:
        if i.islower():
            low += i
        else:
            upp += i
    return low + upp


print(lowerFirst("PyNaTive"))  # Exp output: yaivePNT


# Ex 5: Count all letters, digits, and special symbols from a given string
def countStr(str):
    char = 0
    digit = 0
    sym = 0
    for i in str:
        if i.isalpha():
            char += 1
        elif i.isdigit():
            digit += 1
        else:
            sym += 1
    print("Total character:", char)
    print("Total digits:", digit)
    print("Total symbols:", sym)


countStr("P@#yn26at^&i5ve")  # Exp output: 8, 3, 4


# Ex 6: Given two strings, s1 and s2. Write a program to create a new string s3
# made of the first char of s1, then the last char of s2, Next, the second char
# of s1 and second last char of s2, and so on.
# Any leftover chars go at the end of the result.
def addStrings(s1, s2):
    # reverse s2
    s2 = s2[::-1]
    s3 = ""
    for i in range(max(len(s1), len(s2))):
        if i < len(s1):
            s3 += s1[i]
        if i < len(s2):
            s3 += s2[i]
    return s3


print(addStrings("abcde", "123"))  # Ex output: a3b2c1de


# Ex 7: Write a program to check if two strings are balanced.
# example: strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
# The character’s position doesn’t matter.
def string_balance_test(s1, s2):
    balanced = True
    while balanced == True:
        for char in s1:
            if char in s2:
                continue
            else:
                balanced = False
                break
        break
    return balanced


print(string_balance_test("Yn", "PYnative"))  # Ex output: True
print(string_balance_test("wYnx", "PYnative"))  # Ex output: False


# Ex 8: Find all occurrences of a substring in a given string by ignoring the case
str1 = "Welcome to USA. usa awesome, isn't it?"
word = "usa"

print("The word", word, "appears", str1.casefold().count(word.casefold()), "times")


# Ex 9: Calculate the sum and average of the digits present in a string
def avgDigits(str):
    suma = 0
    tot = 0
    for i in str:
        if i.isdigit():
            suma += int(i)
            tot += 1
    return suma, suma/tot


suma, avg = avgDigits("PYnative29@#8496")
print("The sum of the digits is:", suma)
print("The average of the digits is:", avg)


# Ex 10: Write a program to count occurrences of all characters within a string
def charAppr(str):
    char_dict = dict()
    for char in str:
        # add / update the count of a character
        char_dict[char] = str.count(char)
    print('Result:', char_dict)


charAppr("Apple")


# Ex 11: Reverse a given string
print("You reversed str is:", input("Enter a string: ")[::-1])


# Ex 12: Find the last position of a given substring
str1 = "Emma is a data scientist who knows Python. Emma works at google."
word = "Emma"
print("Last ocurrence of", word, "starts at index", str1.rfind(word))


# Ex 13: Write a program to split a given string on hyphens and display each substring.
str1 = "Emma-is-a-data-scientist"

for i in str1.split("-"):
    print(i)


# Ex 14: Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

for str in str_list:
    if str == "" or str == None:
        str_list.remove(str)

print(str_list)

# or use filter() function
new_str_list = list(filter(None, str_list))
print(new_str_list)


# Ex 15: Remove special symbols / punctuation from a string

str1 = "/*Jon is @developer & musician"
new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is : ", new_str)


# Ex 16: Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'
num_str = ""
for i in str1:
    if i.isdigit():
        num_str += i

print(num_str)
