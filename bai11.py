# Python program to demonstrate
# accessing of element from list


# from typing import ValuesView

# Creating a List with
# the use of multiple ValuesView
List = ["Learning", "for", "myself"]

# accessing a element from the list uing index number
print("Accessing a element from the list")
print(List[0:2])
print(List[2])

# Creating a Multi-Dimesnional List
# (By Nesting a list inside a List)
List = [['Learn', 'For'] , ['Myself']]

# accsessing an element from threading
# Multi-Dimensional List using
# index number
print("Acessing element from Multi-Dimensional list")
print(List [0][0])
print(List[1][0])

L1 = list()
L1.append([1, [2,3],4])
L1.extend([7,8,9])
print(L1[0][1][1] + L1[2])
print(L1)
print(L1[0][1][1])
print(L1[2])
