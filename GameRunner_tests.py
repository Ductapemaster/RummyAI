import unittest

from gameRunner import *

class GameRunnerTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor_works_as_expected(self):
		gr = GameRunner()
	
	def test_GamePackage_is_constructable(self):

		agents = []
		agents.append(IAgent())
		agents.append(IAgent())

		g = GamePackage(agents)

		self.assertEqual(g.num_players, len(agents))
		self.assertEqual(g.agents, agents)
		self.assertEqual(type(g.game), Game)
		self.assertEqual(g.game.numPlayers(), g.num_players)


	def test_GamePackage_raises_error_if_agent_list_is_empty(self):
		agents = []

		self.assertRaises(ValueError, GamePackage, agents)

	def test_GamePackage_raises_exception_if_one_agents(self):
		agents = []
		agents.append(IAgent())

		self.assertRaises(ValueError, GamePackage, agents)
	



if __name__ == '__main__':
	unittest.main()

