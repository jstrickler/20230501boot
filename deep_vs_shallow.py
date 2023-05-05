from copy import deepcopy

list1 = ['alpha', 'bravo', 'charlie', [1, 2, 3]]
list2 = list1   # alias
list2.append('delta')
print(f"list1: {list1}")
print(f"list2: {list2}")
print()
print(f"list1 is list2: {list1 is list2}")  # id(list1) == id(list2)

list3 = list(list1)  # (shallow) copy
# or  list3 = list[::]
print(f"list1 is list3: {list1 is list3}")
list3.append('echo')
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")
print()
list3[3].append(99)
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")
print()
list4 = deepcopy(list1)   # actual recursive (deep) copy
list4[3].append(10000)
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")
print(f"list4: {list4}")

