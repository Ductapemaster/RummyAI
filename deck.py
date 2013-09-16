import random
import copy
from card import *

# Inherits from CardCollection class, adds shuffle capability
class Deck:
	def __init__(self):
		self.cards = []
		for suit in range(1, 5):
			for rank in range(1,14):
				self.cards.append(Card(rank, suit))
				
	def shuffle(self):
		random.shuffle(self.cards)
		
	def cardsLeft(self):
		return len(self.cards)
		
	def getTopCard(self):
		return self.cards.pop(0)

	def peekTopCard(self):
		return copy.copy(self.cards[0])

