from collections import namedtuple

Person = namedtuple("Person", "first_name last_name product dob")

p = Person("Bill", 'Gates', 'Microsoft', '1955-10-28')

print(f"p.first_name: {p.first_name}")
print(p.last_name, p.dob)

print(type(p))

Point = namedtuple("Point", "x y")
p1 = Point(5, 10)
p2 = Point(10, 22)
p3 = Point(8, -6)

for p in p1, p2, p3:
    print(p.x, p.y, p[0], p[1])


