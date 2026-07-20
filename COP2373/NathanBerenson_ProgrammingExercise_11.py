
import random

#A class which creates & randomizes the poker deck
class Deck:


    #Defines the value of the cards
    def __init__(self, n_decks=1):
        #Builds the deck of cards
        self.card_list = [

            num + suit
            #Adds suit logos
            for suit in '\u2665\u2666\u2663\u2660'

            #Defines the value of the cards
            for num in 'A23456789TJQK'

            #Defines the number of decks being used
            for deck in range(n_decks)]

        #An empty list where the used cards go
        self.cards_in_play_list = []

        #An empty list where unused cards go
        self.discards_list = []

        #Shuffles all the cards
        random.shuffle(self.card_list)

    #Deals the cards
    def deal(self):

        if len(self.card_list) < 1:

            random.shuffle(self.discards_list)

            #The discard pile becomes the new deck
            self.card_list = self.discards_list

            #Creates a new discard pile
            self.discards_list = []
            print('Reshuffling')

        #.pop() removes the last card and returns it
        new_card = self.card_list.pop()

        #adds new_card to play
        self.cards_in_play_list.append(new_card)


        return new_card

    #Starts a new hand
    def new_hand(self):

        #All cards in play goes into the discard pile
        self.discards_list += self.cards_in_play_list

        #clears all the cards in play
        self.cards_in_play_list.clear()


dk = Deck(6)

hand = []

#Runs the deal function in Deck class
for i in range(5):
    hand.append(dk.deal())

#Prints and labels the user's hand
for i in range(len(hand)):
    print(f"{i+1}: {hand[i]}")

switch = input("Which card(s) would you like to switch?(e.g., 1 3 5): ")

#Removes whitespaces
choices = switch.split()


for x in choices:
    #Isolates the cards the user wants to switch
    index = int(x)-1

    #Changes those isolated cards only
    hand[index] = dk.deal()


print("\nFinal hand")

#Prints the new hand
for i in range(len(hand)):
    print(f"{i+1}: {hand[i]}")
