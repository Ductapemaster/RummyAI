#null card is rank = 0, suit = 0

class Card:

	# Define face cards
	face_cards = {-1: 'NUL', 1:'AL ', 10: '10 ', 11:'J  ', 12:'Q  ', 13:'K  ', 14:'AH ', 20:'JKR'}
	# Define suits, 0 is a null suit
	suits = {-1: 'N', 1: 'S', 2: 'H', 3: 'C', 4: 'D'}

	def __init__(self, rank=-1, suit=-1):
		self.rank = rank
		self.suit = suit
		self.alt_rank = rank
		if rank == 1:
			self.alt_rank = 14
		
	def __repr__(self, debug=False):
		# Return face card rank if in dict, otherwise return string of the rank (2-9)
		readable_rank = self.face_cards.get(self.rank, str(self.rank) + '  ')
		readable_alt_rank = self.face_cards.get(self.alt_rank, str(self.alt_rank) + '  ')
		readable_suit = self.suits.get(self.suit)
		if(debug): 
			return "<%s %s %s>" % (readable_rank, readable_alt_rank, readable_suit)
		else:
			return "<%s %s>" % (readable_rank, readable_suit)
		
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.suit == other.suit and self.rank == other.rank
		else:
			return False


	def numPoints(self):
		if self.rank > 9 and self.rank < 14:
			return 10
		elif self.rank == 1:
			return 15
		elif self.rank == 20:
			return 20
		elif self.rank == -1:
			return 0
		else:
			return 5

