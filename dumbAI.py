import random
import copy
from itertools import combinations

from iAgent import *
from possibleMoveGetter import *

class DumbAI(IAgent):

	def getDrawAction(self):
		my_original_hand = self.game.players[self.player_number].hand

		game_copy = copy.deepcopy(self.game)
		my_hand = game_copy.players[self.player_number].hand
		my_hand.extend(game_copy.discard_pile)
		
		meld_combos = self.getAllPossibleMeldCombinations(my_hand, game_copy, self.player_number)
		best_meld_combo = self.getBestMeldCombo(meld_combos)

		pickup_index = len(self.game.discard_pile) 
		for m in best_meld_combo:
			for c in m.cards:
				if c in self.game.discard_pile:
					idx = self.game.discard_pile.index(c)
					if idx < pickup_index:
						pickup_index = idx

		cards_to_pickup = len(self.game.discard_pile) - pickup_index

		cards_in_meld_combo = 0
		for m in best_meld_combo:
			cards_in_meld_combo += len(m.cards)
			
		if cards_to_pickup + len(my_original_hand) == cards_in_meld_combo:
			return 0 # picking up and playing this meld combo with leave the player without a discard

		return cards_to_pickup


	def getMeldActions(self):
		my_hand = self.game.players[self.player_number].hand

		meld_combos = self.getAllPossibleMeldCombinations(my_hand, self.game, self.player_number)
		best_meld_combo = self.getBestMeldCombo(meld_combos)

		return best_meld_combo

	def getDiscardAction(self):
		num_cards_in_hand = len(self.game.players[self.player_number].hand) 
		if num_cards_in_hand > 1:
			rand_index = random.randint(0, num_cards_in_hand - 1)
			return self.game.players[self.player_number].hand[rand_index]
		else:
			return self.game.players[self.player_number].hand[0]


	def getAllPossibleMeldCombinations(self, hand, game, player_num):

		possible_melds = get_possible(hand)

		# get every meldable meld
		meldable_melds = []
		for m in possible_melds:
			gc = copy.deepcopy(game)
			if gc.applyMeldAction(player_num, [m]):
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

			if card_total < len(hand):
				valid_melds.append(c)

		return valid_melds

	def getBestMeldCombo(self, meld_combos):
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

