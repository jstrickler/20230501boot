folder1 = [
    'readme.txt',
    'spam.py',
    'ham.py',
    'toast.py',
    'foo.py',
    'bar.py',
]

folder2 = [
    'readme.txt',
    'spam.py',
    'ham.py',
    'toast.py',
    'blah.py',
    'baz.py',
]

s1 = set()
s2 = {1, 2, 3}
fset1 = set(folder1)
fset2 = set(folder2)
fset1.add('jam.py')
fset2.add('jelly.py')
fset1.add('spam.py')


print(f"fset1 & fset2: {fset1 & fset2}")  # common (intersection)
print(f"fset1 ^ fset2: {fset1 ^ fset2}")  # not common (xor)
print(f"fset1 | fset2: {fset1 | fset2}")  # unique combination (union)
print(f"fset1 - fset2: {fset1 - fset2}")  # fset1 only (remove fset2 from fset1)
print(f"fset2 - fset1: {fset2 - fset1}")  # fset2 only (remove fset1 from fset2)
print('-' * 60)

with open("DATA/breakfast.txt") as breakfast_in:
    foods = breakfast_in.read().splitlines()
print(f"foods: {foods}")
print()
unique_foods = set(foods)
print(f"unique_foods: {unique_foods}")


