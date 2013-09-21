import random

from iAgent import *
from humanAgent import *
from game import *

class GamePackage():

	def __init__(self, agents, starting_player=0):
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


	def updateAgentWithGameState(self, agent_number):
			game_copy = self.game.getSanitizedCopy(agent_number)
			self.agents[agent_number].updateGameState(game_copy)
			
	def updateAgentsWithGameState(self):
		for i in range(self.num_players):
			self.updateAgentWithGameState(i)

class GameRunner():

	def __init__(self):
		pass

	def playGame(self, game_pkg):

		cur_player = game_pkg.starting_player
		
		while True:

			# Draw Phase

			draw = game_pkg.agents[cur_player].getDrawAction()

			success = game_pkg.game.applyDrawAction(cur_player, draw)
			if not success:
				return False

			game_pkg.updateAgentWithGameState(cur_player)


			# Meld Phase

			melds = game_pkg.agents[cur_player].getMeldActions()

			success = game_pkg.game.applyMeldAction(cur_player, melds)
			if not success:
				return False

			game_pkg.updateAgentWithGameState(cur_player)

			# Discard Phase

			discard = game_pkg.agents[cur_player].getDiscardAction() 

			success = game_pkg.game.applyDiscardAction(cur_player, discard)
			if not success:
				return False

			game_pkg.updateAgentsWithGameState()

			# Check for win condition

			if len(game_pkg.game.players[cur_player].hand) == 0:
				game_pkg.winner = cur_player
				break

			# let the next player go
			cur_player = (cur_player + 1) % game_pkg.num_players


