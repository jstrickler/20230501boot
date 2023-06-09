
import re

s = """lorem ipsum M-302 dolor sit amet, consectetur r-99 adipiscing elit, sed do
 eiusmod tempor incididunt H-476 ut labore et dolore magna Q-51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z-883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A-110 cupidatat non proident, sunt in H-332 culpa qui 
officia deserunt Y-45 mollit anim id est laborum"""

# match 0   -----------------
# match 1   -------
# match 2           ---------
pattern = r'([A-Z])-(\d{2,3})'  # parens delimit groups

for m in re.finditer(pattern, s):
    print(m.group(0), m.group(1), m.group(2))  # group 1 is first group, etc. (group 0 is entire match)
    print(m.start(1), m.end(1), m.span())
print()

matches = re.findall(pattern, s)  # findall() returns list of tuples containing groups
print("matches:", matches)

# match timestamp

#  r"(\d\d):(\d\d):(\d\d)"

#  r"([\w.-]*?)@(?:[\w.-]*?)""

#  r"(?:red|blue)\s+baron", r.I

