import unittest

from possibleMoveGetter import *	

class GetPossibleActionsTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_returns_empty_list_if_no_cards_in_hand(self):
		hand = []
		moves = get_possible(hand)
		self.assertEqual(len(moves), 0)

	def test_returns_melds_of_both_type_for_single_card(self):
		hand = [Card(2,2)]
		moves = get_possible(hand)
		self.assertEqual(len(moves), 2)
		self.assertEqual(moves[0].meld_type, 1)
		self.assertEqual(moves[1].meld_type, 2)

	def test_returns_melds_of_both_type_for_multiple_cards(self):
		hand = [Card(5,2), Card(2,2)]
		moves = get_possible(hand)
		self.assertEqual(len(moves), 4)
		self.assertEqual(moves[0].meld_type, 1)
		self.assertEqual(moves[1].meld_type, 2)
		self.assertEqual(moves[2].meld_type, 1)
		self.assertEqual(moves[3].meld_type, 2)

	def test_returns_a_meld_of_sets(self):
		hand = [Card(2,1), Card(2,2), Card(2,3)]
		moves = get_possible(hand)
		self.assertEqual(len(moves), 7)
		self.assertEqual(moves[0].meld_type, 1)
		self.assertEqual(moves[1].meld_type, 2)
		self.assertEqual(moves[2].meld_type, 1)
		self.assertEqual(moves[3].meld_type, 2)
		self.assertEqual(moves[4].meld_type, 1)
		self.assertEqual(moves[5].meld_type, 2)
		self.assertEqual(moves[6].meld_type, 1)
		self.assertEqual(moves[6].independent, True)

	def test_returns_a_meld_of_sets_of_3_and_all_combinations_of_4(self):
		hand = [Card(2,1), Card(2,2), Card(2,3), Card(2,4)]
		moves = get_possible(hand)
		self.assertEqual(len(moves), 13)
		self.assertEqual(moves[0].meld_type, 1)
		self.assertEqual(moves[1].meld_type, 2)
		self.assertEqual(moves[2].meld_type, 1)
		self.assertEqual(moves[3].meld_type, 2)
		self.assertEqual(moves[4].meld_type, 1)
		self.assertEqual(moves[5].meld_type, 2)
		self.assertEqual(moves[6].meld_type, 1)
		self.assertEqual(moves[7].meld_type, 2)
		self.assertEqual(moves[8].meld_type, 1)
		self.assertEqual(moves[9].meld_type, 1)
		self.assertEqual(moves[10].meld_type, 1)
		self.assertEqual(moves[11].meld_type, 1)
		self.assertEqual(moves[12].meld_type, 1)
		for i in range(8,13):
			self.assertEqual(moves[i].independent, True)

	def test_returns_a_meld_of_runs(self):
		hand = [Card(2,1), Card(3,1)]
		moves = get_possible(hand)
		self.assertEqual(len(moves), 5)
		self.assertEqual(moves[0].meld_type, 1)
		self.assertEqual(moves[1].meld_type, 2)
		self.assertEqual(moves[2].meld_type, 1)
		self.assertEqual(moves[3].meld_type, 2)
		self.assertEqual(moves[4].meld_type, 2)

	def test_returns_every_meld_of_runs(self):
		hand = [Card(2,1), Card(3,1), Card(4,1)]
		moves = get_possible(hand)
		self.assertEqual(len(moves), 9)
		self.assertEqual(moves[0].meld_type, 1)
		self.assertEqual(moves[1].meld_type, 2)
		self.assertEqual(moves[2].meld_type, 1)
		self.assertEqual(moves[3].meld_type, 2)
		self.assertEqual(moves[4].meld_type, 1)
		self.assertEqual(moves[5].meld_type, 2)
		self.assertEqual(moves[6].meld_type, 2)
		self.assertEqual(moves[7].meld_type, 2)
		self.assertEqual(moves[8].meld_type, 2)


class HasNoDuplicateCardsTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_returns_true_if_cards_are_all_unique(self):
		melds = [Meld( [Card(2,3), Card(3,3)]),
				 Meld( [Card(4,4), Card(5,4)])]

		self.assertEqual(has_no_duplicate_cards(melds), True)

	def test_returns_false_if_duplicate_cards_exist(self):
		melds = [Meld( [Card(2,3), Card(3,3)]),
				 Meld( [Card(3,3), Card(4,3)])]

		self.assertEqual(has_no_duplicate_cards(melds), False)
