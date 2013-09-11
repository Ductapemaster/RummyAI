import unittest

from card import *

class CardTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor_works_as_expected(self):
		rank = 3
		suit = 2
		c = Card(rank, suit)
		self.assertEqual(c.rank, rank)
		self.assertEqual(c.alt_rank, rank)
		self.assertEqual(c.suit, suit)
	
	def test_constructor_with_face_card(self):
		rank = 12
		suit = 3
		c = Card(rank, suit)
		self.assertEqual(c.rank, rank)
		self.assertEqual(c.alt_rank, rank)
		self.assertEqual(c.suit, suit)
		
	def test_constructor_with_ace(self):
		rank = 1
		suit = 2
		c = Card(rank, suit)
		self.assertEqual(c.rank, rank)
		self.assertEqual(c.alt_rank, 14)
		self.assertEqual(c.suit, suit)

	def test_constructor_with_null_card(self):
		c = Card()
		self.assertEqual(c.rank, -1)
		self.assertEqual(c.alt_rank, -1)
		self.assertEqual(c.suit, -1)

	def test_numPoints_returns_5_for_regular_cards(self):
		for r in range(2,10):
			for s in range(1,5):
				c = Card(r, s)
				self.assertEqual(c.numPoints(), 5)

	def test_numPoints_returns_10_for_face_and_10_cards(self):
		for r in range(10,14):
			for s in range(1,5):
				c = Card(r, s)
				self.assertEqual(c.numPoints(), 10)

	def test_numPoints_returns_15_for_ace_cards(self):
		r = 1
		for s in range(1,5):
			c = Card(r, s)
			self.assertEqual(c.numPoints(), 15)

	def test_numPoints_returns_15_for_ace_cards(self):
		r = 20
		for s in range(1,5):
			c = Card(r, s)
			self.assertEqual(c.numPoints(), 20)

if __name__ == '__main__':
	unittest.main()

