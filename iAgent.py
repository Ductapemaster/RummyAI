
class IAgent():

	def setPlayerNumber(self, player_number):
		self.player_number = player_number

	def updateGameState(self, game):
		pass

	def getDrawAction(self):
		#return an integer
		# 0 to draw off of the draw pile
		# N to pickup N cards from the discard pile
		pass

	def getMeldActions(self):
		pass
	
	def getDiscardAction(self):
		pass
