import unittest

from game import *

class GameTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_constructor_works_as_expected(self):
        numPlayers = 3
        g = Game(numPlayers)
        self.assertEqual(len(g.players), numPlayers)

    def test_dealHands_works_as_expected(self):
        numPlayers = 3
        numCards = 7
        g = Game(numPlayers)
        self.assertEqual(len(g.deck.deck), 52-(numPlayers*numCards)-1)

if __name__ == '__main__':
    unittest.main()

