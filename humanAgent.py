from iAgent import *
from meld import *
from operator import attrgetter

class HumanAgent(IAgent):
	
	# do I need this?
	def __init__(self):
		self.players = []
		self.discard_pile = []
		
	def getDrawAction(self):
		print ("It is Player %d's turn. Current Game State:\n" % (self.player_number + 1))
		self.game.players[self.player_number].hand = sorted(self.game.players[self.player_number].hand, key=attrgetter( 'alt_rank', 'suit'))
		print (self.game)
		print ("\nActions:\n0: Draw top card off of draw pile\nN: Pickup N cards from discard pile")
		
		draw_action = -1 # This will be set by the user 
		while(True):
			draw_action_str = input("What would you like to do? ")
			draw_action = int(draw_action_str)
			if ((draw_action >= 0) and (draw_action <= len(self.game.discard_pile))):
				break
			print ("Invalid choice entered, try again.")
		
		if draw_action == 0:
			print ("\nDrawing top card off of draw pile")
		else:
			print ("Drawing %d top card(s) off of the discard pile" % draw_action)
		return draw_action
		
	def getMeldActions(self):

		print ("Player %d, do you want to meld any cards?  Current Game State:\n" % self.player_number)
		self.game.players[self.player_number].hand = sorted(self.game.players[self.player_number].hand, key=attrgetter( 'alt_rank', 'suit'))
		print (self.game)
		print ("Actions:\n\'M <Card 1 Idx> <Card 2 Idx> ... <Card N Idx>\': Create meld of N cards\n\'E\': End meld phase")
		
		meld_list = []
		while(True):
			meld_action_str = input("What would you like to do?")

			if (meld_action_str[0] == 'M'):
				
				meld_action_list = meld_action_str.split(' ')[1:]
				if len(meld_action_list) == 0:
						print("No cards were given to meld!")
						continue

				indicies = []
				try:
					for idx_str in meld_action_list:
						indicies.append(int(idx_str))
				except:
					print("could not convert card index (%s) to int" % idx_str)
					continue

				cards = []
				for idx in indicies:
					cards.append(self.game.players[self.player_number].hand[idx])

				m = Meld(cards)
				for card in cards:
					self.game.players[self.player_number].hand.remove(card)
				
				hand_str = ""
				hand_str += "\nHand:\n"
				for idx in range(len(self.game.players[self.player_number].hand)):
					hand_str += "%d: %s\n" %(idx, self.game.players[self.player_number].hand[idx])
				print (hand_str)
				print ("Meld Created:\n%s\n" % m)
				meld_list.append(m)
			elif (meld_action_str[0] == 'E'):
				break
			
		return meld_list	
		
	def getDiscardAction(self):
		print ("Current Game State:")
		self.game.players[self.player_number].hand = sorted(self.game.players[self.player_number].hand, key=attrgetter( 'alt_rank', 'suit'))
		print (self.game)
		print ("")
		print ("Actions:")
		print ("N: Discard Card at index N, (0 based)")
		print ("-1: Don't discard, (you will lose the game)")
		
		
		discard_action = -2 # This will be set by the user 
		while(True):
			discard_action_str = input("What would you like to do? ")
			discard_action = int(discard_action_str)
			if ((discard_action >= -1) and (discard_action < len(self.game.players[self.player_number].hand))):
				break
			print ("Invalid choice entered, try again.")
		
		if discard_action == -1:
			print ("It's been nice knowing you...")
			return Card()
		else:
			c = self.game.players[self.player_number].hand[discard_action]
			print ("Discarding %s." % c)
			return c
		
