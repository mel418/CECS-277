from random import shuffle
from card import Card

class Deck:
    '''
    _cards – a list of Card objects that are in the deck.
    '''
    def __init__(self):
        self._cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                self._cards.append(card)

    def shuffle(self):
        shuffle(self._cards)

    def draw_card(self):
        if len(self._cards) > 0:
            return self._cards.pop(0)

    def __len__(self):
        return len(self._cards)