import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from util import deck
from evaluation import *
from card import Card
from hand import Hand

class TestEval(unittest.TestCase):
    def test_straight_flush(self):
        hand = Hand([Card('diamonds', '5'), Card('diamonds', '6'),
                     Card('diamonds', '9'), Card('diamonds', '8'),
                     Card('diamonds', '7')])

        self.assertEqual(evaluvate_five_hand(hand), [8,7])
        
        hand = Hand([Card('diamonds', '7'), Card('diamonds', 'J'),
                     Card('diamonds', '9'), Card('diamonds', '10'),
                     Card('diamonds', '8')])

        self.assertEqual(evaluvate_five_hand(hand), [8,9])
        
        hand = Hand([Card('clubs', 'A'), Card('clubs', 'K'),
                     Card('clubs', 'Q'), Card('clubs', 'J'),
                     Card('clubs', '10')])

        self.assertEqual(evaluvate_five_hand(hand), [8,12])

        hand = Hand([Card('clubs', '3'), Card('clubs', '4'),
                     Card('diamonds', '5'), Card('clubs', '6'),
                     Card('clubs', '7')])

        self.assertNotEqual(evaluvate_five_hand(hand)[0], 8)

        hand = Hand([Card('hearts', '8'), Card('hearts', '9'),
                     Card('hearts', '10'), Card('hearts', 'Q'),
                     Card('hearts', 'K')])

        self.assertNotEqual(evaluvate_five_hand(hand)[0], 8)
    
    def test_four_kind(self):
        hand = Hand([Card('clubs', '10'), Card('hearts', '10'),
                     Card('spades', '10'), Card('diamonds', '10'),
                     Card('clubs', 'A')])

        self.assertEqual(evaluvate_five_hand(hand), [7,8,12])
        
        hand = Hand([Card('diamonds', '3'), Card('hearts', '3'),
                     Card('spades', '3'), Card('clubs', '3'),
                     Card('diamonds', '2')])

        self.assertEqual(evaluvate_five_hand(hand), [7,1,0])
        
        hand = Hand([Card('hearts', 'K'), Card('diamonds', 'K'),
                     Card('clubs', 'K'), Card('spades', 'K'),
                     Card('diamonds', 'Q')])

        self.assertEqual(evaluvate_five_hand(hand), [7,11,10])
    
    def test_full_house(self):
        hand = Hand([Card('clubs', '9'), Card('hearts', '9'),
                     Card('spades', '9'), Card('diamonds', 'J'),
                     Card('clubs', 'J')])

        self.assertEqual(evaluvate_five_hand(hand), [6,7,9])
        
        hand = Hand([Card('diamonds', '4'), Card('hearts', '4'),
                     Card('spades', '4'), Card('clubs', '6'),
                     Card('diamonds', '6')])

        self.assertEqual(evaluvate_five_hand(hand), [6,2,4])
        
        hand = Hand([Card('hearts', 'K'), Card('diamonds', 'K'),
                     Card('clubs', 'K'), Card('spades', '7'),
                     Card('diamonds', '7')])

        self.assertEqual(evaluvate_five_hand(hand), [6,11,5])
    
    def test_flush(self):
        hand = Hand([Card('clubs', '2'), Card('clubs', '9'),
                     Card('clubs', '4'), Card('clubs', 'J'),
                     Card('clubs', '5')])

        self.assertEqual(evaluvate_five_hand(hand), [5,9,7,3,2,0])
        
        hand = Hand([Card('spades', '7'), Card('spades', '6'),
                     Card('spades', '10'), Card('spades', '3'),
                     Card('spades', '8')])

        self.assertEqual(evaluvate_five_hand(hand), [5,8,6,5,4,1])
        
        hand = Hand([Card('hearts', 'K'), Card('hearts', '2'),
                     Card('hearts', '5'), Card('hearts', '7'),
                     Card('hearts', '4')])

        self.assertEqual(evaluvate_five_hand(hand), [5,11,5,3,2,0])
    
    def test_straight(self):
        hand = Hand([Card('clubs', '6'), Card('hearts', '9'),
                     Card('spades', '7'), Card('diamonds', '10'),
                     Card('clubs', '8')])

        self.assertEqual(evaluvate_five_hand(hand), [4,8])
        
        hand = Hand([Card('spades', 'J'), Card('spades', '9'),
                     Card('spades', '10'), Card('diamonds', 'Q'),
                     Card('clubs', '8')])

        self.assertEqual(evaluvate_five_hand(hand), [4,10])
        
        hand = Hand([Card('hearts', '5'), Card('hearts', '2'),
                     Card('hearts', '3'), Card('clubs', '6'),
                     Card('hearts', '4')])

        self.assertEqual(evaluvate_five_hand(hand), [4,4])
    
    def test_three_kind(self):
        hand = Hand([Card('clubs', '6'), Card('hearts', '6'),
                     Card('spades', '6'), Card('diamonds', '10'),
                     Card('clubs', '8')])

        self.assertEqual(evaluvate_five_hand(hand), [3,4,8,6])
        
        hand = Hand([Card('spades', 'J'), Card('spades', '9'),
                     Card('spades', 'Q'), Card('diamonds', 'Q'),
                     Card('clubs', 'Q')])

        self.assertEqual(evaluvate_five_hand(hand), [3,10,9,7])
        
        hand = Hand([Card('hearts', '5'), Card('hearts', '10'),
                     Card('hearts', '3'), Card('clubs', '5'),
                     Card('diamonds', '5')])

        self.assertEqual(evaluvate_five_hand(hand), [3,3,8,1])

    def test_two_pair(self):
        hand = Hand([Card('clubs', '6'), Card('hearts', '6'),
                     Card('spades', '8'), Card('diamonds', '10'),
                     Card('clubs', '8')])

        self.assertEqual(evaluvate_five_hand(hand), [2,6,4,8])
        
        hand = Hand([Card('spades', 'J'), Card('spades', '9'),
                     Card('spades', 'Q'), Card('diamonds', '9'),
                     Card('clubs', 'Q')])

        self.assertEqual(evaluvate_five_hand(hand), [2,10,7,9])
        
        hand = Hand([Card('hearts', '5'), Card('hearts', '10'),
                     Card('hearts', '3'), Card('clubs', '10'),
                     Card('diamonds', '5')])

        self.assertEqual(evaluvate_five_hand(hand), [2,8,3,1])

    def test_pair(self):
        hand = Hand([Card('clubs', '6'), Card('hearts', '10'),
                     Card('spades', '8'), Card('diamonds', '10'),
                     Card('clubs', '2')])

        self.assertEqual(evaluvate_five_hand(hand), [1,8,6,4,0])
        
        hand = Hand([Card('spades', 'J'), Card('spades', '9'),
                     Card('spades', '3'), Card('diamonds', '9'),
                     Card('clubs', 'Q')])

        self.assertEqual(evaluvate_five_hand(hand), [1,7,10,9,1])
        
        hand = Hand([Card('hearts', '5'), Card('hearts', '10'),
                     Card('hearts', '3'), Card('clubs', 'A'),
                     Card('diamonds', '3')])

        self.assertEqual(evaluvate_five_hand(hand), [1,1,12,8,3])

    def test_high(self):
        hand = Hand([Card('clubs', '6'), Card('hearts', '10'),
                     Card('spades', '8'), Card('diamonds', 'J'),
                     Card('clubs', '2')])

        self.assertEqual(evaluvate_five_hand(hand), [0,9,8,6,4,0])
        
        hand = Hand([Card('spades', 'J'), Card('spades', '9'),
                     Card('spades', '3'), Card('diamonds', '5'),
                     Card('clubs', 'Q')])

        self.assertEqual(evaluvate_five_hand(hand), [0,10,9,7,3,1])
        
        hand = Hand([Card('hearts', '5'), Card('hearts', '10'),
                     Card('hearts', '3'), Card('clubs', 'A'),
                     Card('diamonds', '8')])

        self.assertEqual(evaluvate_five_hand(hand), [0,12,8,6,3,1])

    def test_compare(self):
        hand_one = Hand([Card('hearts', '5'), Card('hearts', '10'),
                         Card('hearts', '3'), Card('clubs', 'A'),
                         Card('diamonds', '8')])

        hand_two = Hand([Card('hearts', '5'), Card('hearts', '10'),
                         Card('hearts', '3'), Card('clubs', 'A'),
                         Card('diamonds', '3')])

        self.assertEqual(compare_hands(hand_one, hand_two), -1)

        hand_one = Hand([Card('clubs', '6'), Card('hearts', '6'),
                         Card('spades', '6'), Card('diamonds', '10'),
                         Card('clubs', '8')])

        hand_two = Hand([Card('hearts', '5'), Card('hearts', '10'),
                         Card('hearts', '3'), Card('clubs', '3'),
                         Card('diamonds', '3')])

        self.assertEqual(compare_hands(hand_one, hand_two), 1)

        hand_one = Hand([Card('clubs', '6'), Card('clubs', '7'),
                         Card('spades', '8'), Card('diamonds', '10'),
                         Card('clubs', '9')])

        hand_two = Hand([Card('clubs', '9'), Card('hearts', '8'),
                         Card('spades', '7'), Card('diamonds', '10'),
                         Card('diamonds', '6')])

        self.assertEqual(compare_hands(hand_one, hand_two), 0)

    def test_eval_larger_hand(self):
        hand = Hand([Card('hearts', '5'), Card('hearts', '2'),
                     Card('hearts', '3'), Card('clubs', '6'),
                     Card('hearts', '4'), Card('clubs', 'A'),
                     Card('diamonds', '4')])

        self.assertEqual(evaluate(hand), [4,4])

        hand = Hand([Card('clubs', '3'), Card('hearts', '2'),
                     Card('hearts', '3'), Card('clubs', '6'),
                     Card('hearts', '4'), Card('clubs', 'A'),
                     Card('diamonds', '4')])

        self.assertEqual(evaluate(hand), [2,2,1,12])

        hand = Hand([Card('clubs', '6'), Card('hearts', '2'),
                     Card('hearts', '3'), Card('diamonds', '6'),
                     Card('hearts', '8'), Card('clubs', 'A'),
                     Card('diamonds', '4')])

        self.assertEqual(evaluate(hand), [1,4,12,6,2])
        
        hand = Hand([Card('clubs', '6'), Card('hearts', '2'),
                     Card('hearts', '3'), Card('diamonds', 'J'),
                     Card('hearts', '8'), Card('clubs', 'A'),
                     Card('diamonds', '4')])

        self.assertEqual(evaluate(hand), [0,12,9,6,4,2])

if __name__ == "__main__":
    unittest.main()