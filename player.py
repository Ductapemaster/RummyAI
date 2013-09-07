class Player:
	def __init__(self):#, number):
		#self.pNum = number
		self.hand = []
		self.board = []
	
	def discard(self, cardIndex):
		return self.hand.pop(cardIndex)