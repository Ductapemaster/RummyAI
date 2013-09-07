from player import *
from deck import *

class Game:
	def __init__(self, numPlayers):
		# Instantiate new deck and shuffle it
		self.deck = Deck()
		self.deck.shuffle()
		
		# Define lists for players and the draw pile
		self.players = []
		self.drawPile = []
		
		
		for num in range(numPlayers):
			self.players.append(Player())

		self.deck.dealHands(7, self.players)
		self.drawPile.append(self.deck.getTopCard())

	def numPlayers(self):
		return len(self.players)
