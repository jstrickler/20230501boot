
fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

f1 = sorted(fruits)
print(f"f1: {f1}\n")

def ignore_case(s):
    s_compare = s.lower()
#    print(f"comparing {s} as {s_compare}")
    return s_compare

f2 = sorted(fruits, key=ignore_case)
print(f"f2: {f2}\n")

f3 = sorted(fruits, key=str.lower)
print(f"f3: {f3}\n")

f4 = sorted(fruits, key=len)
print(f"f4: {f4}\n")

f5 = sorted(fruits, key=len, reverse=True)
print(f"f5: {f5}\n")

def len_name(fruit):
    return len(fruit), fruit.lower()

f6 = sorted(fruits, key=len_name)
print(f"f6: {f6}\n")

numbers = [5, -10, 8.3, 98, 500, 4, 42323, 2]
n1 = sorted(numbers)
print(f"n1: {n1}\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(p):
    return p[-1]

sorted_people = sorted(people, key=by_dob)
for person in sorted_people:
    print(person)
print()
print("=" * 60)

for person in sorted(people, key=lambda p: (p[1], p[0])):
    print(person)
print()

print(sorted(fruits, key=lambda f: f.lower()))
print()





