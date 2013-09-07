from card import * 

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
		try:
			return self.cards.pop(self.cards.index(card_to_remove))
		except:
			return False
				
	def popCard(self, idx=0):
		try:
			return self.cards.pop(idx)
		except:
			return False
		
	def isEmpty(self):
		if len(self.cards) == 0:
			return True
		return False
		
	def makeEmpty(self):
		self.cards = []
		
	def numCards(self):
		return len(self.cards)
		
