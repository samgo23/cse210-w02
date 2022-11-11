# Sam Gordon - CSE 210 - HILO
import random

#The player starts the game with 300 points. - 
points = 300
game = True
#Individual cards are represented as a number from 1 to 13.
while game == True:
    print()
    card = random.randint(1,13)
    
#The current card is displayed.
    print(f'The card is: {card}')
#The player guesses if the next one will be higher or lower.
    player_guess = input('Higher or lower? [h/l]: ')
#The the next card is displayed.
    next_card = random.randint(1,13)
    
    print(f'Next card was {next_card}')
#The player earns 100 points if they guessed correctly.
#The player loses 75 points if they guessed incorrectly.
    if player_guess == 'l':
        if card > next_card:
            points += 100
        elif card < next_card:
            points -= 70
    elif player_guess == 'h':
        if card < next_card:
            points += 100
        elif card > next_card:
            points -= 70
    '''
    elif card < next_card and player_guess.lower == 'h':
        points -= 70
    elif card < next_card and player_guess.lower == 'l':
        points += 100
    elif card > next_card and player_guess.lower == 'l':
        points -= 70
    '''
    print(f'Your score is: {points}')
#If a player reaches 0 points the game is over.
    if points <= 0:
        game = False
#If a player has more than 0 points they decide if they want to keep playing.
    play_again = input('Play again [y/n]: ')
    if play_again == 'n':
        game = False
#If a player decides not to play again the game is over.
print('Thanks for playing')
