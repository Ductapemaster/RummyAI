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

		self.agents = agents

		self.game = Game(self.num_players)

		self.starting_player = starting_player
		self.winner = -1
		
		


	def playGame(self):

		cur_player = self.starting_player
		
		while True:

			draw = self.agents[cur_player].getDrawAction()

			# verify draw is vaild

			# make the draw action happen

			meld = self.agents[cur_player].getMeldActions()

			# verify meld is vaild

			# make the meld action happen

			self.agents[cur_player].getDiscardAction() 

			# verify discard is vaild

			# make the discard action happen


			# if self.game.player[cur_player].hand.size() == 0:
				#self.winner = cur_player
				#break


			# let the next player go
			cur_player = (cur_player + 1) % self.num_players

			# temporary, to prevent infinite loop
			break


			

