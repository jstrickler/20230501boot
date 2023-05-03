
colors = dict(red=5, green=18, blue=1, pink=0, grey=27, yellow=5)

print(f"colors: {colors}\n")


# sort by key
for color, num in sorted(colors.items()):  # No special sort needed to sort by key
    print(color, num)

print()

# sort by value with lambda
for color, num in sorted(colors.items(), key=lambda e: (e[1], e[0])): # Sorting by value uses second element of nested (key, value) pairs returned by items()
    print(color, num)
print()

# sort by value with defined function
def by_value(kv):
    return kv[1], kv[0]

for color, number in sorted(colors.items(), key=by_value, reverse=True):
    print(color, number)