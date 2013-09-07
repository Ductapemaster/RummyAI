class Game:
	def __init__(self, numPlayers):
		# Instantiate new deck and shuffle it
		self.deck = Deck()
		self.deck.shuffle()
		
		# Define lists for players and the draw pile
		self.players = []
		self.drawPile = []
		
		for num in range(numPlayers):
			self.players.append(RummyPlayer())

		self.deck.dealHands(7, self.players)
		self.drawPile.append(self.deck.getTopCard())