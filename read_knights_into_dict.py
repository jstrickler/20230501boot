from pprint import pprint
knights_info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knights_info[name] = title, color, quest, comment
pprint(knights_info)

for knight_name, info in knights_info.items():
    print(info[0], knight_name, info[2])
print()

print(f"knights_info['Arthur']: {knights_info['Arthur']}")
print(f"knights_info['Arthur'][1]: {knights_info['Arthur'][1]}")


