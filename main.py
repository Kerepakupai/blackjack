import random
import os
from functools import reduce
from art import logo


def first_hand(cards):
    random_cards = []
    for i in range(2):
        card = random.choice(cards)
        random_cards.append(card)
    return random_cards


def total(cards):
    return reduce(lambda x, y: x + y, cards)


def print_final_hand(user_cards, dealer_cards):
    print(f"    Your final hand: {user_cards}, final score: {total(user_cards)}")
    print(f"    Computer's final hand: {dealer_cards}, final score: {total(dealer_cards)}")


def print_first_hand(user_cards, dealer_cards):
    print(f"    Your cards: {user_cards}, current score: {total(user_cards)}")
    print(f"    Computer's first card: {dealer_cards[0]}")


def main():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
    while answer == 'y':
        user_cards = []
        dealer_cards = []
        another_card = True

        user_cards = first_hand(cards)
        dealer_cards = first_hand(cards)

        os.system('clear')
        print(logo)
        
        print_first_hand(user_cards, dealer_cards)

        if total(user_cards) == 21:
            print_first_hand(user_cards, dealer_cards)
            print("Win with a Blackjack 😎")
        else:
            while another_card and total(user_cards) <= 21:
                option = input("Type 'y' to get another card, type 'n' to pass: ")
                if option == 'y':
                    card = random.choice(cards)
                    user_cards.append(card)
                    print_first_hand(user_cards, dealer_cards)
                else:
                    another_card = False
            if total(dealer_cards) == 21:
                print_final_hand(user_cards, dealer_cards)
                print("You lose. Opponent get a Blackjack 😎")
            else:
                if total(user_cards) <= 21:
                    while total(dealer_cards) < 17:
                        card = random.choice(cards)
                        dealer_cards.append(card)

                    print_final_hand(user_cards, dealer_cards)

                    if total(dealer_cards) <= 21:
                        if total(user_cards) > total(dealer_cards):
                            print("You win 😁")
                        elif total(user_cards) < total(dealer_cards):
                            print("You lose 😭")
                        else:
                            print("Draw 🙃")
                    else:
                        print("Opponent went over. You win 😁")
                else:
                    print_final_hand(user_cards, dealer_cards)
                    print("You went over. You lose 😭")

        answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if __name__ == '__main__':
    main()