import random

class Deck:
	def __init__(self):
		self.deck = []
		for suit in 'SCHD':
			for rank in range(1,14):
				self.deck.append(Card(rank, suit))
				
	def __repr__(self):
		outputStr = ""
		for card in self.deck:
			outputStr += card.__repr__()
			outputStr += "\n"
		return outputStr
	
	def shuffle(self):
		random.shuffle(self.deck)
		
	# Take in an array of players and deal them all hands with the specified number of cards
	def dealHands(self, num, playerList):
		for i in range(num):
			for player in playerList:
				player.hand.append(self.deck.pop())
	
	# Pop off the top card of the deck and return it
	def getTopCard(self):
		return self.deck.pop()