
class HumanAgent(IAgent):
	
	# do I need this?
	def __init__(self):
		self.players = []
		self.discard_pile = []
		
	# Simply stores new game state locally
	def updateGameState(self, sanitized_game):
		self.sanitized_game = sanitized_game
		
	def getDrawAction(self):
		print "It is Player %d's turn. Current Game State: ", self.player_number
		print sanitized_game
		print "\nActions:\n0: Draw top card off of draw pile\nN: Pickup N cards from discard pile"		
		
		while(true):
			draw_action_str = raw_input("What would you like to do? ")
			if (int(draw_action_str) > 0 and int(draw_action_str) <= len(sanitized_game.draw_pile)):
				break
			print "Invalid choice entered, try again."
		
		draw_action = int(draw_action_str)
		if draw_action == 0:
			print "Drawing top card off of draw pile"
		elif draw_action == 1:
			print "Drawing the %s off of the discard pile", sanitized_game.discard_pile[len(sanitized_game.discard_pile)-1]
		else:
			print "Drawing %d cards off of the discard pile"
		return draw_action
		
	def getMeldAction(self):
		pass
		
	def getDiscardAction(self):
		pass