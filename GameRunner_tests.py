import unittest

from GameRunner import *

class CardTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor_works_as_expected(self):
		gr = GameRunner()
	
	def test_createNewGame_works_as_expected(self):
		gr = GameRunner()

		agents = []
		agents.append(IAgent())
		agents.append(IAgent())

		gr.createNewGame(agents)

		self.assertEqual(gr.num_players, len(agents))
		self.assertEqual(gr.agents, agents)
		self.assertEqual(type(gr.game), Game)
		self.assertEqual(gr.game.numPlayers(), gr.num_players)


	def test_createNewGame_raises_exception_if_no_agents(self):
		gr = GameRunner()
		agents = []

		self.assertRaises(ValueError, gr.createNewGame, agents)

	def test_createNewGame_raises_exception_if_one_agents(self):
		gr = GameRunner()
		agents = []
		agents.append(IAgent())

		self.assertRaises(ValueError, gr.createNewGame, agents)
	



if __name__ == '__main__':
	unittest.main()

