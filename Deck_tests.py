import unittest

from deck import *

class DeckTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor(self):
		test_deck = []
		for suit in range(1, 5):
			for rank in range (1, 14):
				test_deck.append(Card(rank, suit))
		d = Deck()
		self.assertEqual(d.numCards(), 52)
		self.assertEqual(d.cards, test_deck)
		
	def test_shuffle(self):
		d = Deck()
		d.shuffle()
		self.assertEqual(d.numCards(), 52)

if __name__ == '__main__':
	unittest.main()

