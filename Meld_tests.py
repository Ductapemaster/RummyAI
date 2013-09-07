import unittest

from card import *	
from meld import *

class MeldTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor_with_empty_meld(self):
		m = Meld()
		self.assertEqual(m.getMeldValue(), 0)
		self.assertEqual(len(m.cards), 0)
		self.assertEqual(m.meld_type, 0)
		self.assertEqual(m.isIndependentMeld(), False)
		
	def test_contructor_with_one_card_meld(self):
		test_cards = [Card(4, 2)]
		m = Meld(test_cards)
		self.assertEqual(m.getMeldValue(), test_cards[0].numPoints())
		self.assertEqual(len(m.cards), 1)
		self.assertEqual(m.meld_type, 0)
		self.assertEqual(m.isIndependentMeld(), False)
		
	def test_constructor_with_three_card_meld(self):
		test_cards = [Card(7,1), Card(4,3), Card(12,4)]
		test_value = 20
		m = Meld(test_cards)
		self.assertEqual(m.getMeldValue(), test_value)
		self.assertEqual(len(m.cards), 3)
		self.assertEqual(m.meld_type, 0)
		self.assertEqual(m.isIndependentMeld(), False)
		
	def test_sorting_with_off_suit_straight(self):
		test_cards = [Card(9,1), Card(7,4), Card(8,3)]
		test_cards_sorted = [Card(9,1), Card(8,3), Card(7,4)]
		test_value = 15
		m = Meld(test_cards)
		self.assertEqual(m.cards, test_cards_sorted)
		self.assertEqual(m.getMeldValue(), test_value)
		self.assertEqual(m.isIndependentMeld(), False)
		
	def test_sorting_with_suited_straight(self):
		test_cards = [Card(9,1), Card(7,1), Card(8,1)]
		test_cards_sorted = [Card(7,1), Card(8,1), Card(9,1)]
		test_value = 15
		m = Meld(test_cards)
		self.assertEqual(m.cards, test_cards_sorted)
		self.assertEqual(m.getMeldValue(), test_value)
		self.assertEqual(m.isIndependentMeld(), True)
		
	def test_sorting_with_three_of_a_kind(self):
		test_cards = [Card(13,4), Card(13,1), Card(13,2)]
		test_cards_sorted = [Card(13,1), Card(13,2), Card(13,4)]
		test_value = 30
		m = Meld(test_cards)
		self.assertEqual(m.cards, test_cards_sorted)
		self.assertEqual(m.getMeldValue(), test_value)
		self.assertEqual(m.isIndependentMeld(), True)
		
	def test_independent_meld_method_with_four_of_a_kind(self):
		test_cards = [Card(1,1), Card(1,2), Card(1,3), Card(1,4)]
		test_value = 60
		m = Meld(test_cards)
		self.assertEqual(m.getMeldValue(), test_value)
		self.assertEqual(m.isIndependentMeld(), True)
		
	def test_independent_meld_with_five_card_straight(self):
		test_cards = [Card(1,1), Card(2,1), Card(3,1), Card(4,1), Card(5,1)]
		test_value = 35
		m = Meld(test_cards)
		self.assertEqual(m.getMeldValue(), test_value)
		self.assertEqual(m.isIndependentMeld(), True)

	def test_can_combine_with_method_with_valid_three_plus_one_of_a_kind(self):
		test_cards_1 = [Card(5,1), Card(5,2), Card(5,4)]
		test_cards_2 = [Card(5,3)]
		m = Meld(test_cards_1)
		self.assertEqual(m.canCombineWith(Meld(test_cards_2)), True)
		
	def test_can_combine_with_method_with_valid_three_plus_two_straight(self):
		test_cards_1 = [Card(2,1), Card(1,1), Card(3,1)]
		test_cards_2 = [Card(5,1), Card(4,1)]
		m = Meld(test_cards_1)
		self.assertEqual(m.canCombineWith(Meld(test_cards_2)), True)
		
	def test_can_combine_with_method_with_invalid_three_plus_one_of_a_kind(self):
		test_cards_1 = [Card(5,1), Card(5,2), Card(5,4)]
		test_cards_2 = [Card(11,3)]
		m = Meld(test_cards_1)
		self.assertEqual(m.canCombineWith(Meld(test_cards_2)), False)
		
	def test_can_combine_with_method_with_invalid_three_plus_two_straight(self):
		test_cards_1 = [Card(1,1), Card(2,1), Card(3,1)]
		test_cards_2 = [Card(4,1), Card(6,1)]
		m = Meld(test_cards_1)
		self.assertEqual(m.canCombineWith(Meld(test_cards_2)), False)
	
	def test_can_combine_with_method_with_invalid_run_of_two(self):
		test_card_1 = [Card(1,2)]
		test_card_2 = [Card(2,1)]
		m = Meld(test_card_1)
		self.assertEqual(m.canCombineWith(Meld(test_card_2)), False)
		
	def test_can_combine_with_method_with_valid_run_of_two(self):
		test_card_1 = [Card(12,2)]
		test_card_2 = [Card(13,2)]
		m = Meld(test_card_1)
		self.assertEqual(m.canCombineWith(Meld(test_card_2)), True)
		

if __name__ == '__main__':
	unittest.main()
