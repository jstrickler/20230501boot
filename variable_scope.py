
x = 100  # GLOBAL variable (global to file)

def spam():
    y = 99  # LOCAL variable
    print("spam: x is", x)
    print("spam: y is", y)

x = 50

print("main: x is", x)
print(f"__name__: {__name__}")

spam()



