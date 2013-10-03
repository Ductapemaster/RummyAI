import random
import copy
from itertools import combinations

from iAgent import *
from possibleMoveGetter import *

class DumbAI(IAgent):

	def getDrawAction(self):
		return 0

	def getMeldActions(self):
		my_hand = self.game.players[self.player_number].hand
		possible_melds = get_possible(my_hand)

		# get every meldable meld
		meldable_melds = []
		for m in possible_melds:
			gc = copy.deepcopy(self.game)
			if gc.applyMeldAction(self.player_number, [m]):
				meldable_melds.append(m)

		# get every combination of melds
		meld_combos = []
		for n in range(0, len(meldable_melds)):
			for c in combinations(meldable_melds, n+1):
				# verify that it is a valid combination
				if has_no_duplicate_cards(c):
					meld_combos.append(c)

		# verify that at least one card is left in hand to discard
		valid_melds = []
		for c in meld_combos:
			card_total = 0
			for m in c:
				card_total += len(m.cards)

			if card_total < len(my_hand):
				valid_melds.append(c)

		# rank by number of points
		# select the higest ranking meld combination, breaking ties by selecting the combination with the smallest number of melds
		best_meld_combo = []
		most_points = 0
		fewest_combos = 52
		for mc in meld_combos:
			pt = 0
			for m in mc:
				pt += m.numPoints()

			if pt > most_points or (pt == most_points and len(mc) < fewest_combos):
				best_meld_combo = mc
				most_points = pt
				fewest_combos = len(mc)

		return best_meld_combo

	def getDiscardAction(self):
		num_cards_in_hand = len(self.game.players[self.player_number].hand) 
		if num_cards_in_hand > 1:
			rand_index = random.randint(0, num_cards_in_hand - 1)
			return self.game.players[self.player_number].hand[rand_index]
		else:
			return self.game.players[self.player_number].hand[0]


