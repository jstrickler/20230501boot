import re

s = """lorem ipsum M-302 dolor sit amet, consectetur r-99 adipiscing elit, sed do
 eiusmod tempor incididunt H-476 ut labore et dolore magna Q-51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z-883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A-110 cupidatat non proident, sunt in H-332 culpa qui 
officia deserunt Y-45 mollit anim id est laborum"""

pattern = r'[A-Z]-\d{2,3}'  # store pattern in raw string

if re.search(pattern, s):  # search returns True on match
    print("Found pattern.")
print()

m = re.search(pattern, s)  # search actually returns match object
print(m, type(m))
if m:
    print("Found:", m.group(0))  # group(0) returns text that was matched by entire expression (or just m.group())    
print()

for m in re.finditer(pattern, s):  # iterate over all matches in string:
    print(m.group())
print()

# same as findall()
# matches = [m.group() for m in re.finditer(pattern, s)]

matches = re.findall(pattern, s)  # return list of all matches
print("matches:", matches)
