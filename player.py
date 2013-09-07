from card import *

class Player:
	def __init__(self):
		self.hand = []
		self.board = []
	
	def discard(self, card):
		return self.hand.remove(card)

	def addCardToHand(self, card):
		self.hand.append(card)

	def getNullHandCopy(self):
		null_hand = []
		return null_hand

	def getCopy(self):
		copy = Player()
		copy.hand = self.hand.copy()
		copy.board = self.board.copy()
		return copy

	def getCopyNullHand(self):
		copy = Player()
		for i in range(len(self.hand)):
			copy.hand.append(Card())
		copy.board = self.board.copy()
		return copy
