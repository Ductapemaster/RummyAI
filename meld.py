from card import *
from operator import attrgetter

# Need to implement Ace high/low validation
# Go through and check if meld is valid, if its a straight 
# and it has an ace, change the ace rank to 14 and re-validate

# Create isStraight() function with a default argument equal to self.cards for list to check?
# Create property in Cards class for 'alternate value' for the Ace?
# 	- Could reuse for the Joker, where it is set to the value the joker is representing
# 	- Could cause an issue with the AI setting the alternate value to anything - need check to see that its only set
#		on the aces and the jokers

class Meld:
	def __init__(self, cards=[]):
		
		self.cards = self.sortCards(cards)
		
		# Meld Type:
		# 0: don't care (play anywhere valid)
		# 1: set
		# 2: run
		self.meld_type = 0
	
	def sortCards(self, cardList):
		return sorted(cardList, key=attrgetter('suit', 'rank'))

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
		# Check if all cards are the same suit and if an Ace has been 
		# sorted into the first index of the cards list
		elif (self.isSameSuit() and self.cards[0].rank == 1):
			# - Create an ace with a rank of 14 instead of 1
			# - Make temporary card list containing high ace instead of the low ace
			# - Sort temp list
			# - Check if its a straight
			temp_high_ace = Card(14, self.cards[0].suit)
			temp_cards = [temp_high_ace]
			temp_cards.extend(self.cards[1:])
			# switch internal cards list to new temporary list
			temp = self.cards
			self.cards = self.sortCards(temp_cards)
			if self.isStraight():
				# Replace internal list with original list
				self.cards = temp
				return True
		return False
		
	def isIndependentMeld(self):
		#print ("\nisIndependentMeld()")
		#print (self.cards)
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
		combined_cards = self.cards.copy()
		combined_cards.extend(meld_on_board.cards)
		test_meld = Meld(combined_cards)
		return test_meld.isValidMeld()
