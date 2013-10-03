from operator import attrgetter
from meld import *

def sortCardsByRank(cards):
	return sorted(cards, key=attrgetter('rank', 'suit'))

def sortCardsBySuit(cards):
	return sorted(cards, key=attrgetter('suit', 'rank'))

def get_possible(hand):
	result = []

	num_cards = len(hand)

	if num_cards == 0:
		return result

	for c in hand:
		m1 = Meld([c])
		m2 = Meld([c])
		m1.setMeldTypeManual(1)
		m2.setMeldTypeManual(2)
		result.append(m1)
		result.append(m2)


	# check for sets
	rank_sorted_hand = sortCardsByRank(hand)
	rank_sorted_hand.append(Card()) #this is to trigger the last check
	set_cards = []
	cur_rank = -1
	for c in rank_sorted_hand:
		if c.rank != cur_rank:
			if len(set_cards) == 3: # add the set
				result.append(Meld(set_cards))
			elif len(set_cards) == 4:
				for i in range(4): # add every combination of three 
					copy_cards = set_cards.copy()
					copy_cards.pop(i)
					result.append(Meld(copy_cards))
				result.append(Meld(set_cards)) # add set of four
			set_cards = []
			cur_rank = c.rank
		set_cards.append(c)

	# check for runs
	suit_sorted_hand = sortCardsBySuit(hand)
	suit_sorted_hand.append(Card()) #this is to trigger the last check
	run_cards = []
	cur_suit = -1
	cur_rank = -1
	for c in suit_sorted_hand:
		if c.rank != cur_rank or c.suit != cur_suit:
			if len(run_cards) >= 2:
				for i in range(len(run_cards)):
					for j in range(i+1,len(run_cards)):
						result.append(Meld(run_cards[i:j+1]))
			run_cards = []
			cur_rank = c.rank
			cur_suit = c.suit
		run_cards.append(c)
		cur_rank += 1
		
	return result 


def has_no_duplicate_cards(melds):
	cards = []
	for m in melds:
		cards.extend(m.cards)
	
	sc = sortCardsByRank(cards)

	for i in range(len(sc)-1):
		if sc[i] == sc[i+1]:
			return False

	return True
	
