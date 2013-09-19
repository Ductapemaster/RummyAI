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
		
	def __repr__(self):
		string = ""
		for idx in range(0,52):
			string += "%d: %s\n" %(idx + 1, self.cards[idx])
		return string


class NullDeck():
	def __init__(self, cards_left=0):
		self.cards = []
		self.cards_left= cards_left;

	def cardsLeft(self):
		return self.cards_left
	
	def __repr__(self):
		string = ""
		for idx in range(0,52):
			string += "%d: %s\n" %(idx + 1, self.cards[idx])
		return string
