#######################################################################
#Student Name           :Sayak Ghosh
#ID                     :873464327
#Description of Program :simulates a card game by declaring a class and
#few methonds
#######################################################################
import random
class Card:
    '''A Card object represents a single card. It should have two string
    attributes: suit and rank'''

    def __init__(self,value,suit):
        '''sets the rank and the suit from its parameters'''
        self.suit = suit
        self.value = value

    def __str__(self):
        '''returns the card's value in the form "<rank> of <suit>"'''
        return f'{self.value} of {self.suit}'

    def __repr__(self):
        '''returns an appropriate string for this object'''
        return f'Card({self.value} of {self.suit})'

class Deck:
    '''A Deck object represents an entire deck of cards . It should have a
     single attribute cards, which is a list of Card objects currently in
     the deck'''

    def __init__(self,Cards):
        '''sets cards from its parameters'''
        self.Cards = list(Cards)
        #self.number_of_cards = len(Cards)

    def __str__(self):
        '''returns the string "Deck of <number-of-cards> cards"'''
        return f'Deck of {len(self.Cards)} of cards'

    def __repr__(self):
        '''returns an appropriate string for this object'''
        return f'Deck({repr(self.Cards)})'

    def shuffle(self):
        '''which randomly shuffles the cards in the deck'''
        #randomises the list by emptying one list and copy into another
        self.random_card =[]
        if len(self.Cards) == 0:
            raise ValueError('No more Cards in the Deck')
        print(self.Cards)
        while len(self.Cards)>0:
            self.random_card += [self.Cards.pop(random.randint(0,len(self.Cards)-1))]
        self.Cards = self.random_card[:]
        #print(self.Cards)
        return self.Cards


    def draw(self):
        '''removes and returns the first card from the deck.
        This method should raise a ValueError if the deck is empty'''
        #raise Value error if deck is empty,and this method pops a element from
        #the list
        try:
            if len(self.Cards) == 0:
                raise ValueError('No more Cards in the Deck')
            return self.Cards.pop(0)

        except IndexError:
            print('No more Cards in the Deck')


    def size(self):
        '''returns the number of cards left in the deck'''
        return len(self.Cards)


def deal(Deck,players,hand_size):
    '''take three parameters: a Deck object, an integer player_count, and an
    integer hand_size. It should simulate the setup of a card game'''
    Deck.shuffle()
    players_card =[]
    #prints cards per player
    for i in range(players):
        hand_card =[]
        for j in range(hand_size):
            hand_card += [Deck.Cards.pop(0)]
        print('Player ',i+1,'got: ',hand_card)
