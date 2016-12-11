import random

class Deck(object):

	def shuffle(self):
		suits =["Spades", "Hearts", "Clubs", "Diamonds"]
		ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
		self.cards = []
		for suit in suits:
			for rank in ranks:
				self.cards.append("%s of %s"%(suit, rank))

		random.shuffle(self.cards)

	def deal(self):
		return self.cards.pop()

cards = Deck()
cards.shuffle()
print cards.deal()
print cards.deal()
print cards.deal()
print cards.deal()
print cards.deal()

