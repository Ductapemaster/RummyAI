import random
from cardCollection import *

# Inherits from CardCollection class, adds shuffle capability
class Deck(CardCollection):
	def __init__(self):
		super().__init__()
		for suit in range(1, 5):
			for rank in range(1,14):
				self.addCard(Card(rank, suit))
				
	def shuffle(self):
		random.shuffle(self.cards)

