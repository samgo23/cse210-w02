# Import Card methods 
from game.card import Card
card = Card()
next_card = Card()



class Director:
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        
        
        self.game = True
        self.points = 300
        self.player_guess = ''
        self.play_again = ''
        self.card1 = 0
        self.card2 = 0
        
        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.game == True:
            print()
            self.display()
            self.check_card()
            self.keep_playing()
            

    #inout phase
    def display(self):
        '''The current card is displayed. The player guesses if the next one will be higher or lower. The the next card is displayed.
        
        Args:
            self (Director): An instance of Director.
        '''
        self.card1 = card.draw_card()
        self.card2 = next_card.draw_card()

        print(f'The card is: {self.card1}')
        self.player_guess = input('Higher or lower? [h/l]: ')
        print(f'Next card was {self.card2}')
        

        
    #update phase
    def check_card(self):
        '''The player earns 100 points if they guessed correctly. The player loses 75 points if they guessed incorrectly.

        Args:
            self (Director): An instance of Director.
        '''
        
        if self.player_guess == 'l':
            if self.card1 > self.card2:
                self.points += 100
            elif self.card1 < self.card2:
                self.points -= 70
        elif self.player_guess == 'h':
            if self.card1 < self.card2:
                self.points += 100
            elif self.card1 > self.card2:
                self.points -= 70

    #output phase
    def keep_playing(self):
        '''Display the card and score. If a player reaches 0 points the game is over.
        
        Args:
            self (Director): An instance of Director.
        '''
        if self.points <= 0:
            self.game = False
        
        print(f'Your score is: {self.points}')
        self.play_again = input('Play again [y/n]: ')
        if self.play_again == 'n':
            self.game = False
    



        