import random

from iAgent import *
from humanAgent import *
from game import *


class GameRunner():

	def __init__(self):
		pass

	def createNewGame(self, agents, starting_player=0):
		self.num_players = len(agents)

		if self.num_players < 2:
			raise ValueError("Not enough players!")

		# Setup the game
		self.game = Game(self.num_players)

		# Setup the agents
		self.agents = agents
		for i in range(self.num_players):
			self.agents[i].setPlayerNumber(i)

		self.updateAgentsWithGameState()

		# set some internal variables
		self.starting_player = starting_player
		self.winner = -1


	def playGame(self):

		cur_player = self.starting_player
		
		while True:

			# Draw Phase

			draw = self.agents[cur_player].getDrawAction()

			success = self.game.applyDrawAction(cur_player, draw)
			if not success:
				return False

			self.updateAgentWithGameState(cur_player)


			# Meld Phase

			melds = self.agents[cur_player].getMeldActions()

			success = self.game.applyMeldAction(cur_player, melds)
			if not success:
				return False

			# Discard Phase

			discard = self.agents[cur_player].getDiscardAction() 

			success = self.game.applyDiscardAction(discard)
			if not success:
				return False

			self.updateAgentsWithGameState()

			# Check for win condition

			if self.game.player[cur_player].hand.size() == 0:
				self.winner = cur_player
				break

			# let the next player go
			cur_player = (cur_player + 1) % self.num_players


	def updateAgentWithGameState(self, agent_number):
			game_copy = self.game.getSanitizedCopy(agent_number)
			self.agents[agent_number].updateGameState(game_copy)
			
	def updateAgentsWithGameState(self):
		for i in range(self.num_players):
			self.updateAgentWithGameState(i)

	def runHumanVsHumanGame(self, num_humans):

		hu_ags = []
		for i in range(num_humans):
			hu_ags.append(HumanAgent())

		self.createNewGame(hu_ags)

		self.playGame()





