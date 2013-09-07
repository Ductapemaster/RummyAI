import unittest

from card import *

class PlayerTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor_works_as_expected(self):
		rank = 1
		suit = 2
		c = Card(rank, suit)
		self.assertEqual(c.rank, rank)
		self.assertEqual(c.suit, suit)

if __name__ == '__main__':
	unittest.main()

