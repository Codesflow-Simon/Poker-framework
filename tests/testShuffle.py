import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from deck import Deck
import numpy as np
import pandas as pd

def test(iters=10000):
    results = pd.DataFrame(np.zeros([52,52]))

    deck = Deck()
    for i in range(iters):
        deck.shuffle()
        for i, card in enumerate(deck.get_deck()):
            results.iat[i,card.int_encoding()] += 1

    return results

if __name__ == "__main__":
    results = test()
    results.to_csv("tests\dist.csv")

