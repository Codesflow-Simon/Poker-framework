import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from card import Card, suit_num_dict, rank_num_dict
from itertools import product

deck = []
suits = []
ranks = []
for suit, rank in product(suit_num_dict.keys(),rank_num_dict.keys()):
    deck.append(Card(suit, rank))
    suits.append(suit)
    ranks.append(rank)
