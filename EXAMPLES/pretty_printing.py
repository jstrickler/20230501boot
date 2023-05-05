from pprint import pprint

struct = {  # nested data structure
    'charlie': [
        ['a', 'b', 'c'], ['d', 'e', 'f']
    ],
    'delta': {
        'red': 55,
        'blue': [8, 98, -3],
        'purple': ['Chicago', 'New York', 'L.A.'],
    },
    'alpha': ['g', 'h', 'i'],
}

print('Without pprint:')
print(struct)  # print normally
print()

print('With pprint:')
pprint(struct)  # pretty-print
print()

print('With pprint (depth=2):')
pprint(struct, depth=1)  # only print top two levels of structure
print()

print('With pprint (sort_dicts=False):')
pprint(struct, sort_dicts=False)  # only print top two levels of structure
print()
