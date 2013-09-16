import unittest

from game import *

class GameTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor_creates_the_correct_number_of_players(self):
		numPlayers = 3
		g = Game(numPlayers)
		self.assertEqual(len(g.players), numPlayers)
		self.assertEqual(g.numPlayers(), numPlayers)


	def test_constructor_deals_the_correct_number_of_cards(self):
		numPlayers = 3
		g = Game(numPlayers)
		self.assertEqual(g.draw_pile.cardsLeft(), 52 - 7*numPlayers - 1)
		self.assertEqual(len(g.discard_pile), 1)


	def test_getSanitizedCopy_hides_cards(self):
		numPlayers = 3
		g = Game(numPlayers)

		agent_num = 2
		copy = g.getSanitizedCopy(agent_num)
		
		for i in range(numPlayers):
			for c in range(len(copy.players[i].hand)):
				if i != agent_num:
					self.assertEqual(copy.players[i].hand[c], Card())
				else:
					self.assertEqual(copy.players[i].hand[c], g.players[i].hand[c])

		for c in copy.draw_pile:
			self.assertEquals(c, Card())


	def test_applyDrawAction_draws_off_of_the_draw_pile(self):
		numPlayers = 3
		playerNum = 2
		g = Game(numPlayers)

		cards_left = g.draw_pile.cardsLeft()
		top_card = g.draw_pile.peekTopCard()
		cards_in_hand = len(g.players[playerNum].hand)

		success = g.applyDrawAction(playerNum, 0)

		self.assertEqual(success, True)
		self.assertEqual(g.draw_pile.cardsLeft(), cards_left - 1)
		self.assertEqual(len(g.players[playerNum].hand), cards_in_hand + 1)
		self.assertEqual(g.players[playerNum].hand[-1], top_card)
		self.assertEqual(g.last_draw_action, 0)

	def test_applyDrawAction_draws_off_of_the_discard_pile(self):
		numPlayers = 3
		playerNum = 2
		g = Game(numPlayers)

		card1 = g.draw_pile.peekTopCard()
		g.discard_pile.append(g.draw_pile.getTopCard())
		card2 = g.draw_pile.peekTopCard()
		g.discard_pile.append(g.draw_pile.getTopCard())

		cards_left = g.draw_pile.cardsLeft()
		cards_in_hand = len(g.players[playerNum].hand)

		success = g.applyDrawAction(playerNum, 2)

		self.assertEqual(success, True)
		self.assertEqual(g.draw_pile.cardsLeft(), cards_left)
		self.assertEqual(len(g.players[playerNum].hand), cards_in_hand + 2)
		self.assertEqual(len(g.discard_pile), 1)
		self.assertEqual(g.players[playerNum].hand[-1], card1)
		self.assertEqual(g.players[playerNum].hand[-2], card2)
		self.assertEqual(g.last_draw_action, 2)
		self.assertEqual(g.last_card_removed_from_discard_pile, card1)

	def test_applyDrawAction_returns_false_if_not_enough_cards_in_discard_pile(self):
		numPlayers = 3
		playerNum = 2
		g = Game(numPlayers)
		too_big = 5

		success = g.applyDrawAction(playerNum, too_big)

		self.assertEqual(success, False)

	def test_applyDrawAction_returns_false_if_bad_player_number(self):
		numPlayers = 3
		playerNum = numPlayers + 1
		g = Game(numPlayers)

		success = g.applyDrawAction(playerNum, 0)

		self.assertEqual(success, False)

	def test_applyMeldAction_does_nothing_with_empty_list(self):
		numPlayers = 3
		g = Game(numPlayers)

		self.assertEqual(g.applyMeldAction(1,[]), True)
		

	def test_applyDiscardAction_returns_false_if_null_card(self):
		numPlayers = 3
		playerNum = 1
		g = Game(numPlayers)

		success = g.applyDiscardAction(playerNum, Card())

		self.assertEqual(success, False)

	def test_applyDiscardAction_returns_false_if_bad_player_number(self):
		numPlayers = 3
		playerNum = numPlayers + 1
		g = Game(numPlayers)

		success = g.applyDiscardAction(playerNum, g.players[0].hand[0])

		self.assertEqual(success, False)

	def test_applyDiscardAction_returns_false_if_card_not_in_hand(self):
		numPlayers = 3
		playerNum = 1
		g = Game(numPlayers)

		success = g.applyDiscardAction(playerNum, g.players[playerNum -1].hand[0])

		self.assertEqual(success, False)

	def test_applyDiscardAction_returns_true_and_works(self):
		numPlayers = 3
		playerNum = 1
		g = Game(numPlayers)

		discarded_card = g.players[playerNum].hand[0]
		hand_len = len(g.players[playerNum].hand)

		success = g.applyDiscardAction(playerNum, discarded_card) 

		self.assertEqual(success, True)
		self.assertEqual(len(g.players[playerNum].hand), hand_len - 1)



if __name__ == '__main__':
	unittest.main()

