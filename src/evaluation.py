from card import Card, rank_num_dict

# Evaluations are a list, first element represents the hand type, folowed by 
# the strength of the hand compared to similar hands ie kickers...
# high card: [0, kickers from highest to lowest...]
# pair: [1, value of pair, kickers...}
# two pair: [2, higher pair, lower pair, kicker]
# three of a kind: [3, trip value, kickers...]
# straight: [4, highest card]
# flush: [5, cards in order...]
# full house: [6, top card, bottom card]
# four of a kind: [7, quad value, kicker]
# straight flush: [8, highest card]

def evaluate(hand):
    # Search strong hands first
    # Search for flush (and straight flush)
    
    isFlush = True
    for prev, current in zip(hand, hand[1:]):
        if prev.get_suit() != current.get_suit():
            isFlush = False
            break

    isStraight = False
    for card in hand:
        for otherCard in hand:
            if card.equals(otherCard): continue

def card_combinations(self, hand, max_depth=5):
    output = []
    for card in hand:
        remaining = hand.copy()
        remaining.remove_card(card)
        


    
    