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

	def __repr__(self):
		draw_pile_str = "Draw Pile:\n\tCards Left: %d\n\n" % (self.draw_pile.cardsLeft())

		discard_pile_str = "Discard Pile:\n\t"
		for c in self.discard_pile:
			discard_pile_str += c.__repr__() + ", "
		discard_pile_str += "\n\n"

		player_str = ""
		for p in range(len(self.players)):
			player_str += "Player %d:\n\tBoard:\n" % (p+1)
			#print melds	
			player_str += "\n\tHand:\n"
			#print hand	

		return draw_pile_str + discard_pile_str + player_str


	def numPlayers(self):
		return len(self.players)

