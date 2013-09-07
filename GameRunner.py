from IAgent import IAgent
from Game import *

class GameRunner():

	def __init__(self):
		pass

	def createNewGame(self, agents):
		self.num_players = len(agents)

		if self.num_players < 2:
			raise ValueError("Not enough players!")

		self.agents = agents

		self.game = Game(self.num_players)
