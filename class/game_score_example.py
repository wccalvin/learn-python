#!/usr/local/bin/python3


class Game(object):

    def __init__(self):
        self.current_score = [0, 0]

    def score(self, player):
        self.player = player

        if self.player == 1:
            increment = self.current_score[0] + 1
            self.current_score[0] = increment
            return self.current_score
        else:
            increment = self.current_score[1] + 1
            self.current_score[1] = increment
            return self.current_score

play = Game()
print play.score(1)
