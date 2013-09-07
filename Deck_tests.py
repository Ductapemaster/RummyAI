import unittest

from deck import *
from card import *

class CardTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor(self):
		test_deck = []
		for suit in range(1, 5):
			for rank in range (1, 14):
				test_deck.append(Card(rank, suit))
		d = Deck()
		self.assertEqual(d.cardsLeft(), 52)
		self.assertEqual(d.deck.cards, test_deck)
		
	def test_shuffle(self):
		d = Deck()
		d.shuffle()
		self.assertEqual(d.cardsLeft(), 52)
		
	def test_get_top_card(self):
		d = Deck()
		d.shuffle()
		top_card_test = d.deck.cards[0]
		self.assertEqual(d.getTopCard(), top_card_test)
		self.assertEqual(d.cardsLeft(), 51)

if __name__ == '__main__':
	unittest.main()

