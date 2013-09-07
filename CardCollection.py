import Card

class CardCollection:
	def __init__(self):
		self.cards = []
		
	def __repr__(self):
		output_str = ""
		for card in self.cards:
			output_str += card.__repr__()
			output_str += "\n"
		return output_str
		
	def addCard(self, new_card):
		self.cards.append(new_card)
		
	def removeCard(self, card_to_remove):
		for idx in range(len(cards)):
			if cards[idx] == card_to_remove:
				c = cards[idx]
				cards.remove(idx)
				return c
		return False
				
	def popCard(self, idx=0):
		return self.cards.pop(idx)
		
	def isEmpty(self):
		if len(self.cards) == 0:
			return True
		return False
		
	def makeEmpty(self):
		self.cards = []
		