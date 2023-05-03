"""
    Function examples

    Some simple function examples for Charter Python class.
"""
import os

def say_hello():  # Function takes no parameters
    """
        Output "Hello, world" for all to see. 
    """
    print("Hello, world")
    print()
    # If no return statement, return None


h = say_hello()  # Call function (arguments, if any, in () )
print(f"h: {h}")


def get_hello():
    """Get a phrase

    :return: phrase as a word
    :rtype: str
    """
    return "Hello, world"  # Function returns value


h = get_hello()  # Store return value in h
print(h)
print()


def sqrt(num):  # Function takes exactly one argument
    """Calculate square root of a number

    :param num: number for which to find square root
    :type num: int or float
    :return: square root of provided number
    :rtype: float
    """
    return num ** .5   # calculate square root 


m = sqrt(1234)  # Call function with one argument
n = sqrt(2)

print("m is {:.3f} n is {:.3f}".format(m, n))
print('-' * 60)

def find_text(text_to_find, *file_paths):
    # print(f"looking for {text_to_find} in {file_paths}")
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        with open(file_path) as file_in:
            for raw_line in file_in:
                if text_to_find in raw_line:
                    line = raw_line.rstrip()
                    print(file_name, line)

find_text('rabbit', '../DATA/alice.txt', '../DATA/words.txt', '../DATA/mary.txt')
find_text('wombat', '../DATA/testscores.dat')
find_text('honey badger')

def greet(whom="world"):
    print(f"Hello, {whom}")

greet("Mom")
greet("New York")
greet()


