from random import shuffle


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return self.value + ' of ' + self.suit


class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init(self):
        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.cards.append(card)

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return 'Deck of' + str(self.count()) + ' cards'

    def _deal(self, num):
        if self.count == 0:
            raise ValueError('All cards have been dealt')
        elif self.count() <= num:
            self.cards = []
        else:
            self.cards = self.cards[:self.count() - num]

    def shuffle(self):
        if self.count == 0:
            raise ValueError('Only full decks can be shuffled')
        shuffle(self.cards)

    def _deal(self):
        return self.cards.pop()

    def deal_card(self):
        return self._deal()

    def deal_hand(num):
        result = []
        for n in range(num):
            result.append(self._deal())
        return result
