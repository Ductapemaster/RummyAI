import random

from iAgent import *
from game import *


class GameRunner():

	def __init__(self):
		pass

	def createNewGame(self, agents, starting_player=1):
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

			draw = self.agents[cur_player].getDrawAction()

			if self.game.applyDrawAction(cur_player, draw) == False:
				return False

			# update agent with new game info
			self.updateAgentWithGameState(self, cur_player)


			meld = self.agents[cur_player].getMeldActions()

			# verify meld is vaild

			# make the meld action happen

			self.agents[cur_player].getDiscardAction() 

			# verify discard is vaild

			# make the discard action happen


			# if self.game.player[cur_player].hand.size() == 0:
				#self.winner = cur_player
				#break

			
			self.updateAgentsWithGameState()

			# let the next player go
			cur_player = (cur_player + 1) % self.num_players

			# temporary, to prevent infinite loop
			break


	def updateAgentWithGameState(self, agent_number):
			game_copy = self.game.getSanitizedCopy(agent_number)
			self.agents[agent_number].updateGameState(game_copy)
			
	def updateAgentsWithGameState(self):
		for i in range(self.num_players):
			self.updateAgentWithGameState(i)

