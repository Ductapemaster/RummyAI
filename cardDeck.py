import random

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
		
class Deck:
	def __init__(self):
		self.deck = []
		for suit in 'SCHD':
			for rank in range(1,14):
				self.deck.append(Card(rank, suit))
				
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
		
class RummyPlayer:
	def __init__(self):#, number):
		#self.pNum = number
		self.hand = []
		self.board = []
	
	def discard(self, cardIndex):
		return self.hand.pop(cardIndex)
	
class Rummy:
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

