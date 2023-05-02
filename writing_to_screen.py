name = "Tony Stark"
city = "Los Angeles"
value = 32.380234986304982496832

print(name, city, value)
print()  # prints only "\n"
print(name)
print(city)
print()

print(name, city, value, sep="/")
# str(name) + sep + str(city) + sep + str(value) + end
print(name, city, value, sep=",")
print(name, city, value, sep="")
print(name, city, value, sep=" <===> ")
print()

print(name, end=" ")  # normally end == '\n'
# conditional logic here ...
print(city)
print()

print(name, ":", city)
print(name, city, sep=":")

print(f"Avenger: {name}:{city} (AKA Iron Man)")
print("Avenger: {}:{} (AKA Iron Man)".format(name, city))

print(f'2 plus 2 is {2 + 2}')

print(f"value: {value}  {value:.2f}")

s = f"Avenger: {name}:{city}"
print(len(s))
print(s)




