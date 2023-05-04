import sys
#  from pkg.pkg import module
from alpha.mathlib import geometry  # find and run geometry.py

print(f"geometry.PI: {geometry.PI}")

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)
print(f"geometry.ANIMALS[1]: {geometry.ANIMALS[1]}")

# module location algorithm
# 1. current folder          modules part of current project
# 2. folders in PYTHONPATH   typically locally created modules
#     dir1;dir2;dir3
# 3. INSTALLATION-DIR/lib... stdlib and downloaded modules
for path in sys.path:
    print(path)
