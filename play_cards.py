from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Priscilla")  # CardDeck.__init__()
print(f"d1: {d1}")
print(f"type(d1): {type(d1)}")

d2 = CardDeck("Mortimer")

# Bad programmer! No biscuit!!
print(f"d1._dealer: {d1._dealer}")

print(f"d1.dealer: {d1.dealer}")
print(f"d2.dealer: {d2.dealer}")

d1.dealer = "Francis"
print(f"d1.dealer: {d1.dealer}")

try:
    d1.dealer = [1, 2, 3]
except ValueError as err:
    print(err)
else:
    print(f"d1.dealer.upper(): {d1.dealer.upper()}")

d1.shuffle()
print(f"d1.cards: {d1.cards}")
print('-' * 60)

for _ in range(10):
    card = d1.draw()
    print(f"card: {card}")
print('-' * 60)
 
print(f"d1.cards: {d1.cards}")

print(f"d1.count(): {d1.count()}")

print(f"len(d1): {len(d1)}")

print(f"d1: {d1}")   # CardDeck: Priscilla, 42

print(d1)
print(str(d1))
print("=" * 60)
j1 = JokerDeck("Jimmy")
print(f"j1: {j1}")
print(f"type(j1): {type(j1)}")
j1.shuffle()
print(f"j1.cards: {j1.cards}")
