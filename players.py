import math
import random
from cards import Card
from cards import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def getName(self):
        return self.name
    def getHand(self):
        return self.hand

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        print("{}'s hand : ".format(self.name)) 
        for card in self.hand:
            card.show()

    def drawHand(self, size, deck):
        while size > 0:
            self.draw(deck)
            size -= 1
    
    def showSumHand(self):
        value = sum(card.value for card in self.hand)
        return print("{}'s value of cards in hand = {}".format(self.name, value))

    def throwCard(self, size):
        while size > 0:
            self.hand.pop()
            size -= 1
        return self.hand
