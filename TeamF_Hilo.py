# Team Members
# Ashley DeMott, Hailey Phipps, John Lydiksen, Matt Rucker


import random

POINTS = {'right': 100, 'wrong': 75}

def main():
    game_one = Game() # instance
    game_one.play_game()

    print("Good game!")
    #person_one = Person()
    #person_two = Person()

    # person_one.first_name = "Sarah"
    # person_two.first_name = "Johnathan"

    # person_one.print_name()
    # person_two.print_name()

    #print(f"Game score: {game_one.score}")
    #print(f"Game score: {game_two.score}")

    # - - - - - - 


class Card():
    def __init__(self):
        self.value = 0
    
    def change_value(self):
        self.value = random.randint(1, 50)

class Game():
    
    def __init__(self):
        """ Initialize the attributes of the self (instance of the Game)"""
        self.score = 300
        self.point_system = POINTS
        self.current_card = Card()
        self.next_card = Card()

    def play_game(self):
        
        game_over = False
        while not game_over:
        
            # Draw a card
            self.current_card.change_value()
            print(f"\nThe card is {self.current_card.value}")
            user_input = input("Higher or lower? [h/l] ")
            
            # Draw a new card
            self.next_card.change_value()
            print("The next card is ", self.next_card.value)
            
            # user input check
            if user_input == 'h':
                if self.next_card.value > self.current_card.value:
                    #print("right!")
                    # self.score = self.score + 100
                    self.score += 100
                else:
                    #print("wrong!")
                    self.score -= 75
            elif user_input == 'l':
                if self.next_card.value < self.current_card.value:
                    #print("right!")
                    self.score += 100
                else:
                    #print("wrong!")
                    self.score -= 75
            elif user_input == 'q':
                game_over = True
            else:
                print("Didn't choose a valid choice [h/l] or q to quit")
            
            # after scoring, check if reached 0 points
            if self.score <= 0:
                game_over = True

            print("Your score is: ", self.score)
        print("Game over")

    
class Person():
    def __init__(self):
        self.first_name = ""
        self.family_name = "Smith"
    def print_name(self):
        print(f"My name is {self.family_name}, {self.first_name}")

if __name__ == "__main__":
    main()
