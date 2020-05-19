from enum import Enum
from random import shuffle

suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
face_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] #might want to make a dic with values

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def pretty_print(self):
        print(self.value + "of" + self.suit + "\n")

class Deck: #may want to implement different decks
    def __init__(self):
        self.cards = []

        for s in suits:
            for fv in face_values:
                toAdd = Card(s, fv)
                self.cards.append(toAdd)

        shuffle(self.cards)

    #last item in cards is removed.
    def pop_card(self):
        return self.cards.pop()

    def pretty_print(self):
        for c in self.cards:
            print("{} of {}".format(c.value, c.suit))
