from card import *
from operator import attrgetter

class Meld:
	def __init__(self, card_list=[]):
		
		self.card_list = sorted(card_list, key=attrgetter('suit', 'rank'))
		
		# Meld Type:
		# 0: don't care (play anywhere valid)
		# 1: set
		# 2: run
		self.meld_type = 0
		
	def isIndependentMeld(self):
		if len(self.card_list) < 3: 
			return False
		else:
			
			same_rank = True
			for c in self.card_list:
				if c.rank != self.card_list[0].rank: 
					same_rank = False
					break
			
			same_suit = True
			for c in self.card_list:
				if c.suit != self.card_list[0].suit: 
					same_suit = False
					break
					
			is_straight = True
			for idx in range(len(self.card_list)):
				if idx != 0:
					if self.card_list[idx].rank != self.card_list[idx-1].rank + 1:
						is_straight = False
						break
			
			if same_rank:
				return True
			elif (same_suit and is_straight):
				return True
			else: 
				return False
		
	def getMeldValue(self):
		points = 0
		for c in self.card_list:
			points += c.numPoints()
		return points