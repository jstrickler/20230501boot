i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    name = input("What is your name? ")
    if name == 'q':
        break  # exit loop
    if name == '':
        print("please enter your name")
        continue # go to top
    print(f"Hello, {name}")


