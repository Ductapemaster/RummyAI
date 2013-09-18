import copy
from player import *
from deck import *
from meld import *

class Game:
	def __init__(self, numPlayers):
		# Instantiate new deck and shuffle it
		self.draw_pile = Deck()
		self.draw_pile.shuffle()
		
		# Define lists for players and populate it
		self.players = []
		for num in range(numPlayers):
			self.players.append(Player())

		# deal 7 cards to each player
		for i in range(7):
			for player in self.players:
				player.hand.append(self.draw_pile.getTopCard())

		# create a discard pile and add one card to it
		self.discard_pile = []
		self.discard_pile.append(self.draw_pile.getTopCard())
		self.last_card_removed_from_discard_pile = Card()
		self.last_draw_action = 0

	def __repr__(self):
		draw_pile_str = "Draw Pile:\n\tCards Left: %d\n\n" % (self.draw_pile.cardsLeft())

		discard_pile_str = "Discard Pile:\n\t"
		for c in self.discard_pile:
			discard_pile_str += c.__repr__() + ", "
		discard_pile_str += "\n\n"

		player_str = ""
		for p in range(len(self.players)):
			player_str += "Player %d:\n\tBoard:\n" % (p+1)
			#print melds	
			player_str += "\n\tHand:\n"
			#print hand	

		return draw_pile_str + discard_pile_str + player_str


	def numPlayers(self):
		return len(self.players)

	def getSanitizedCopy(self, agent_num):
		copy = Game(len(self.players))
		copy.players = []
		for i in range(len(self.players)):
			if i != agent_num:
				copy.players.append(self.players[i].getCopyNullHand())
			else:
				copy.players.append(self.players[i].getCopy())
		copy.discard_pile = self.discard_pile.copy()
		copy.draw_pile = NullDeck(self.draw_pile.cardsLeft())
		return copy

	def applyDrawAction(self, player_num, action):
		if player_num < 0 or player_num >= self.numPlayers():
			return False

		self.last_draw_action = action

		if action == 0:
			c = self.draw_pile.getTopCard()
			self.players[player_num].draw(c)
		else:
			if action > len(self.discard_pile):
				return False

			for i in range(action):
				c = self.discard_pile.pop()
				self.last_card_removed_from_discard_pile = copy.copy(c)
				self.players[player_num].draw(c)

		return True


	def applyMeldAction(self, player_num, melds):
		# if an agent picks up, make sure it's using the last card 
		if self.last_draw_action > 0:
			using_last_picked_up_card = False
			for m in melds:
				for c in m.cards:
					if c == self.last_card_removed_from_discard_pile:
						using_last_picked_up_card = True
				if using_last_picked_up_card:
					break
			if not using_last_picked_up_card:
				return False

		for m in melds:
			can_meld = False

			meld_cards = []
			# verify that the meld is contained in the player's hand
			for c in m.cards:
				success, mc = self.players[player_num].discard(c)
				meld_cards.append(mc)
				if not success:
					return False

			# create a meld with the cards
			actual_meld = Meld(meld_cards)
			if (actual_meld.length == 1):
				actual_meld.meld_type = m.meld_type

			if not actual_meld.valid:
				return False


			# if the play is independent, play the meld
			if actual_meld.isIndependentMeld():
				self.players[player_num].board.append(actual_meld)
				can_meld = True
				continue

			# otherwise, see if it can be combined with any other meld
			for p in self.players:
				for other_meld in p.board:
					if actual_meld.canCombineWith(other_meld):
						self.players[player_num].board.append(actual_meld)
						can_meld = True
						break
				if can_meld:# check next meld 
					break
			if not can_meld:# if meld was not played, indicate failure 
				return False
		
		# all melds were melded
		return True
			
	def applyDiscardAction(self, player_num, card):
		if player_num < 0 or player_num >= self.numPlayers():
			return False

		success, c = self.players[player_num].discard(card)
		if success == False:
			return False

		self.discard_pile.append(c)
		return True
			
			



