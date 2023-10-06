class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    @property
    def rank(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        return ranks[self._rank]

    @property
    def suit(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        return suits[self._suit]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __lt__(self, other):
        return self._rank < other._rank

