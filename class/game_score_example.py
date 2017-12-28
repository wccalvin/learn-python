#!/usr/local/bin/python3


class Game(object):

    def __init__(self, player):
        self.current_score = [0, 0]
        self.player = player

    def score(self):
        if self.player == 1:
            increment = self.current_score[0] + 1
            self.current_score[0] = increment
            return self.current_score
        else:
            increment = self.current_score[1] + 1
            self.current_score[1] = increment
            return self.current_score

play = Game(1)
print play.score()
