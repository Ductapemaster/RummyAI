import unittest

from cardCollection import *

class CardTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor_and_is_empty_method(self):
		cc = CardCollection()
		self.assertEqual(cc.isEmpty(), True)

	def test_add_card_method_with_non_face_card(self):
		cc = CardCollection()
		test_card = Card(2, 'H')
		cc.addCard(test_card)
		self.assertEqual(cc.cards, [test_card])
	
	def test_add_card_method_with_face_card(self):
		cc = CardCollection()
		test_card = Card(1, 'S')
		cc.addCard(test_card)
		self.assertEqual(cc.cards, [test_card])
		
	def test_add_card_method_with_multiple_cards(self):
		cc = CardCollection()
		test_cards = [Card(2, 'H'), Card(13, 'D'), Card(7, 'S'), Card(1, 'C')]
		for c in test_cards:
			cc.addCard(c)
		for idx in range(5):
			self.assertEqual(cc.cards[idx], test_cards[idx])
		
	def test_make_empty_method_with_one_card(self):
		cc = CardCollection()
		test_card = Card(7, 'S')
		cc.addCard(test_card)
		cc.makeEmpty()
		self.assertEqual(cc.isEmpty(), True)
		
	def test_make_empty_method_with_multiple_cards(self):
		cc = CardCollection()
		test_cards = [Card(2, 'H'), Card(13, 'D'), Card(7, 'S'), Card(1, 'C')]
		for c in test_cards:
			cc.addCard(c)
		cc.makeEmpty()
		self.assertEqual(cc.isEmpty(), True)
		
	def test_pop_card_method_without_index(self):
		cc = CardCollection()
		test_cards = [Card(2, 'H'), Card(13, 'D'), Card(7, 'S'), Card(1, 'C')]
		for c in test_cards:
			cc.addCard(c)
		self.assertEqual(cc.popCard(), test_cards[0])
		
	def test_pop_card_method_with_index(self):
		cc = CardCollection()
		test_cards = [Card(2, 'H'), Card(13, 'D'), Card(7, 'S'), Card(1, 'C')]
		for c in test_cards:
			cc.addCard(c)
		self.assertEqual(cc.popCard(2), test_cards[2])
		
	def test_remove_card_method_with_one_card(self):
		cc = CardCollection()
		test_card = Card(7, 'S')
		cc.addCard(test_card)
		self.assertEqual(cc.removeCard(test_card), test_card)
		
	def test_remove_card_method_with_nonexistent_card(self):
		cc = CardCollection()
		test_card = Card(7, 'S')
		absent_card = Card(2, 'C')
		cc.addCard(test_card)
		self.assertEqual(cc.removeCard(absent_card), False)
		
	def test_remove_card_method_with_multiple_cards(self):
		cc = CardCollection()
		test_cards = [Card(2, 'H'), Card(13, 'D'), Card(7, 'S'), Card(1, 'C')]
		for c in test_cards:
			cc.addCard(c)
		self.assertEqual(cc.removeCard(test_card[1]), test_card[1])
		self.assertEqual(cc.removeCard(test_card[0]), test_card[0])
		
if __name__ == '__main__':
	unittest.main()

