import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from itertools import product
from util import deck, suits, ranks

class TestCards(unittest.TestCase):
    def test_getters(self):
        for suit, rank, card in zip(suits, ranks, deck):
            self.assertEqual(suit, card.get_suit())
            self.assertEqual(rank, card.get_rank())

    def test_to_string(self):
        for suit, rank, card in zip(suits, ranks, deck):
            self.assertEqual(card.__str__(), rank + " of " + suit )

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