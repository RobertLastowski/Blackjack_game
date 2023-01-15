'''
THIS A BLACK JACK GAME FOR ONE HUMAN PLAYERs AND COMPUTER DEALER
'''

import random


values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)
    
class Deck:
    
    def __init__(self):
        
        self.deck = []
        
        for suit in suits:
            for rank in ranks:
                # Create the Card object with for in for like taking every sut and creating every card(of every rank) with this suit
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'The deck has:' + deck_comp
            
                  
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
        
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1 
            
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(player_chips):
    while True:
        try:
            player_chips.bet = int(input("Please pick your bet: "))
        except:
            print("Please enter an intiger.")
            continue
        else:
            if player_chips.bet > player_chips.total:
                print("You don't have that much money! :c")
                continue
            else:
                print("Your bet is {}".format(player_chips.bet))
            break
        
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
    
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        if_hit = input("Do you want to hit or stand[h/s]?")
        
        if if_hit[0].lower() == "h":
            hit(deck,hand)
            
        elif if_hit[0].lower() == "s":
            print("You choose to stand. It's Dealer's turn")
            playing = False
            
        else:
            print("Please input s for stand or h for hit")
            continue
        break
    
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep = "\n")
    print("Dealer's Hand value = ", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand value = ", player.value)
    
def player_busts(player,dealer,chips):
    chips.lose_bet()
    print("Player's hand is over 21! You bust and you loose :/ You lost {} dollars and now your total is {}".format(chips.bet,chips.total))
        
def player_wins(player,dealer,chips):
    chips.win_bet()
    print("Player's hand is closer to 21! Player has won! :) You won {} dollars and now your total is {}".format(chips.bet,chips.total))


def dealer_busts(player,dealer,chips):
    chips.win_bet()
    print("Dealer's hand is over 21! Player has won! :) You won {} dollars and now your total is {}".format(chips.bet,chips.total))

    
def dealer_wins(player,dealer,chips):
    chips.lose_bet()
    print("Dealers's hand is closer to 21! Player has lost! :/ You lost {} dollars and now your total is {}".format(chips.bet,chips.total))

    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
    
chips = Chips()

while True:
    # Print an opening statement
    print("Welcome to the blackjack!! Let's begin the game!")
    
    # Create & shuffle the deck, deal two cards to each player
    play_deck = Deck()
    play_deck.shuffle()
    
    player = Hand()
    player.add_card(play_deck.deal())
    player.add_card(play_deck.deal())
    
    dealer = Hand()
    dealer.add_card(play_deck.deal())
    dealer.add_card(play_deck.deal())
    
    # Set up the Player's chips

    
    # Prompt the Player for their bet
    take_bet(chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(play_deck,player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player,dealer,chips)
            break
            
    if player.value <= 21:
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer.value < 17:
            print("Dealer is hiting..")
            dealer.add_card(play_deck.deal())

            # Show all cards
        show_all(player,dealer)    
            # Run different winning scenarios
        if player.value > dealer.value and player.value < 22:
            player_wins(player,dealer,chips)

        elif dealer.value > 21:
            dealer_busts(player,dealer,chips)

        elif player.value < dealer.value and dealer.value < 22:
            dealer_wins(player,dealer,chips)

        else:
            push(player,dealer,hand)
        
    # Ask to play again
    new_game = input("Would you like to play again? Please insert 'y' or 'n' ")
    
    if new_game.lower() == 'n':
        print("Thank you for playing! :)")
        break
    else:
        playing = True
        continue