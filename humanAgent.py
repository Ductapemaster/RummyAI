from iAgent import *
from meld import *

class HumanAgent(IAgent):
	
	# do I need this?
	def __init__(self):
		self.players = []
		self.discard_pile = []
		
	# Simply stores new game state locally
	def updateGameState(self, sanitized_game):
		self.sanitized_game = sanitized_game
		
	def getDrawAction(self):
		print ("It is Player %d's turn. Current Game State:\n" % self.player_number)
		print (self.sanitized_game)
		print ("\nActions:\n0: Draw top card off of draw pile\nN: Pickup N cards from discard pile")
		
		draw_action = -1 # This will be set by the user 
		while(True):
			draw_action_str = input("What would you like to do? ")
			draw_action = int(draw_action_str)
			if (int(draw_action) >= 0 and int(draw_action) <= len(self.sanitized_game.discard_pile)):
				break
			print ("Invalid choice entered, try again.")
		
		if draw_action == 0:
			print ("\nDrawing top card off of draw pile")
		else:
			print ("Drawing %d top card(s) off of the discard pile" % draw_action)
		return draw_action
		
	def getMeldAction(self):
		
		print ("Player %d, do you want to meld any cards?  Current Game State:\n" % self.player_number)
		print (self.sanitized_game)
		print ("Actions:\n\'M <Card 1 Idx> <Card 2 Idx> ... <Card N Idx>\': Create meld of N cards\n\'E\': End meld phase")
		
		meld_list = []
		while(True):
			meld_action_str = input("What would you like to do?")
			if (meld_action_str[0] == 'M'):
				meld_action_list = meld_action_str.split(' ')
				try:
					cards = []
					for idx in range(len(meld_action_list[1:])):
						cards.append(self.sanitized_game.players[self.player_number].hand[idx])
					m = Meld(cards)
					for card in cards:
						self.sanitized_game.players[self.player_number].hand.remove(card)
					
					hand_str = ""
					hand_str += "\nHand:\n"
					for idx in range(len(self.sanitized_game.players[self.player_number].hand)):
						hand_str += "%d: %s\n" %(idx, self.sanitized_game.players[self.player_number].hand[idx])
					print (hand_str)
					print ("Meld Created:\n%s\n" % m)
					meld_list.append(m)
				except:
					print ("Invalid card index!  Next time try to not be so obtuse\n")
			elif (meld_action_str[0] == 'E'):
				break
			
		return meld_list	
		
	def getDiscardAction(self):
		pass
