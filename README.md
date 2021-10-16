
# Four in a row

The game four in a row is played on a standing board with seven columns of six rows where two players alternate dropping
a tile into a column of their choice. The tile ends up at the bottom free row of the chosen column. The goal of the game 
is to get four of your own tiles in a row either vertically, horizontally or diagonally.

This is a command-line version of the game, suitable to learn how to play or to entertain.

Link to deployed game: https://p3-four-in-a-row.herokuapp.com/

## Features 

A digital representation of the game.
A visual representation of the game.
Two users can play the game.
One user can play against the computer.
Any number of users can watch two computer players play eachother.
Games can be saved and watched again.
Moves can be undone.


### Existing Features


- __A digital representation of the game.__

  Each game is simply stored as a Python list consisting of player1, player2, column nr for move#1, 
  column nr for move#2, ...

- __A visual representation of the game.__

The game is represented as a ASCII-graphic in the command window, as follows:

    -------------------


          O     @
          O  O  @
          @  @  O      
          @  O  O  O  @
    -------------------
    1  2  3  4  5  6  7
    The Game is over -Computer won!
    The game is over, please make a choice:
    8) Undo last move, 9) Save the game 0) Return to start menu.


- __User playing the game__

A human player gives input through entering single digit integers into the command line.
Two players sharing a computer can play eachother, the game prompts each player to make a move.


- __Computer playing the game__ 

There is a computer player able to process the digital game representation and make a move. At the 
start of a game the user enters names for both players. If any player is named 'Computer' the computer
player will make the moves for that player.

The computer player plays a far from perfect game, but should make for a good opponent for anyone learning
the game.


- __Computer vs Computer__ 

By naming both player one & player two as 'Computer' you can watch the computer play itself. A perfect 
computer player would win every game if it makes first move.

See: https://www.gamesver.com/is-connect-4-a-solved-game-what-does-that-even-mean/


- __Saving Games__ 

Any time during a game, including after the winning move has been made the game can be saved. Up to 10 
games can be saved (a design choice to keep in line with the other menu choices of 0)-9). If an eleventh
game is saved, the first one saved is dropped (FIFO).

Games are saved as a nested list in json format.


- __Loading Saved Games__

Instead of starting a new game one can load one of the previously saved games to finish it.


- __Watching Replays__

Saved games can also be watched move-by-move as replays.


- __Undo Move__

At any time during play, including after the winning move has been made a player can choose to undo his last move.
Since the computer is rather unimaginative the undo move is disabled in computer vs computer games, it simply would
repeat the same move again.


### Features Left to Implement

- Different computer players
- Ability to change players, I.E. load a computer vs computer game, change one of the players to
  a human player and use as a learning tool.


## Testing 

- By methodically going through the games menus I have managed to run through every option 
  without the program crashing.

      0) Exit game  1) Play a game 2) Load a Saved Game 3) Watch a Replay

      0) Exit game Works!

      1) Player vs Player:
        1-7) Making Moves Works!
        8) Undo Works!
        9) Save Works!
        0) Return to start_game_menu Works!

      1) Player vs Computer
        1-7) Making Moves Works!
        8) Undo Works!
        9) Save Works!
        0) Return to start_game_menu Works!

      1) Computer vs Player
        1-7) Making Moves Works!
        8) Undo Works!
        9) Save Works!
        0) Return to start_game_menu Works!

      1) Computer vs Computer   end menu only, and no Undo.
        9) Save Works!
        0) Return to start_game_menu Works!!

      2) Loading Saved Games Works!

      3) Watching Replay Works!

- By having the computer player play itself 100's of times I am reasonably confident that no
  moves in the game cause any problems.


### Validator Testing 

- Python PEP8 - http://pep8online.com/

The code checks out without remarks on the online PEP8 validator

- Pylance - https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance

The linter I use in VS Code gives no errors or warnings.

### Unfixed Bugs

- The final round of testing did not turn up any bugs.

## Deployment

- The code was deployed on Heroku.com by following the steps of the Deployment instruction
  video in the Code Institure programme material.


## Credits 

- W3 schools for being such a great source of basic programming knowledge.

### Content 

- The code is completely written by me.
