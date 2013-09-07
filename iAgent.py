
class IAgent():

	def setPlayerNumber(self, player_number):
		self.player_number = player_number

	def updateGameState(self, players, discard_pile):
		pass

	def getDrawAction(self):
		pass

	def getMeldActions(self):
		pass
	
	def getDiscardAction(self):
		pass
