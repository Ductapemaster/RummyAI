from card import *
from operator import *

class Meld:
	def __init__(self, card_list=[]):
		
		self.card_list = sorted(card_list, key=attrgetter('suit', 'rank'))
		
		# Meld Type:
		# 0: don't care (play anywhere valid)
		# 1: set
		# 2: run
		self.meld_type = 0
		
	def isIndependentMeld(self):
		if len(card_list) < 3: return False
		else: return True
		
	def getMeldValue(self):
		points = 0
		for c in self.card_list:
			points += c.numPoints()
		return points