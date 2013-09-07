
class Human(IAgent):
	
	# do I need this?
	def __init__(self):
		self.players = []
		self.discard_pile = []
		
	# Simply stores new game state locally
	def updateGameState(self, sanitized_game):
		self.sanitized_game = sanitized_game
		
	def getDrawAction(self):
		print "Current Game State: "
		print sanitized_game
		print "\nActions:\n0: Draw top card off of pile\nN: Pickup N cards from discard pile"		
		
		while(true):
			draw_action_str = raw_input("What would you like to do? ")
			if (int(draw_action_str) > 0 and int(draw_action_str) <= len(sanitized_game.draw_pile)):
				break
		return int(draw_action_str)
		
	def getMeldAction(self):
		pass
		
	def getDiscardAction(self):
		pass