"""
struct person {
    char *fname;
    char *lname;
    int age;
}
"""

person = "Bill", "Gates", "Microsoft", "1955-10-28"
print(f"type(person): {type(person)}")
print(f"person[0]: {person[0]}")
print(f"person[1]: {person[1]}")

# no append, insert, extend
# no del, pop, remove
# no person[0] = "Melinda"

first_name, last_name, product, dob = person  # iterable unpacking

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', 'rsend', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
    ('Frank', 'Sinatra', '1915-04-18'),
]


print(f"type(people): {type(people)}")
print(f"type(people[0]): {type(people[0])}")
print(f"people[0]: {people[0]}")
print(f"people[0][0]: {people[0][0]}")
print(f"people[0][0][0]: {people[0][0][0]}")
print('-' * 60)
for person in people:
    print(person, person[0], person[1])
print()

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, product, dob)
print()










