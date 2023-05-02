list1 = list()   # call the list class
print(f"list1: {list1}")
list2 = ['alpha', 'bravo', 'charlie']
list3 = [1, 5, 98, 42, -4]
list4 = ["Fred", 2.6, 8, None, ['a', 'b', 'm']]
list5 = []  # empty list
print()

cities = ['Durham', 'Austin', 'St. Louis', 'Charlotte']
print(f"cities[0]: {cities[0]}")
print(f"cities[2]: {cities[2]}")

cities.append("Columbus")
print(f"cities: {cities}")

cities.insert(0, "Houston")
print(f"cities: {cities}")

cities.insert(3, "San Antonio")
print(f"cities: {cities}")

more_cities = ['Concord', 'Indian Trail']

cities.extend(more_cities)
print(f"cities: {cities}")

#  LIST.insert(pos, OBJ)  LIST.append(OBJ)  LIST.extend(ITERABLE)

del cities[1]    # del ANY-OBJECT
print(f"cities: {cities}")

cities.remove('Columbus')
print(f"cities: {cities}")

del cities[2:5]
print(f"cities: {cities}")

city = cities.pop()  # remove last element of list
print(f"city: {city}")
print(f"cities: {cities}")
city = cities.pop(2)  # remove third element of list
print(f"city: {city}")
print(f"cities: {cities}")

#  del LIST[pos]   LIST.remove(VALUE)    OBJ = LIST.pop(pos)

cities = ['Durham', 'Austin', 'St. Louis', 'Charlotte']
cities.append("Columbus")
cities.insert(0, "Houston")
cities.insert(3, "San Antonio")
more_cities = ['Concord', 'Indian Trail']
cities.extend(more_cities)
print(f"cities: {cities}\n")
print(f"len(cities): {len(cities)}")
print(f"cities[0]: {cities[0]}")
print(f"cities[5]: {cities[5]}")
print(f"cities[-1]: {cities[-1]}")
print(f"cities[-3]: {cities[-3]}")

# SLICE   start:stop  start:stop:step   :stop  start:

print(f"cities[0:3]: {cities[0:3]}")
print(f"cities[4:8]: {cities[4:8]}")
print(f"cities[:3]: {cities[:3]}")
print(f"cities[5:]: {cities[5:]}")
print(f"cities[:]: {cities[:]}")
print(f"cities[::]: {cities[::]}")

c2 = cities  # does NOT make a copy of cities
c3 = cities[::]   # DOES make a copy
c4 = list(cities) # DOES make a copy

cities[1:3] = ['Raleigh', 'Dallas', 'Stallings']
print(f"cities: {cities}")

#    012345
s = "wombat"
print(f"s[0:3] {s[0:3]}")
print(f"s[1:4] {s[1:4]}")
print(f"s[:3] {s[:3]}")
print(f"s[2:] {s[2:]}")
print('-' * 60)

# for VARIABLE ... in ITERABLE:   # list tuple dict str bytes GENERATOR
     # VARIABLE = ITERABLE[0]
     # VARIABLE = ITERABLE[1]
#    ...
#    Use VARIABLE
for city in cities:  # loop over the individual values in cities one at a time
    print(city)
print()

x = "abcd"
for letter in x:
    print(letter)
print()

#       0         1            2            3
argv = ['foo.py', 'jan01.log', 'jan02.log', 'jan03.log']
for file_name in argv[1:]:
    print(f"processing {file_name}")

# C lang
#  x[0]  # first element
#  *(x + 0)
#  x[1]  # second element
#  *(x + 1)

print(f"cities: {cities}")

city = "Orlando"
print(f"{city} in cities: {city in cities}")
print(f"{city} not in cities: {city not in cities}")
print(f"'Or' in {city}: {'Or' in city}")
print(f"'Wombat' in {city}: {'Wombat' in city}")

a = "foot"
b = "ball"
sport = a + b
print(f"sport: {sport}")

x = [1, 2, 3]
y = ['alpha', 'bravo', 'charlie']
z = x + y
print(f"z: {z}")

print('-' * 60)
print(f"'abc' * 10: {'abc' * 10}")

flags = [False] * 10
print(f"flags: {flags}")

print(f"len(cities): {len(cities)}")
print(f"len(z): {len(z)}")
print()

print(f"min(cities): {min(cities)}")
print(f"max(cities): {max(cities)}")
print(f"sorted(cities): {sorted(cities)}")

nums = [5.72, 42, -8.3, 19.2, 45, 16, 3]
print(f"min(nums): {min(nums)}")
print(f"max(nums): {max(nums)}")
print(f"sorted(nums): {sorted(nums)}")
print(f"sum(nums): {sum(nums)}")

print(f"cities: {cities}")

rev_cities = reversed(cities)
print(f"rev_cities: {rev_cities}")
# print(f"len(rev_cities): {len(rev_cities)}")
# print(f"rev_cities[0]: {rev_cities[0]}")
for city in rev_cities:
    print(city)

w = ['wombat', 'wallaby', 'platypus']
x = [1, 2, 3]
y = ['alpha', 'bravo', 'charlie']
combo = zip(w, x, y)
for animal, number, letter in combo:
    print(number, letter)
print(f"list(zip(w, x, y)): {list(zip(w, x, y))}")
print()

for i, city in enumerate(cities):
    print(i, city)
print()
print(f"list(enumerate(cities)): {list(enumerate(cities))}")
print()

for i in range(4):
    print(i)
print()

for i in range(1, 6):
    print(i)
print()







    


























