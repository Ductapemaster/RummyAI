import unittest

from player import *

class PlayerTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor_works_as_expected(self):
		p = Player()
		self.assertEqual(p.hand, [])
		self.assertEqual(p.board, [])

	def test_draw_adds_the_card_its_hand(self):
		p = Player()
		c = Card(2,3)

		p.draw(c)

		self.assertEqual(len(p.hand), 1)
		self.assertEqual(p.hand[0], c)

	def test_getCopy_returns_a_copy(self):
		p = Player()
		c = Card(2,3)

		p.draw(c)

		copy = p.getCopy()
		self.assertEqual(len(copy.hand), len(p.hand))
		self.assertEqual(copy.hand[0], p.hand[0])

	def test_getCopyNullHand_returns_a_copy(self):
		p = Player()
		c = Card(2,3)
		nc = Card()

		p.draw(c)

		copy = p.getCopyNullHand()
		self.assertEqual(len(copy.hand), len(p.hand))
		self.assertEqual(copy.hand[0], nc)

if __name__ == '__main__':
	unittest.main()

