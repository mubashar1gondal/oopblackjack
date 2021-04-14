from IPython.display import clear_output as co
import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f'<Card: ({self.suit}, {self.rank})>'

    def __str__(self):
        return f'{self.rank} of {self.suit}s'


class Hand:
    def __init__(self):
        self.holding = []

    def show(self):
        return [print(card) for card in self.holding]

    def get_total(self):
        total = 0
        for card_obj in self.holding:
            total += card_obj.rank
        return total


class Player:
    def __init__(self):
        self.hand = Hand()

    def show_hand(self, stand=False):
        if isinstance(self, Dealer):
            if stand == False:
                print(f'Dealer --> {self.hand.holding[0]}')
            else:
                print(
                    f'Dealer --> {self.hand.holding} [{self.hand.get_total()}]')
        else:
            print(
                f'Human --> {[card for card in self.hand.holding]} [{self.hand.get_total()}]')


class Dealer(Player):
    def deal(self, cls, a_deck):
        if len(cls.hand.holding) >= 2:
            cls.hand.holding.append(a_deck.cards.pop())
        else:
            for i in range(2):
                cls.hand.holding.append(a_deck.cards.pop())


class Deck:
    def __init__(self):
        self.ranks = range(1, 13)
        self.suits = ['Club', 'Spade', 'Diamond', 'Heart']
        self.cards = [Card(s, r) for s in self.suits for r in self.ranks]

    def shuffle_cards(self):
        print('Shuffling deck...')
        random.shuffle(self.cards)

    def show_cards(self):
        [print(card) for card in self.cards]


class Blackjack:
    current_round = 1

    @classmethod
    def game_over(self, done=False):
        print('BUST')
        print('Game Over')
        input('Press any key to continue. ')

    @classmethod
    def run(self):
        game_over = False
        while not game_over:
            co()
            deck = Deck()
            human = Player()
            dealer = Dealer()

            print("Welcome to PyJack")
            deck.shuffle_cards()

#             deck.show_cards()

            confirm = input(
                "Press any key to continue. Type 'quit' to exit program. ").lower()
            if confirm == 'quit':
                game_over = True
            else:
                dealer.deal(human, deck)
                dealer.deal(dealer, deck)

                done = False
                while not done:
                    co()
                    if human.hand.get_total() == 21 and self.current_round == 1:
                        print('Blackjack!')
                        print('Human wins')
                        print('Dealer loses')
                        break
                    if human.hand.get_total() > 21:
                        Blackjack.game_over(done=True)
                        break
                    if dealer.hand.get_total() > 21:
                        Blackjack.game_over(done=True)
                        break
                    human.show_hand()
                    dealer.show_hand()

                    ask = input(
                        "Would you like to hit or stand? Type 'exit' to stop playing. ").lower()
                    if ask == 'exit':
                        done = True
                    elif ask == 'hit':
                        dealer.deal(human, deck)
                    elif ask == 'stand':
                        co()
                        while dealer.hand.get_total() <= 16:
                            dealer.deal(dealer, deck)
                        human.show_hand()
                        dealer.show_hand(stand=True)

                        if human.hand.get_total() > dealer.hand.get_total() or dealer.hand.get_total() > 21:
                            print('Human wins')
                            print('Dealer loses')
                        else:
                            print('Dealer wins')
                            print('Human loses')
                        input('Press any key to continue. ')
                        done = True
                self.current_round += 1


Blackjack.run()
