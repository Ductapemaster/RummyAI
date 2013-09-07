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


	def test_getSanitizedCopy_hides_cards(self):
		numPlayers = 3
		g = Game(numPlayers)

		agent_num = 2
		copy = g.getSanitizedCopy(agent_num)
		
		for i in range(numPlayers):
			for c in range(len(copy.players[i].hand)):
				if i != agent_num:
					self.assertEqual(copy.players[i].hand[c], Card())
				else:
					self.assertEqual(copy.players[i].hand[c], g.players[i].hand[c])

		for c in copy.draw_pile:
			self.assertEquals(c, Card())



if __name__ == '__main__':
	unittest.main()

