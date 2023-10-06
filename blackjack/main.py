# Melody Gatan, Kenton La
# 10/5/2023
# Blackjack - user makes bets and tries to beat the dealer
from check_input import get_int_range
from check_input import get_yes_no
from deck import Deck
from player import Player
from dealer import Dealer


def display_winner(pScore, dScore, points):
    if (dScore < pScore <= 21) or (dScore > 21 >= pScore):
        points[0] += 1
        print('Player wins.\n'
              f'Player\'s points: {points[0]}\n'
              f'Dealer\'s points: {points[1]}')

    elif (21 >= dScore > pScore) or (pScore > 21 >= dScore):
        points[1] += 1
        print('Dealer wins.\n'
              f'Player\'s points: {points[0]}\n'
              f'Dealer\'s points: {points[1]}')

    else:
        print('Both players tied!\n'
              f'Player\'s points: {points[0]}\n'
              f'Dealer\'s points: {points[1]}')


def main():
    print('-Blackjack-\n')
    deck = Deck()
    deck.shuffle()
    user_choice = True
    points = [0, 0]
    while user_choice:
        player = Player(deck)
        print('Player\'s Cards:')
        print(str(player), end='')
        if player.score() <= 21:
            hit_or_stay = get_int_range('1. Hit\n'
                                        '2. Stay\n'
                                        'Enter choice: ', 1, 2)
        print()
        while hit_or_stay == 1:
            player.hit()
            print('Player\'s Cards:')
            print(str(player), end='')
            if player.score() > 21:
                print('Bust!\n')
                break
            else:
                hit_or_stay = get_int_range('1. Hit\n'
                                            '2. Stay\n'
                                            'Enter choice: ', 1, 2)
                print()
        # Dealers turn
        dealer = Dealer(deck)
        info = dealer.play()
        print(info, end='')

        display_winner(player.score(), dealer.score(), points)
        user_choice = get_yes_no('Play again? (Y/N):')
        if len(deck) <= 15:
            deck = Deck()
            deck.shuffle()
        print()


main()