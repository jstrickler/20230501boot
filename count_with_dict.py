
counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food = raw_line.rstrip()
        
        if food not in counts:  # key is not present in dict
            counts[food] = 0  # initialize key with value 0
        
        counts[food] = counts[food] + 1  # replace value with value + 1 
        # counts[food] += 1

for food, count in counts.items():
    print(food, count)

print('-' * 60)

letter_counts = {}
with open('DATA/words.txt') as words_in:
    for raw_word in words_in:
        first_letter = raw_word[0]
        letter_counts[first_letter] = letter_counts.get(first_letter, 0) + 1

for letter, count in letter_counts.items():
    print(letter, count)

