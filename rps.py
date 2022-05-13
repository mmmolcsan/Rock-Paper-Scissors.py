import random


class Player:
    score = 0

    def __init__(self):
        self.my_move = None
        self.their_move = None

    def record(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class HumanPlayer(Player):

    def __init__(self):
        super().__init__()
        self.behavior = 'Primary Player'

    def move(self):
        while True:
            move = input('rock, paper, or scissors\n').lower()
            if move in moves:
                return move
            else:
                print('Invalid Input')


# Random move
class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


# Returns only rock
class RepeatPlayer(Player):
    def move(self):
        return 'rock'


# Returns their last move
class ReflectPlayer(Player):

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


# Cycles through moves
class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            index = moves.index(self.their_move) + 1
            if index == len(moves):
                index = 0
            return moves[index]


def p1_win(one, two):
    return (
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock') or
            (one == 'rock' and two == 'scissors')
    )


def p2_win(one, two):
    return (
            (one == 'paper' and two == 'scissors') or
            (one == 'rock' and two == 'paper') or
            (one == 'scissors' and two == 'rock')
    )


class Game:
    def __init__(self, player1, player2):

        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()
        print(f'Player 1: {move1} Player 2: {move2}')

        if p1_win(move1, move2) is True and p2_win(move1, move2) is False:
            self.player1.score += 1
            print('You win!')
        elif p2_win(move1, move2) is True and p1_win(move1, move2) is False:
            self.player2.score += 1
            print('Player 2 wins!')

        else:
            print("It is a tie!")

        self.player1.record(move1, move2)
        self.player2.record(move1, move2)

        print('The score is: ')
        print(f'Player 1: {self.player1.score}\n'
              f'Player 2: {self.player2.score}\n')

    def play_game(self):
        print('Game has started!\n')
        for round in range(3):
            print(f'Round {round + 1}:')
            self.play_round()
        print('Game Over!\n\n')
        self.player1.score = 0
        self.player2.score = 0
        exit(0)


if __name__ == '__main__':
    moves = ['rock', 'paper', 'scissors']

    behaviors = {
        'human': HumanPlayer(),
        'reflect': ReflectPlayer(),
        'cycle': CyclePlayer(),
        'random': RandomPlayer(),
        'repeat': RepeatPlayer()
    }

    while True:
        print('Rock, Paper, or Scissors\n')
        print('Rules: Rock Beats Scissors,\n '
              'Scissors Beats Paper,\n '
              'Paper Beats Rock.\n'
              'Best out of 3 wins')

        choice = input('Who would you like to play against: '
                       '(random, reflect, repeat, cycle)\n').lower()
        if choice in behaviors:
            game = Game(behaviors['human'], behaviors[choice])
            game.play_game()
        else:
            print('Invalid Input. Try again.')

