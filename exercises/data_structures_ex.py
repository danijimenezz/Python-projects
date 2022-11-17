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
