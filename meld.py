from card import *
from operator import attrgetter

# Create isStraight() function with a default argument equal to self.cards for list to check?
# Create property in Cards class for 'alternate value' for the Ace?
# 	- Could reuse for the Joker, where it is set to the value the joker is representing
# 	- Could cause an issue with the AI setting the alternate value to anything - need check to see that its only set
#		on the aces and the jokers

class Meld:
	def __init__(self, cards=[]):
		
		self.cards = cards
		# initial sort
		self.sortCardsByRank()
		
		self.length = len(self.cards)
		
		# Meld Type:
		# 0: not set
		# 1: set
		# 2: run
		self.meld_type = 0
		
		# A valid meld is either a single card, a two card straight,
		# or any independent meld
		self.valid = False
		
		# An independent meld is a valid meld of 3 or more cards
		self.independent = False
		
		if (len(self.cards) > 0):
			# Check meld properties
			self.straight = self.isStraight()
			self.same_suit = self.isSameSuit()
			self.same_rank = self.isSameRank()
			
			# Validates for straights and single cards
			if (self.straight and self.same_suit):
				self.valid = True
				self.value = self.getMeldValue()
				#independent = len(self.cards) >= 3
				if (len(self.cards) == 1):
					self.meld_type = 0
				elif (len(self.cards) == 2):
					self.meld_type = 2
				else:
					self.meld_type = 2
					self.independent = True
				#print ("\nrank: %s suit: %s straight: %s indep: %s\n%s" %(self.same_rank, self.same_suit, self.straight, self.independent, self.cards))
			
			# Validates for runs (always 3 or more cards)
			elif (self.same_rank and len(self.cards) >= 3):
				self.valid = True
				self.value = self.getMeldValue()
				self.independent = True
				self.meld_type = 1
				#print ("\nrank: %s suit: %s straight: %s indep: %s\n%s" %(self.same_rank, self.same_suit, self.straight, self.independent, self.cards))
				
			# Otherwise meld is invalid
			else:
				self.valid = False
				self.value = 0
				self.independent = False
				self.meld_type = 0	
				
		
		#print ("meld type: %s" %(self.meld_type))
		
	def __repr__(self):
		meld_str = ""
		for card in self.cards:
			meld_str += "%s" % card
		return meld_str
		
	def sortCardsByRank(self):
		self.cards = sorted(self.cards, key=attrgetter('suit', 'rank'))
		
	def sortCardsByAltRank(self):
		self.cards = sorted(self.cards, key=attrgetter('suit', 'alt_rank'))

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
		# Start at index 1
		for idx in range(1, len(self.cards)):
			if self.cards[idx].rank != self.cards[idx-1].rank + 1:
				# Resort by alternate rank and recheck straight
				self.sortCardsByAltRank()
				for idx in range(1, len(self.cards)):
					if self.cards[idx].alt_rank != self.cards[idx-1].alt_rank + 1:
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
			
	def setMeldTypeManual(self, type):
		# If meld type is already set to 1 or 2, return false
		if self.meld_type > 0:
			return False
		# Check for valid meld type argument, if correct, set it
		elif type in range(1,3):
			self.meld_type = type
			return True
		# Any other case, raise an exception
		else:
			raise ("SetInvalidMeldTypeException")
		
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
		if (test_meld.valid and (meld_on_board.meld_type == self.meld_type)):
			return True
		else:
			return False

