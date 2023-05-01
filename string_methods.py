actor = "Chris Hemsworth"
print(actor)
print(len(actor))

print(actor + " plays Thor")
print("is" in actor)
print("wombat" in actor)

print(actor.lower())   # obj.method()
print("hem" in actor)
print("hem" in actor.lower())
print(actor.upper())
print(actor.startswith('Chris'))
print(actor.startswith('Liam'))

file_path = "foo.txt"
print(file_path.removesuffix('.txt'))

print(actor.replace('Chris', 'Liam'))
print(actor.replace('s', ''))

print(actor.find('worth'))
print(actor.find("value"))

a = 22
b = 35
print("up {} down {}".format(a, b))
print(f"up {a} down {b}")

s = "Mary:Smith:Buffalo:NY"
fields = s.split(':')
print(fields)
s = "fee fi fo fum"
print(s.split())

s = "     All my exes live in Texas    "
print(s + "|")
print(s.lstrip() + "|")
print(s.rstrip() + "|")
print(s.strip() + "|")
print()

value = "$  40,000   "
print(value.strip(' $').replace(',', ""))















