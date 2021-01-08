import random
import math
import players

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getSuit(self):
        return self.suit
    def getValue(self):
        return self.value

    def show(self):
        print ("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(suit,value))

    def show(self):
        for card in self.cards:
            card.show() 

    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            ran = random.randint(0, i)
            self.cards[i], self.cards[ran] = self.cards[ran], self.cards[i]
        print("\n Shuffled deck\n")

    def amountOfCards(self, deck):
        return len(deck)

    def drawCard(self, deck):
        return self.cards.pop()
    
    