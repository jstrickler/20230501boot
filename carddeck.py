import random

class CardDeck:   # inherits from 'object' class
    # class variables
    CLUB = '\u2663'
    DIAMOND = '\u2666'
    HEART = '\u2665'
    SPADE = '\u2660'
    SUITS = CLUB, DIAMOND, HEART, SPADE
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


    # constructor -- initializers new instance
    def __init__(self, dealer):
        self._dealer = dealer  # save info in instance
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)
    
    def draw(self):
        return self._cards.pop()

    def count(self):
        return len(self._cards)
    
    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}: {self.dealer},{len(self)}"


    @property
    def dealer(self):  # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise ValueError("Dealer must be a string")

    # (instance method)
    def print_dashed_line(self):
        print("-" * 20)

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    @staticmethod
    def print_line(symbol):
        print(symbol * 60)

if __name__ == "__main__":
    d = CardDeck("Fred")
    print(f"d.get_suits(): {d.get_suits()}")
    print(f"CardDeck.get_suits(): {CardDeck.get_suits()}")
    CardDeck.print_line("=")
    d.print_line('*')
    d.print_dashed_line()



