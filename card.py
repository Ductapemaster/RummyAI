class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		
	def __repr__(self):
		# Define face cards
		letters = {1:'A', 11:'J', 12:'Q', 13:'K'}
		# Return face card rank if in dict, otherwise return string of the rank (2-9)
		letter = letters.get(self.rank, str(self.rank))
		return "<Card %s %s>" % (letter, self.suit)
		
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.suit == other.suit and self.rank == other.rank
		else:
			return False

