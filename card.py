#null card is rank = 0, suit = 0

class Card:
	def __init__(self, rank=0, suit=0):
		self.rank = rank
		self.suit = suit
		
	def __repr__(self):
		# Define face cards
		face_cards = {1:'A', 11:'J', 12:'Q', 13:'K'}
		# Define suits, 0 is a null suit
		suits = {0: '0', 1: 'S', 2: 'H', 3: 'C', 4: 'D'}
		# Return face card rank if in dict, otherwise return string of the rank (2-9)
		readable_rank = face_cards.get(self.rank, str(self.rank))
		readable_suit = suits.get(self.suit)
		return "<%s %s>" % (readable_rank, readable_suit)
		
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.suit == other.suit and self.rank == other.rank
		else:
			return False


	def numPoints(self):
		if self.rank > 9:
			return 10
		elif self.rank == 1:
			return 15
		else:
			return 5

