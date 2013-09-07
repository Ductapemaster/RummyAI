import unittest

from iAgent import *

class IAgentTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_setPlayerNumber_works(self):
		player_number = 2
		a = IAgent()
		a.setPlayerNumber(player_number)
		
		self.assertEqual(a.player_number, player_number)

if __name__ == '__main__':
	unittest.main()

