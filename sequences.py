ctemps = [-40, 0, 37, 75, 100]

for celsius in ctemps:
    fahrenheit = ((9 * celsius) / 5) + 32
    #  f"...{VARIABLE}....{VARIABLE:FMT}...""
    print(f"{celsius:5.1f} C is {fahrenheit:5.1f} F")

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

clean_fruits = [f.strip().lower() for f in fruits]
print(f"clean_fruits: {clean_fruits}")

clean_fruits = []
for bbq in fruits:
    # f = fruits[0]
    # f = fruits[1]
    # f = fruits[2]
    # ...
    # f = fruits[6]
    value = bbq.strip().lower()
    clean_fruits.append(value)

