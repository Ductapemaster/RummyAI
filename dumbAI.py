import random

class dumbAI():

	def getDrawAction(self):
		return 0

	def getMeldActions(self):
		return []

	def getDiscardAction(self):
		return random.randint(0, len(self.game.players[self.player_num].hand))
