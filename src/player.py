from hand import Hand


class Player:
    def __init__(self, initial_stack=0):
        self.stack = initial_stack
        self.hand = Hand()

    def get_stack(self):
        return self.stack

    def add_stack(self, amount):
        self.stack += amount
        return self.stack

    def remove_stack(self, amount):
        self.stack -= amount
        return self.stack

    def remove_safe(self, amount):
        self.stack -= min(self.stack, amount)
        return stack

    def get_hand(self):
        return self.hand

    def add_card(self, card):
        self.hand.add_card(card)
        return self.hand

    def reset_cards(self):
        self.hand.reset()
        return self.hand

    def action(self, board):

