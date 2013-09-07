from player import *
from deck import *

class Game:
    def __init__(self, numPlayers):
        # Instantiate new deck and shuffle it
        self.deck = Deck()
        self.deck.shuffle()
        
        # Define lists for players and the draw pile
        self.players = []
        self.drawPile = []
        
        
        for num in range(numPlayers):
            self.players.append(Player())

        self.dealHands(7)
        self.drawPile.append(self.deck.popCard())

    def numPlayers(self):
        return len(self.players)

    # Take in an array of players and deal them all hands with the specified number of cards
    def dealHands(self, numCards):
        for i in range(numCards):
            for player in self.players:
                player.hand.append(self.deck.popCard())
