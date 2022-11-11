import random

class Card:
    '''A random card is drawn from a deck of cards.

        
        Attributes:
            card (int): The number value associated with the card drawn, jacks, queens, and kings are 11, 12, and 13. Ace is 1.
        '''
    def __init__(self):
        '''Constructs a new instance of Card with a card attribute.

        Args:
            self (Card): An instance of Card.
        '''
        
        self.card = 0
        
    
    def draw_card(self):
        '''Generates a new random card

        Args:
            self (Card): An instance of Card.
        '''
        self.card = random.randint(1,13)
        return self.card
        



