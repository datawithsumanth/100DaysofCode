from art import blackjack_logo
import random

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,10, 10]

player_cards = []
dealer_cards = []
repeat = 'y'

def print_score():
    print(f"Your cards: {player_cards}, your score: {sum(player_cards)}")
    print(f"Dealer's cards: {dealer_cards}, dealer's score: {sum(dealer_cards)}")



def black_jack():
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    print_score()
    hit = input("Type 'y' to get another card, type 'n' to pass: ")
    while hit == 'y':
        player_cards.append(random.choice(cards))
        if sum(player_cards) <= 21:
            print_score()
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
            print_score()
            print("You lose, exceeded 21")
            hit == 'n'
            return
    else:
        comp_new_card = random.choice(cards)
        while sum(dealer_cards) + comp_new_card <=21:
            dealer_cards.append(comp_new_card)
        else:
            print_score()
            if sum(player_cards) == sum(dealer_cards):
                print("It's a tie")
            elif sum(player_cards) > sum(dealer_cards):
                print("You win!")
            else:
                print("Sorry, you lost!")




while repeat == 'y':
    repeat = input("Do you want play a game of BlackJack? Type 'y' or 'n': ")
    if repeat == 'y':
        print(blackjack_logo)
        black_jack()
    else:
        print("Goodbye!")


