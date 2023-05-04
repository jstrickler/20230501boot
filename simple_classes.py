import re

cities = list()   #   List cities = new List();

cities.append("Durham")
cities.append("Austin")
cities.sort()    # LIST.sort(key=...)
print(f"cities: {cities}")

print(f"type(cities): {type(cities)}")
print(f"type(re): {type(re)}")  
print(f"type(print): {type(print)}")
print(f"type(list): {type(list)}")
x = 5
print(f"type(x): {type(x)}")

class Dog:
    def bark(self):
        print("Woof! Woof!")

d1 = Dog()
d2 = Dog()
print(type(d1), type(d2))
d1.bark()
d2.bark()

# multi-paradigm
#  1. imperative 
#  2. object-oriented
#  3. functional

# client code:
# 

with open('DATA/mary.txt') as mary_in:  # TextIOWrapper
    pass

















