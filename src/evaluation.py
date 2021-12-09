from itertools import combinations
from collections import Counter

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

# Use for any hand size
def evaluate(hand):
    return evaluvate_five_hand(get_best_hand(hand))

# Use for any hand size
def get_best_hand(hand):
    assert len(hand) > 4
    current_eval = [-1]
    best_hand = []
    for five_hand in combinations(hand, 5):
        evaluation = evaluvate_five_hand(five_hand)
        if compare_eval(evaluation, current_eval) == 1:
            best_hand = five_hand
            current_eval = evaluation
    return best_hand
    
# Only use for 5 card hands
# 1 if hand one better, -1 if hand 2 better, 0 if draw
def compare_hands(hand_one, hand_two):
    eval_one = evaluvate_five_hand(hand_one) if len(hand_one) == 5 else evaluate(hand_one)
    eval_two = evaluvate_five_hand(hand_two) if len(hand_two) == 5 else evaluate(hand_two)
    return compare_eval(eval_one, eval_two)
    
def compare_eval(eval_one, eval_two):
    if (eval_one == [] and eval_two == []): return 0

    elif (eval_one[0] > eval_two[0]): return 1
    elif (eval_one[0] < eval_two[0]): return -1
    else: return compare_eval(eval_one[1:], eval_two[1:])

# Only use for 5 card hands
def evaluvate_five_hand(hand):
    assert len(hand)==5

    # Construct times seen dict
    times_seen = dict()
    for card in hand:
        if (card.get_rank() in times_seen.keys()):
            times_seen[card.get_rank()] += 1                
        else:
            times_seen[card.get_rank()] = 1

    assert sum(times_seen.values()) == 5
    assert 5 not in times_seen

    frequency = Counter(times_seen.values())

    # Search strong hands first
    # Search for flush (and straight flush)
    is_flush = True
    for prev, current in zip(hand, hand[1:]):
        if prev.get_suit() != current.get_suit():
            is_flush = False
            break

    # Search for straight
    is_straight = True
    cards_seen = {rank_num_dict[key] for key in times_seen.keys()}

    diff = max(cards_seen) - min(cards_seen)
    is_straight = diff == 4 and len(cards_seen) == 5
    
    # Straight flush
    if is_straight and is_flush:
        return [8, max(cards_seen)]


    # Four of a kind
    if (4 in times_seen.values()):
        out = [7,-1,-1]
        for key, value in times_seen.items():
            if value == 4:
                out[1] = rank_num_dict[key]
            elif value == 1:
                out[2] = rank_num_dict[key]
        assert -1 not in out
        return out
    
    # Full house
    if (3 in times_seen.values() and 2 in times_seen.values()):
        out = [6,-1,-1]
        for key, value in times_seen.items():
            if value == 3:
                out[1] = rank_num_dict[key]
            elif value == 2:
                out[2] = rank_num_dict[key]
        assert -1 not in out
        return out
    
    # Full house
    if (3 in times_seen.values() and 2 in times_seen.values()):
        out = [6,-1,-1]
        for key, value in times_seen.items():
            if value == 3:
                out[1] = rank_num_dict[key]
            elif value == 2:
                out[2] = rank_num_dict[key]
        assert -1 not in out
        return out

    # Flush
    if is_flush and not is_straight:
        out = [5,-1,-1,-1,-1,-1]
        for key, value in times_seen.items():
            out[5] = rank_num_dict[key]
            for i in reversed(range(2, 6)):
                if out[i] > out[i-1]:
                    temp = out[i-1]
                    out[i-1] = out[i]
                    out[i] = temp
        assert -1 not in out
        assert out[1]>out[2] and out[2]>out[3] and\
           out[3]>out[4] and out[4]>out[5]
        return out

    # Straight
    if is_straight and not is_flush:
        return [4, max(cards_seen)]

    # Three of a kind
    if (3 in times_seen.values() and
        1 in times_seen.values() and 
        frequency[1] == 2 ):
        
        out = [3,-1,-1,-1]
        for key, value in times_seen.items():
            if value == 3:
                out[1] = rank_num_dict[key]
            elif value == 1:
                if (rank_num_dict[key] > out[2]):
                    out[3] = out[2]
                    out[2] = rank_num_dict[key]
                else:
                    out[3] = rank_num_dict[key]
        assert -1 not in out 
        assert out[2]>out[3]
        return out

    # Two pair
    if (2 in times_seen.values() and
        1 in times_seen.values() and 
        frequency[2] == 2 ):
        
        out = [2,-1,-1,-1]
        for key, value in times_seen.items():
            if value == 2:
                if (rank_num_dict[key] > out[1]):
                    out[2] = out[1]
                    out[1] = rank_num_dict[key]

            elif value == 1:
                out[3] = rank_num_dict[key]
        assert -1 not in out and out[1]>out[2]
        return out

    # Pair
    if (2 in times_seen.values() and
        1 in times_seen.values() and 
        frequency[1] == 3):
        
        out = [1,-1,-1,-1,-1]
        for key, value in times_seen.items():
            if value == 2:
                out[1] = rank_num_dict[key]

            elif value == 1:
                out[4] = rank_num_dict[key]
                for i in reversed(range(3, 5)):
                    if out[i] > out[i-1]:
                        temp = out[i-1]
                        out[i-1] = out[i]
                        out[i] = temp

        assert -1 not in out and out[2]>out[3] and out[3]>out[4]
        return out

    # Highcard
    assert frequency[1] == 5
    
    out = [0,-1,-1,-1,-1,-1]
    for key, value in times_seen.items():
        out[5] = rank_num_dict[key]
        for i in reversed(range(2, 6)):
            if out[i] > out[i-1]:
                temp = out[i-1]
                out[i-1] = out[i]
                out[i] = temp

    assert -1 not in out
    assert out[1]>out[2] and out[2]>out[3] and\
           out[3]>out[4] and out[4]>out[5]

    return out

    