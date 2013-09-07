import unittest
	# properties
		# list of cards
		# number of points
		# flag to specify meld type
		# isIndependentMeld flag
	
	# methods
		# add card

from card import *	
from meld import *

class MeldTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor_with_empty_meld(self):
		m = Meld()
		self.assertEqual(m.getMeldValue(), 0)
		self.assertEqual(len(m.card_list), 0)
		self.assertEqual(m.meld_type, 0)
		self.assertEqual(m.isIndependentMeld(), False)
		
	def test_contructor_with_one_card_meld(self):
		test_cards = [Card(4, 2)]
		m = Meld(test_cards)
		self.assertEqual(m.getMeldValue(), test_cards[0].numPoints())
		self.assertEqual(len(m.card_list), 1)
		self.assertEqual(m.meld_type, 0)
		self.assertEqual(m.isIndependentMeld(), False)
		
	def test_constructor_with_three_card_meld(self):
		test_cards = [Card(7,1), Card(4,3), Card(12,4)]
		test_value = 20
		m = Meld(test_cards)
		self.assertEqual(m.getMeldValue(), test_value)
		self.assertEqual(len(m.card_list), 3)
		self.assertEqual(m.meld_type, 0)
		self.assertEqual(m.isIndependentMeld(), False)
		
		

if __name__ == '__main__':
	unittest.main()