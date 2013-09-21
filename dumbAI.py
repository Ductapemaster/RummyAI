import random

from iAgent import *

class DumbAI(IAgent):

	def getDrawAction(self):
		return 0

	def getMeldActions(self):
		return []

	def getDiscardAction(self):
		rand_index = random.randint(0, len(self.game.players[self.player_number].hand))
		return self.game.players[self.player_number].hand[rand_index]
