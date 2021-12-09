from itertools import product
from random import randint
from card import Card

SUITS = ("spades", "clubs", "diamonds", "hearts")
RANKS = ("2","3","4","5","6","7","8","9","10","J","Q","K","A")

class Deck:
    def __init__(self):
        self.reset()

    def reset(self):
        self.deck = []
        for suit, rank in product(SUITS,RANKS):
            self.deck.append(Card(suit, rank))
        self.shuffle()

    def get_deck(self):
        return self.deck

    def shuffle(self):
        new_deck = []
        for i in range(len(self.deck)):
            remaining = len(SUITS)*len(RANKS)-1-i
            num = randint(0,remaining)
            new_deck.append(self.deck[num])
            del self.deck[num]
        self.deck = new_deck

    def print_deck(self):
        out = ""
        for i, card in enumerate(self.deck):
            if (i != 0): out += ", "
            out += card.to_string()
        print(out)

    def pop(self):
        temp = self.deck[-1]
        del self.deck[-1]
        return temp
