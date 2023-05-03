from pprint import pprint

d1 = dict()    # create new, empty dictionary
d2 = {'a': 5, 'm': 22, "f": 150, "l": 25}
d2['x'] = 15
d2['y'] = 88
d2['b'] = 22
d2['r'] = 22
d2['wombat'] = 12.9
d2['honey badger'] = 33.3333
d2['pastafazool'] = 8
d2['y'] = "whataburger"
d3 = {}
pprint(d2, sort_dicts=False)
print()

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"airports['MCO']: {airports['MCO']}")
print(f"airports['RDU']: {airports['RDU']}")
# print(f"airports['AUS']: {airports['AUS']}")
code = "AUS"
if code in airports:
    print(f"airports[code]: {airports[code]}")
    
print(f"airports.get(code): {airports.get(code)}")
print(f"airports.get('YCC'): {airports.get('YCC')}")
print(f"airports.get(code, 'NOT FOUND'): {airports.get(code, 'NOT FOUND')}")

print(f"airports.setdefault('AUS', 'Austin'): {airports.setdefault('AUS', 'Austin')}")
pprint(airports, sort_dicts=False)

airport_keys = airports.keys()
print(f"airport_keys: {airport_keys}")
print(f"airports.values(): {airports.values()}")
print('-' * 60)

for code, city in airports.items():
    print(code, city)
print()

print(f"airports.items(): {airports.items()}")







