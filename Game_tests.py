import unittest

from game import *

class GameTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor_creates_the_correct_number_of_players(self):
		numPlayers = 3
		g = Game(numPlayers)
		self.assertEqual(len(g.players), numPlayers)
		self.assertEqual(g.numPlayers(), numPlayers)


	def test_constructor_deals_the_correct_number_of_cards(self):
		numPlayers = 3
		g = Game(numPlayers)
		self.assertEqual(g.draw_pile.cardsLeft(), 52 - 7*numPlayers - 1)
		self.assertEqual(len(g.discard_pile), 1)


	def test_getPlayersCopyForAgent_returns_null_cards_for_appropriate_players(self):
		numPlayers = 3
		g = Game(numPlayers)

		agent_num = 2
		pc = g.getPlayersCopyForAgent(agent_num)
		
		for i in range(numPlayers):
			for c in range(len(pc[i].hand)):
				if i != agent_num:
					self.assertEqual(pc[i].hand[c], Card())
				else:
					self.assertEqual(pc[i].hand[c], g.players[i].hand[c])

if __name__ == '__main__':
	unittest.main()

