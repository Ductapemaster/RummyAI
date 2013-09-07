import random
from cardCollection import *

class Deck:
	def __init__(self):
		self.deck = CardCollection()
		for suit in range(1, 5):
			for rank in range(1,14):
				self.deck.addCard(Card(rank, suit))
				
	def __repr__(self):
		outputStr = ""
		for card in self.deck.cards:
			outputStr += card.__repr__()
			outputStr += "\n"
		return outputStr
	
	def shuffle(self):
		random.shuffle(self.deck.cards)
	
	# Pop off the top card of the deck and return it
	def getTopCard(self):
		return self.deck.popCard()
		
	def cardsLeft(self):
		return self.deck.numCards()
