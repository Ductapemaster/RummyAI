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



if __name__ == '__main__':
    unittest.main()

