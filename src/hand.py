


class Hand:
    def __init__(self, hand=[]):
        self.cards = hand

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, sub):
        return self.cards[sub]

    def __iter__(self):
        return iter(self.cards)

    def __repr__(self):
        if len(self)==0: return "[]"
        builder = "Hand: ["
        for card in self[:-1]:
            builder += str(card) + ", "
        builder += str(self.get_cards()[-1]) + "]"

        
        return builder

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
        newHand = Hand([])
        for card in self:
            newHand.add_card(card.copy())
        return newHand

    def reset(self):
        self.cards = []

    def merge(self, hand):
        cards = self.cards.append(hand.get_cards)

