from card import *

class Player:
	def __init__(self):
		self.hand = []
		self.board = []
	
	def discard(self, card):
		try:
			i = self.hand.index(card)
			#self.hand.remove(card)
		except ValueError:
			return [False, Card()]
		return [True, self.hand.pop(i)]

	def draw(self, card):
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
		copy.hand = [Card()]*len(self.hand)
		copy.board = self.board.copy()
		return copy

