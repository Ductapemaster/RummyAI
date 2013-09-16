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

	def test_discard_returns_false_if_card_is_not_in_hand(self):
		p = Player()
		c1 = Card(2,3)
		c2 = Card(5,2)
		c3 = Card(3,4)
		nc = Card()

		p.draw(c1)
		p.draw(c2)

		self.assertEqual(p.discard(c3)[0], False)
		self.assertEqual(p.discard(c3)[1], nc)
		self.assertEqual(p.discard(nc)[0], False)
		self.assertEqual(p.discard(None)[0], False)
		self.assertEqual(p.discard([])[0], False)
		self.assertEqual(len(p.hand), 2)

	def test_discard_returns_true_and_remvoves_card_if_card_is_not_in_hand(self):
		p = Player()
		c1 = Card(2,3)

		p.draw(c1)

		success, c = p.discard(c1) 
		self.assertEqual(success, True)
		self.assertEqual(c, c1)
		self.assertEqual(len(p.hand), 0)



if __name__ == '__main__':
	unittest.main()

