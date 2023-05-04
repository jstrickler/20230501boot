from carddeck import CardDeck

class JokerDeck(CardDeck):
    JOKER = '\U0001F0CF'
    NUM_JOKERS = 2
    def _make_deck(self):
        super()._make_deck() # call _make_deck() in superclass
        joker = self.JOKER, self.JOKER
        for _ in range(self.NUM_JOKERS):
            self._cards.append(joker)

