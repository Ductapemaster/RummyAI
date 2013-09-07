import unittest

from card import *

class CardTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor_works_as_expected(self):
		rank = 1
		suit = 2
		c = Card(rank, suit)
		self.assertEqual(c.rank, rank)
		self.assertEqual(c.suit, suit)
	
	def test_constructor_with_face_card(self):
		rank = 12
		suit = 2
		c = Card(rank, suit)
		self.assertEqual(c.rank, rank)
		self.assertEqual(c.suit, suit)
		
	def test_constructor_with_null_card(self):
		rank = 0
		suit = 0
		c = Card(rank, suit)
		self.assertEqual(c.rank, rank)
		self.assertEqual(c.suit, suit)

if __name__ == '__main__':
	unittest.main()

