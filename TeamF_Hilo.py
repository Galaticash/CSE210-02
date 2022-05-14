# Team Members
# Ashley DeMott, Hailey Phipps, John Lydiksen, Matt Rucker
# This is a quick comment by John Lydiksen, showing that my system is set up to do pushes, pulls and commits.

import random

POINTS = {'right': 100, 'wrong': 75}
HIGH_CARD = 13

def main():
    game_one = Game()
    game_one.play_game()

    # print("Good game!")

class Card():
    """
        A card to be used in the game of Hilo.
        Can tell it's value, and randomize it.
    """
    def __init__(self):
        self.value = 0
    
    def change_value(self):
        self.value = random.randint(1, HIGH_CARD)

class Game():
    """
        Game of Hilo. User can guess if a the next card
         will be higher or lower than the current card
    """
    
    def __init__(self):
        """ 
            Initialize the attributes of the self (instance of the Game)
        """
        self.score = 300
        self.point_system = POINTS
        self.current_card = Card()
        self.next_card = Card()

    def play_game(self):
        """
            Plays a game of Hilo (Higher or Lower)
            Exits when the user decides to quit, or wins the game
        """
        game_over = False
        # While the game has not ended
        while not game_over:
        
            # Draw a card.
            self.current_card.change_value()
            print(f"\nThe card is {self.current_card.value}")

            # Ask the user to guess higher or lower.
            user_input = input("Higher or lower? [h/l] ")
            
            # Draw a new card.
            self.next_card.change_value()
            print("The next card is ", self.next_card.value)
            
            # Check the user's input.
            if user_input == 'h':
                # If the user correctly guessed higher
                if self.next_card.value > self.current_card.value:
                    self.score += self.point_system["right"]
                else:
                    # Card was lower
                    self.score -= self.point_system["wrong"]
            elif user_input == 'l':
                # If the user correctly guessed lower
                if self.next_card.value < self.current_card.value:
                    self.score += self.point_system["right"]
                else:
                    # Card was higher
                    self.score -= self.point_system["wrong"]
            # User chose to quit the game
            elif user_input == 'q':
                game_over = True
            else:
                print("Didn't choose a valid choice [h/l] - or q to quit")
            
            # After scoring, check if reached 0 points.
            if self.score <= 0:
                # No more points, game over.
                game_over = True
            
            # Print the user's score
            print("Your score is: ", self.score)
        # Exit while loop, game over.    
        print("Game over")

if __name__ == "__main__":
    main()
