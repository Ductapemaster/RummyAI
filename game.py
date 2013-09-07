from player import *
from deck import *

class Game:
	def __init__(self, numPlayers):
		# Instantiate new deck and shuffle it
		self.draw_pile = Deck()
		self.draw_pile.shuffle()
		
		# Define lists for players and populate it
		self.players = []
		for num in range(numPlayers):
			self.players.append(Player())

		# deal 7 cards to each player
		for i in range(7):
			for player in self.players:
				player.hand.append(self.draw_pile.getTopCard())

		# create a discard pile and add one card to it
		self.discard_pile = []
		self.discard_pile.append(self.draw_pile.getTopCard())

	def numPlayers(self):
		return len(self.players)

