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
			if (int(draw_action) >= 0 and int(draw_action) <= len(self.sanitized_game.discard_pile)):
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
		pass
