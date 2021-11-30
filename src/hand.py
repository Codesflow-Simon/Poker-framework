from card import Card

class Hand:
    def __init__(self):
        self.cards = []

    def __iter__(self):
        return get_cards()

    def add_card(self, card):
        self.cards.append(card)
        return card

    def remove_card(self, target):
        for i, card in enumerate(self):
            if card.equals(target):
                del self.cards[i]

    def get_cards(self):
        return self.cards

    def copy(self):
        newHand = Hand()
        for card in self:
            newHand.add_card(card)
        return newHand

    def reset(self):
        self.cards = []

    def merge(self, hand):
        cards = self.cards.append(hand.get_cards)

