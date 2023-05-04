with open("../DATA/fruit.txt", "r") as F:
    fruit_lines = F.read().splitlines()

print(sorted(fruit_lines))
print()

print(sorted(fruit_lines, key=str.lower))
print()

#  lambda parameters: (return value)
print(sorted(fruit_lines, key=lambda s: (len(s), s.lower())))
print()

def length_and_name(s):
    return len(s), s.lower()

print(sorted(fruit_lines, key=length_and_name))
print()

print(sorted(fruit_lines, key=lambda s: (s[1].lower(), s[0].lower())))
print()


def wacky(fruit):
    print(f"comparing {fruit} as {fruit.lower()}")
    return fruit.lower()

result = sorted(fruit_lines, key=wacky)
print(f"result: {result}")


