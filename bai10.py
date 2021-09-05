# Creating list
ListEmpty = []
print("Empty list: ", ListEmpty)

# Adding
ListEmpty.append(20)
ListEmpty.append(11)
ListEmpty.append(1997)
print("List after adding: ", end="")
print(ListEmpty)

# Adding a list to a list
ListString = ["Duong","Phuong","Nga"]
ListEmpty.append(ListString)
print("List after adding a list:", end="")
print(ListEmpty)

Listchien = [7,1,97]

# Insert(vi tri, element)
Listchien.insert(0,80)
print(Listchien)
# removing element from list 
Listchien.remove(20)
Listchien.clear()
print("List after removing 2 elements: ", end="")
print(lstNumber)
