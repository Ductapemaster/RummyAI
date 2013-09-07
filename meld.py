from card import *
from operator import attrgetter

# Need to implement Ace high/low validation
# Go through and check if meld is valid, if its a straight 
# and it has an ace, change the ace rank to 14 and re-validate

class Meld:
	def __init__(self, cards=[]):
		
		self.cards = sorted(cards, key=attrgetter('suit', 'rank'))
		
		# Meld Type:
		# 0: don't care (play anywhere valid)
		# 1: set
		# 2: run
		self.meld_type = 0
		
	def isSameRank(self):
		same_rank = True
		for c in self.cards:
			if c.rank != self.cards[0].rank: 
				same_rank = False
				
		return same_rank
		
	def isSameSuit(self):
		same_suit = True
		for c in self.cards:
			if c.suit != self.cards[0].suit: 
				same_suit = False

		return same_suit

	def isStraight(self):
		is_straight = True
		for idx in range(len(self.cards)):
			if idx != 0:
				if self.cards[idx].rank != self.cards[idx-1].rank + 1:
					is_straight = False
					break
					
		return is_straight
		
	def isValidMeld(self):
		if self.isSameRank() or (self.isSameSuit() and self.isStraight()):
			return True
		return False
		
	def isIndependentMeld(self):
		if len(self.cards) < 3: 
			return False
		return self.isValidMeld()
		
	def getMeldValue(self):
		points = 0
		for c in self.cards:
			points += c.numPoints()
		return points

	# Checks if meld instance can be combined with a valid meld 
	# from the board and results in a valid meld
	def canCombineWith(self, meld_on_board):
		combined_cards = self.cards
		combined_cards.extend(meld_on_board)
		test_meld = Meld(combined_cards)
		return test_meld.isValidMeld()