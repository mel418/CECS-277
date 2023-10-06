from card import Card
from deck import Deck

class Player:
    '''
    _deck – a reference to the deck of cards that both the player and the dealer use.
    _hand – a list of Cards that the player is currently holding.
    '''
    def __init__(self, deck) -> None:
        self._deck = deck
        self._hand = []
        for _ in range(2):
           self.hit()
    
    def hit(self):
        card = self._deck.draw_card()
        self._hand.append(card)
        self._hand.sort()

    def score(self):
        total_score = 0
        # card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        for card in self._hand:
            if card.rank == 'Ace':
                if total_score <= 11:
                    total_score += 11
                else:
                    total_score += 1
            elif card.rank in ['Jack', 'Queen', 'King']:
                total_score += 10
            else:
                total_score += int(card.rank)
        return total_score
    
    def __str__(self) -> str:
        cards = "\n".join([str(card) for card in self._hand])
        return (f'{cards}'
                f'\nScore = {self.score()}\n')
        # hand_str = ""
        # for card in self._hand:
        #     hand_str += str(card) + "\n"
        # return hand_str + 'Score = ' + str(self.score()) + "\n"


