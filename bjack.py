import random

 

class Card:
    def __init__(self, suit, value, card_value):         
        self.suit = suit
        self.value = value
        self.card_value = card_value



 

def blackjack_game(deck):
 

    player_cards = []
    dealer_cards = []

    player_score = 0
    dealer_score = 0

    def __repr__(self):
        return player_cards


    while len(player_cards) < 2:
 

        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)
 

        player_score += player_card.card_value
 

        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10
 
 
        print("PLAYER CARDS:  ")
        print(__repr__)
        print("PLAYER SCORE = ", player_score)
 
        input()
 

        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
 

        dealer_score += dealer_card.card_value
 

        print("DEALER CARDS: ")
        if len(dealer_cards) == 1:

            print("DEALER SCORE = ", dealer_score)
        else:   
            print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)
 
 

        if len(dealer_cards) == 2:
            if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                dealer_cards[1].card_value = 1
                dealer_score -= 10
 
        input()
 
    if player_score == 21:
        print("PLAYER HAS A BLACKJACK!!!!")
        print("PLAYER WINS!!!!")
        quit()
 

 

    print(f"DEALER CARDS: {dealer_cards[:-1]}")
    print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)
 
    print() 
 
    print(f"PLAYER CARDS: {player_cards} ")

    print("PLAYER SCORE = ", player_score)
 

    while player_score < 21:
        choice = input("Enter H to Hit or S to Stand : ")
 
        if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            print("Wrong choice!! Try Again")
   

        if choice.upper() == 'H':

            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)
 

            player_score += player_card.card_value
 

            c = 0
            while player_score > 21 and c < len(player_cards):
                if player_cards[c].card_value == 11:
                    player_cards[c].card_value = 1
                    player_score -= 10
                    c += 1
                else:
                    c += 1 
 
   
 

            print(f"DEALER CARDS: {dealer_cards[:-1]}")
            print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)
 
            print()
 
            print(f"PLAYER CARDS: {player_cards} ")
            print("PLAYER SCORE = ", player_score)
             

        if choice.upper() == 'S':
            break
 
 
  

    print(f"PLAYER CARDS: {player_cards} ")

    print("PLAYER SCORE = ", player_score)
 
    print()
    print("DEALER IS REVEALING THE CARDS....")
 
    print(f"DEALER CARDS: {dealer_cards}")

    print("DEALER SCORE = ", dealer_score)
 

    if player_score == 21:
        print("PLAYER HAS A BLACKJACK")
        quit()
 
    if player_score > 21:
        print("PLAYER BUSTED!!! GAME OVER!!!")
        quit()
 
    input() 
 
    while dealer_score < 17:
 
 
        print("DEALER DECIDES TO HIT.....")
 

        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
 

        dealer_score += dealer_card.card_value
 

        c = 0
        while dealer_score > 21 and c < len(dealer_cards):
            if dealer_cards[c].card_value == 11:
                dealer_cards[c].card_value = 1
                dealer_score -= 10
                c += 1
            else:
                c += 1

        print(f"PLAYER CARDS: {player_cards} ")
 
        print("PLAYER SCORE = ", player_score)
 
        print()
 
        print(f"DEALER CARDS: {dealer_cards[:-1]}")

        print("DEALER SCORE = ", dealer_score)      
 
        input()
 

    if dealer_score > 21:        
        print("DEALER BUSTED!!! YOU WIN!!!") 
        quit()  
 

    if dealer_score == 21:
        print("DEALER HAS A BLACKJACK!!! PLAYER LOSES")
        quit()
 

    if dealer_score == player_score:
        print("TIE GAME!!!!")
 

    elif player_score > dealer_score:
        print("PLAYER WINS!!!")                 
 

    else:
        print("DEALER WINS!!!")                 
 
if __name__ == '__main__':
 

    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
 
 
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
 

    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
  
    cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
 

    deck = []
 

    for suit in suits:
 

        for card in cards:
 

            deck.append(Card(suits_values[suit], card, cards_values[card]))
     
    blackjack_game(deck)    