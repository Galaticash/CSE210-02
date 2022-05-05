# Hilo

## Overview
Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

## Rules
- The player starts the game with 300 points.
- Individual cards are represented as a number from 1 to 13.
- The current card is displayed.
- The player guesses if the next one will be higher or lower.
- The the next card is displayed.
- The player earns 100 points if they guessed correctly.
- The player loses 75 points if they guessed incorrectly.
- If a player reaches 0 points the game is over.
- If a player has more than 0 points they decide if they want to keep playing.
- If a player decides not to play again the game is over.

### Matt Rucker's ideas (to be removed later)
- follow Brother Manley's lead on breaking apart the code into compostable chunks
- two classes, one that instantiates the game itself "game()", another that generates a card object "card()" that returns attributes value and points (just like the first example). If the game was to support more than one player, I would suggest we implement a player() class.
- the game() class should implement most of our methods. Think methods like firstcard(), nextcard(), playerinput(), displayscore(), playagain(), calculatescore(), etc.
- main() will only import game(), refer to the "broken" example. I'll build a sample structure and some basic code in the repo. I'll build the method card().
- you could choose to implement the playerinput method in the card() class, but I'm not sure it matters either way. For simplicity's sake, keeping the playerinput in the game() class would make more sense.