from collections import defaultdict

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

fruits_by_letter = defaultdict(list)

for fruit in fruits:
    first_letter = fruit[0]
    # if first_letter not in fruits_by_letter:
    #     fruits_by_letter[first_letter] = list()
    fruits_by_letter[first_letter].append(fruit)

for letter, fruit_list in fruits_by_letter.items():
    print(letter, fruit_list)

def get_zero():
    return 0

zvals = defaultdict(lambda: 0)   # default_dict(get_zero)

zvals['alpha'] = 456
zvals['bravo'] = 99
zvals['charlie'] = 18

for key in 'alpha', 'wombat', 'charlie', 3.8:
    print(key, zvals[key])











