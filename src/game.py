from deck import Deck
from player import Player

class Board():
    def __init__(self):
        self.stage = 'pre-game'
        self.communities = []
        self.players = []
        self.folded= []
        self.pot = []
        self.deck = Deck()

    def get_communities(self):
        return self.communities

    def add_player(self, player):
        self.players.append(player)
        self.pot.append(0)
        self.pot.append(False)

    def add_all_players(self, players):
        self.players += players
        self.pot += [0] * len(players)
        self.folded += [False] * len(players)

    def reset_folds(self):
        self.folded = [False] * len(self.folded)

    def get_currently_playing(self):
        out = []
        for fold, player in zip(self.folded, self.players):
            if fold or player.get_stack()==0: 
                out.append(None)
            else:
                out.append(player)

    def player_pays_pot(self, player_idx, amount):
        pot[idx] += self.players[idx].remove_safe(amount)
    
    def deal():
        self.deck.reset()
        self.reset_folds()
        for player in self.players:
            player.reset_cards()
            player.add_card(deck.pop())
            player.add_card(deck.pop())
        self.stage = 'pre-flop'
    
    # Bet 0 for check, bet positive for bet, bet -1 for fold
    def bet():
        for player in self.player:
            if player.get_stack() != 0:
                player.action(self)



if __name__ == '__main__':
    board = Board()
    board.add_all_players([Player(100), Player(100)])
    print(board.pot)