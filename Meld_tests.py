import unittest

from card import *	
from meld import *

class MeldTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor_with_empty_meld(self):
		m = Meld()
		self.assertEqual(len(m.cards), 0)
		self.assertEqual(m.independent, False)
		
	def test_contructor_with_one_card_meld(self):
		test_cards = [Card(4, 2)]
		m = Meld(test_cards)
		self.assertEqual(m.value, test_cards[0].numPoints())
		self.assertEqual(len(m.cards), 1)
		self.assertEqual(m.meld_type, 0)
		self.assertEqual(m.independent, False)
		
	def test_constructor_with_three_card_meld(self):
		test_cards = [Card(7,1), Card(4,3), Card(12,4)]
		test_value = 20
		m = Meld(test_cards)
		self.assertEqual(m.independent, False)
		self.assertEqual(m.valid, False)
		
	def test_sorting_with_off_suit_straight(self):
		test_cards = [Card(9,1), Card(7,4), Card(8,3)]
		test_cards_sorted = [Card(9,1), Card(8,3), Card(7,4)]
		test_value = 15
		m = Meld(test_cards)
		self.assertEqual(m.cards, test_cards_sorted)
		self.assertEqual(m.independent, False)
		self.assertEqual(m.valid, False)
		
	def test_sorting_with_suited_straight(self):
		test_cards = [Card(9,1), Card(7,1), Card(8,1)]
		test_cards_sorted = [Card(7,1), Card(8,1), Card(9,1)]
		test_value = 15
		m = Meld(test_cards)
		self.assertEqual(m.cards, test_cards_sorted)
		self.assertEqual(m.value, test_value)
		self.assertEqual(m.independent, True)
		self.assertEqual(m.valid, True)
		
	def test_sorting_with_three_of_a_kind(self):
		test_cards = [Card(13,4), Card(13,1), Card(13,2)]
		test_cards_sorted = [Card(13,1), Card(13,2), Card(13,4)]
		test_value = 30
		m = Meld(test_cards)
		self.assertEqual(m.cards, test_cards_sorted)
		self.assertEqual(m.value, test_value)
		self.assertEqual(m.independent, True)
		self.assertEqual(m.valid, True)
		
	def test_independent_meld_method_with_four_of_a_kind(self):
		test_cards = [Card(1,1), Card(1,2), Card(1,3), Card(1,4)]
		test_value = 60
		m = Meld(test_cards)
		self.assertEqual(m.value, test_value)
		self.assertEqual(m.independent, True)
		self.assertEqual(m.valid, True)
		
	def test_independent_meld_with_five_card_straight(self):
		test_cards = [Card(1,1), Card(2,1), Card(3,1), Card(4,1), Card(5,1)]
		test_value = 35
		m = Meld(test_cards)
		self.assertEqual(m.meld_type, 2)
		self.assertEqual(m.value, test_value)
		self.assertEqual(m.independent, True)
		self.assertEqual(m.valid, True)

	def test_can_combine_with_method_with_valid_three_plus_one_of_a_kind(self):
		test_cards_1 = [Card(5,1), Card(5,2), Card(5,4)]
		test_cards_2 = [Card(5,3)]

		mob = Meld(test_cards_1)
		m = Meld(test_cards_2)
		
		self.assertEqual(mob.meld_type, 1)
		self.assertEqual(m.canCombineWith(mob), False)		
		
		self.assertEqual(m.setMeldTypeManual(1), True)
		self.assertEqual(m.canCombineWith(mob), True)
		
	def test_setting_meld_type_manually_twice(self):
		test_cards_1 = [Card(5,1), Card(5,2), Card(5,4)]
		test_cards_2 = [Card(5,3)]

		mob = Meld(test_cards_1)
		m = Meld(test_cards_2)
		
		self.assertEqual(mob.meld_type, 1)
		self.assertEqual(m.canCombineWith(mob), False)		
		
		self.assertEqual(m.setMeldTypeManual(2), True)
		self.assertEqual(m.canCombineWith(mob), False)
		
		# Trying to set meld_type a second time should fail
		self.assertEqual(m.setMeldTypeManual(1), False)
		self.assertEqual(m.canCombineWith(mob), False)		

	def test_can_combine_with_method_with_valid_three_plus_two_straight(self):
		test_cards_1 = [Card(2,1), Card(1,1), Card(3,1)]
		test_cards_2 = [Card(5,1), Card(4,1)]
		m = Meld(test_cards_1)
		mob = Meld(test_cards_2)

		self.assertEqual(m.canCombineWith(mob), True)
		
	def test_can_combine_with_method_with_invalid_three_plus_one_of_a_kind(self):
		test_cards_1 = [Card(5,1), Card(5,2), Card(5,4)]
		test_cards_2 = [Card(11,3)]
		m = Meld(test_cards_1)
		mob = Meld(test_cards_2)
		mob.setMeldTypeManual(1)
		self.assertEqual(m.canCombineWith(mob), False)
		
	def test_can_combine_with_method_with_invalid_three_plus_two_straight(self):
		test_cards_1 = [Card(1,1), Card(2,1), Card(3,1)]
		test_cards_2 = [Card(4,1), Card(6,1)]
		m = Meld(test_cards_1)
		mob = Meld(test_cards_2)
		mob.setMeldTypeManual(2)
		self.assertEqual(m.canCombineWith(mob), False)
	
	def test_can_combine_with_method_with_invalid_run_of_two(self):
		test_card_1 = [Card(1,2)]
		test_card_2 = [Card(2,1)]
		m = Meld(test_card_1)
		mob = Meld(test_card_2)
		mob.setMeldTypeManual(2)
		self.assertEqual(m.canCombineWith(mob), False)
		m.setMeldTypeManual(2)
		self.assertEqual(m.canCombineWith(mob), False)
		
	def test_can_combine_with_method_with_valid_run_of_two(self):
		test_card_1 = [Card(12,2)]
		test_card_2 = [Card(13,2)]
		m = Meld(test_card_1)
		mob = Meld(test_card_2)
		mob.setMeldTypeManual(2)
		self.assertEqual(m.canCombineWith(mob), False)
		m.setMeldTypeManual(2)
		self.assertEqual(m.canCombineWith(mob), True)
	
	def test_meld_with_ace_low_run(self):
		test_cards = [Card(1,2), Card(2,2), Card(3,2)] # <A 2 3> of Hearts
		test_value = 25
		m = Meld(test_cards)
		self.assertEqual(m.meld_type, 2)
		self.assertEqual(m.value, test_value)
		self.assertEqual(m.valid, True)
		self.assertEqual(m.independent, True)
		
	def test_meld_with_ace_high_run(self):
		test_cards = [Card(12,2), Card(13,2), Card(1,2)] # <Q K A> of Hearts
		test_value = 35
		m = Meld(test_cards)
		self.assertEqual(m.meld_type, 2)
		self.assertEqual(m.value, test_value)
		self.assertEqual(m.valid, True)
		self.assertEqual(m.independent, True)
		
	def test_meld_with_wraparound_meld(self):
		test_cards = [Card(13,2), Card(1,2), Card(2,2)] # <K A 2> of Hearts
		test_value = 0
		m = Meld(test_cards)
		self.assertEqual(m.value, test_value)
		self.assertEqual(m.valid, False)
		self.assertEqual(m.independent, False)
		
	def test_combining_valid_ace_low_straight_with_inconsecutive_valid_straight(self):
		test_cards_1 = [Card(1,2), Card(2,2), Card(3,2)] # <A 2 3> of Hearts
		test_cards_2 = [Card(4,2), Card(6,2)]
		mob = Meld(test_cards_1)
		m = Meld(test_cards_2)
		
		self.assertEqual(mob.meld_type, 2)
		
		self.assertEqual(m.canCombineWith(mob), False)
		m.setMeldTypeManual(2)
		self.assertEqual(m.canCombineWith(mob), False)
		
		self.assertEqual(m.valid, False)
		self.assertEqual(m.independent, False)
		
	def test_combining_JQK_straight_with_Ace(self):
		test_cards_1 = [Card(11,2), Card(12,2), Card(13,2)] # <A 2 3> of Hearts
		test_cards_2 = [Card(1,2)]
		
		mob = Meld(test_cards_1)
		m = Meld(test_cards_2)
		
		self.assertEqual(mob.meld_type, 2)
		
		self.assertEqual(m.canCombineWith(mob), False)
		m.setMeldTypeManual(2)
		self.assertEqual(m.canCombineWith(mob), True)
		
		self.assertEqual(m.valid, True)
		self.assertEqual(m.independent, False)
		
	def test_combining_10_with_JQKA_straight(self):
		test_cards_1 = [Card(11,2), Card(12,2), Card(13,2), Card(1,2)] # <A 2 3> of Hearts
		test_cards_2 = [Card(10,2)]
		
		mob = Meld(test_cards_1)
		m = Meld(test_cards_2)
		
		self.assertEqual(mob.meld_type, 2)
		
		self.assertEqual(m.canCombineWith(mob), False)
		m.setMeldTypeManual(2)
		self.assertEqual(m.canCombineWith(mob), True)
		
		self.assertEqual(m.valid, True)
		self.assertEqual(m.independent, False)
		
	def test_determine_meld_type_with_one_card_non_independent_meld(self):
		test_card = [Card(1,4)]
		m = Meld(test_card)
		self.assertEqual(m.valid, True)
		self.assertEqual(m.independent, False)
		self.assertEqual(m.meld_type, 0)
		
	def test_determine_meld_type_with_three_card_non_independent_meld(self):
		test_card = [Card(1,4), Card(2,3), Card(7,1)]
		m = Meld(test_card)
		self.assertEqual(m.valid, False)
		self.assertEqual(m.independent, False)
		self.assertEqual(m.meld_type, 0)
		
	def test_determine_meld_type_with_independent_straight(self):
		test_cards = [Card(1,1), Card(3,1), Card(2,1)]
		m = Meld(test_cards)
		self.assertEqual(m.valid, True)
		self.assertEqual(m.independent, True)
		self.assertEqual(m.meld_type, 2)
		
	def test_determine_meld_type_with_independent_set(self):
		test_cards = [Card(1,4), Card(1,3), Card(1,1)]
		m = Meld(test_cards)
		self.assertEqual(m.valid, True)
		self.assertEqual(m.independent, True)
		self.assertEqual(m.meld_type, 1)

if __name__ == '__main__':
	unittest.main()  
