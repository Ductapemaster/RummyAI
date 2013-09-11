
class IAgent():

	def setPlayerNumber(self, player_number):
		self.player_number = player_number

	def updateGameState(self, game):
		pass

	def getDrawAction(self):
		# Return an integer
		#	0 to draw off of the draw pile
		#	N to pickup N cards from the discard pile
		#		You must meld the last card you pick up
		#		If you do not, you lose immediately, cheater
		
		pass

	def getMeldActions(self):
		# Return a list of meld objects, or an empty list
		#	the melds must consist of cards in your hand
		pass
	
	def getDiscardAction(self):
		# Return a card that exists in your hand
		#	If the card does not exist in your hand
		#	you lose immediately, cheater
		pass
