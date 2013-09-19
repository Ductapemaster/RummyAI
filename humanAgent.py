from iAgent import *

class HumanAgent(IAgent):
	
	# do I need this?
	def __init__(self):
		self.players = []
		self.discard_pile = []
		
	# Simply stores new game state locally
	def updateGameState(self, sanitized_game):
		self.sanitized_game = sanitized_game
		
	def getDrawAction(self):
		print ("It is Player %d's turn. Current Game State: " % self.player_number)
		print (self.sanitized_game)
		print ("\nActions:\n0: Draw top card off of draw pile\nN: Pickup N cards from discard pile")
		
		draw_action = -1 # This will be set by the user 
		while(True):
			draw_action_str = input("What would you like to do? ")
			draw_action = int(draw_action_str)
			if ((draw_action >= 0) and (draw_action <= len(self.sanitized_game.discard_pile))):
				break
			print ("Invalid choice entered, try again.")
		
		if draw_action == 0:
			print ("Drawing top card off of draw pile")
		else:
			print ("Drawing %d top card(s) off of the discard pile" % draw_action)
		return draw_action
		
	def getMeldAction(self):
		pass
		
	def getDiscardAction(self):
		print ("Current Game State:")
		print (self.sanitized_game)
		print ("")
		print ("Actions:")
		print ("N: Discard Card at index N, (0 based)")
		print ("-1: Don't discard, (you will lose the game)")
		
		
		discard_action = -2 # This will be set by the user 
		while(True):
			discard_action_str = input("What would you like to do? ")
			discard_action = int(discard_action_str)
			if ((discard_action >= -1) and (discard_action < len(self.sanitized_game.players[self.player_number].hand))):
				break
			print ("Invalid choice entered, try again.")
		
		if discard_action == -1:
			print ("It's been nice knowing you...")
			return Card()
		else:
			c = self.sanitized_game.players[self.player_number].hand[discard_action]
			print ("Discarding %s." % c)
			return c
		
