from player import Player

class Dealer(Player):
    def play(self):
        info = ''
        while self.score() <= 16:
            info += f'Dealer\'s Cards:\n{str(self)} \nDealer Hits!\n'
            self.hit()
            if self.score() > 21:
                info += 'Bust!\n'
                break
        if self.score() <= 21:
            info += f'Dealer\'s Cards:\n{str(self)}\n'
        return info
