import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from itertools import product
from card import Card, suit_num_dict, rank_num_dict

deck = []
suits = []
ranks = []
for suit, rank in product(suit_num_dict.keys(),rank_num_dict.keys()):
    deck.append(Card(suit, rank))
    suits.append(suit)
    ranks.append(rank)

class TestCards(unittest.TestCase):
    def test_getters(self):
        for suit, rank, card in zip(suits, ranks, deck):
            self.assertEquals(suit, card.get_suit())
            self.assertEquals(rank, card.get_rank())

    def test_to_string(self):
        for suit, rank, card in zip(suits, ranks, deck):
            self.assertEquals(card.to_string(), rank + " of " + suit )

    def test_encodings(self):
        seen = set()
        for card in deck:
            num = card.int_encoding()
            self.assertLess(num, 52)
            self.assertGreaterEqual(num, 0)
            self.assertFalse(card in seen)
            seen.add(card)

if __name__ == "__main__":
    unittest.main()