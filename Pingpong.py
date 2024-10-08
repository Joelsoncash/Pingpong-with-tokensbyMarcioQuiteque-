# Ping Pong Game with Tokens

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.tokens = 10  # Each player starts with 10 tokens

    def lose_token(self):
        if self.tokens > 0:
            self.tokens -= 1
        else:
            print(f'{self.name} has no tokens left!')

    def __str__(self):
        return f'{self.name} has {self.tokens} tokens.'

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        winner = random.choice([self.player1, self.player2])
        print(f'{winner.name} wins this round!')
        winner.lose_token()

    def play_game(self):
        while self.player1.tokens > 0 and self.player2.tokens > 0:
            self.play_round()
            print(self.player1)
            print(self.player2)
            time.sleep(1)  # Pause for a second between rounds

if __name__ == '__main__':
    player1 = Player('Alice')
    player2 = Player('Bob')
    game = Game(player1, player2)
    game.play_game()