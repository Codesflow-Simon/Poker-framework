


suit_num_dict = {"spades": 0, "clubs": 1, "diamonds":2, "hearts":3}
rank_num_dict = {"2": 0, "3": 1, "4":2, "5":3, "6": 4, "7": 5, "8":6,
                 "9":7, "10": 8, "J": 9, "Q":10, "K":11, "A": 12}

class Card:
    def __init__(self, suit, rank):
        assert suit in suit_num_dict.keys()
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return self.rank + " of " + self.suit

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def to_string(self):
        return self.rank + " of " + self.suit

    def int_encoding(self):
        suit_num = suit_num_dict[self.suit]
        rank_num = rank_num_dict[self.rank]
        return suit_num*13 + rank_num
        
    def equals(self, other):
        return self.suit == other.get_suit() and self.rank == other.get_rank()

    def copy(self):
        return Card(self.suit, self.rank)
