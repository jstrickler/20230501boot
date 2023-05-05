from collections import Counter

with open('DATA/words.txt') as words_in:
    letters = [word[0] for word in words_in]

c = Counter(letters)
c['a'] += 1
c['0'] += 1

for letter, count in c.items():
    print(letter, count)
print()

print(c.most_common(5))

