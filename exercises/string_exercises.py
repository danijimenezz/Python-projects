# Ex 1A: Create a string made of the first, middle and last character
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
