# Ex 1: Create a list by picking an odd-index items from the first list
# and even index items from the second
def even_odd_List(l1, l2):
    l3 = []
    # add odd index elements from l1
    for i in range(len(l1)):
        if i % 2 != 0 and i > 0:
            l3.append(l1[i])
    # add even index elements from l2
    for i in range(len(l2)):
        if i % 2 == 0 or i == 0:
            l3.append(l2[i])
    print("The new list is:", l3)


l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
even_odd_List(l1, l2)


# Ex 2: Write a program to remove the item present at index 4
# and add it to the 2nd position and at the end of the list.
list1 = [54, 44, 27, 79, 91, 41]

element = list1[4]  # 91
list1.pop(4)
list1.insert(2, element)
list1.append(element)

print(list1)  # [54, 44, 91, 27, 79, 41, 91]
