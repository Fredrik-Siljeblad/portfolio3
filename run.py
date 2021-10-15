# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
A python project for a command-line four-in-a-row game
"""

import random
import json

class FourInARowGame:
    """
    The main object of the game, handling the game board, the moves made and so forth.
    """
    def __init__(self):
        self.moves = []
        self.user = User(self)
        self.computer = Computer(self)

    def welcome(self):
        """
        Welcomes the user to the game, and presents the start game menu.
        """
        print("Welcome to the Python Four-In-A-Row game.")
        self.start_game_menu()

    def start_game_menu(self):
        """
        Start menu of the game
        """
        self.moves.clear()
        print("Please pick one of the following choiches:")
        print("0) Exit game  1) Play a game 2) Load a Saved Game 3) Watch a Replay")
        user_input = input(" >> ")
        # 0. End game
        if user_input == "0":
            self.end_game()
        # 1. Play game
        elif user_input == "1":
            print("If entering 'Computer' as name of either player the moves of")
            print("that player will be made by the computer.")
            print("Enter name of Player One.")
            self.moves.append(input(" >> "))
            print("Enter name of Player Two.")
            self.moves.append(input(" >> "))
            self.play_game()
        # 2. Load game
        elif user_input == "2":
            self.load_game()
        # 3. Watch replay
        elif user_input == "3":
            self.view_replay()
        # Any other input.
        else:
            print("You need to make a valid choice.")
            self.start_game_menu()

    def play_game(self):
        """
        The main game loop.
        """

        self.print_board(self.render_game(self.moves))
        while not self.winner():
            #check which players turn it is
            player = self.moves[(len(self.moves))%2]
            if player == self.moves[0]:
                opponent = self.moves[1]
            else:
                opponent = self.moves[0]
            if player == "Computer":
                if opponent == "Computer":
                    input("Press <Enter> to continue.")
                move = self.computer.make_move(player, self.full_columns())
            else:
                move = self.user.make_move(player, self.full_columns())
            if move == 8:
                self.undo_move()
            elif move == 0:
                self.start_game_menu()
                break
            else:
                self.moves.append(move)
                self.print_board(self.render_game(self.moves))

        self.end_of_game_menu()

    def end_of_game_menu(self):
        """
        Menu that shows when the game is won. Allows to undo last move or return to start
        """
        print("The game is over, please make a choice:")
        print("8) Undo last move, 9) Save the game 0) Return to start menu.")
        choice = -1
        while choice < 0 :
            try:
                choice = int(input(" >>"))
                if choice == 8:
                    self.undo_move()
                    self.play_game()
                elif choice == 9:
                    self.save_game()
                    print("Game Saved.")
                    self.start_game_menu()
                elif choice == 0:
                    self.start_game_menu()
                else:
                    choice = -1
            except: # pylint: disable=bare-except
                choice = -1

    def end_game(self):
        """
        Ends the game
        """
        print("Goodbye, hope to see you again soon!")
        quit()

    def save_game(self):
        """
        Saves the current game into the save4.json file.
        Only the last 10 saved games will be retained.
        """
        try:
            with open("save4.json", encoding="UTF-8") as json_file:
                saved_games = json.load(json_file)
        except: # pylint: disable=bare-except
            saved_games = []
        saved_games.append(self.moves)
        while len(saved_games) > 10:
            saved_games.pop(0)
        with open("save4.json",mode="w", encoding="UTF-8") as outfile:
            json.dump(saved_games, outfile)

    def load_game(self):
        """
        Lets the user pick up the loaded game at the saved point.
        """
        self.moves = self.get_game_from_file("continue playing")
        self.play_game()

    def view_replay(self):
        """
        Load a saved game from the save-file, and shows the replay one
        move at a time
        """
        replay_moves = self.get_game_from_file("watch replay")
        replay = []
        replay.append(replay_moves[0])
        replay.append(replay_moves[1])
        for index in range(2, len(replay_moves)-1):
            player = replay[index%2]
            column = replay_moves[index]
            replay.append(column)
            self.print_board(self.render_game(replay))
            print(f"{player} plays column {column}.")
            input("<Enter> to continue")
        self.start_game_menu()

    def get_game_from_file(self, msg):
        """
        Allows the player to select a saved game and returns its moves
        """
        try:
            with open("save4.json", encoding="UTF-8") as json_file:
                saved_games = json.load(json_file)
        except: # pylint: disable=bare-except
            print("There are no saved games.")
            self.start_game_menu()
        index = 0
        for moves in saved_games:
            player_1 = moves[0]
            player_2 = moves[1]
            nr_of_moves = len(moves) - 2
            print(f"{index}) - {player_1} vs {player_2}, {nr_of_moves} moves made.")
            index += 1
        choice = -1
        while choice < 0:
            print(f"Please choose game to {msg} (0-{len(saved_games) - 1}).")
            choice = input(" >> ")
            try:
                choice = int(choice)
                if choice > len(saved_games) - 1:
                    choice = -1
            except: # pylint: disable=bare-except
                choice = -1
        return saved_games[choice]

    def full_columns(self):
        """
        Returns a list of columns with 6 tiles in them.
        """
        is_full = []
        for column in range(1,7):
            if self.moves.count(column) > 5:
                is_full.append(column)
        return is_full

    def winner(self):
        """
        Function to determine if the game is won
        """
        # if len(moves) < 10 there can be no winner
        # to save time we don't bother counting.
        if len(self.moves) < 10:
            return 0
        # if there's 4 in a row, the last player to place a 
        # tile is the winner
        if self.count_rows(self.render_game(self.moves)) == 4:
            winner = self.moves[(1 + len(self.moves))%2]
            print(f"The Game is over - {winner} won!")
            return 1
        # if there's no winner and all positions on the board
        # are filled the game is a draw and over.
        if len(self.moves) == 44:
            print("The game is over - it was a draw!")
            return 1
        else:
            return 0

    def count_rows(self, board):
        """
        Counts tiles in a row in columns, rows and both diagonals.
        """
        max_in_row = 0
        #Columns
        for row in board:
            this_max = self.count_row(row)
            max_in_row = max(max_in_row, this_max)
        for row in self.transpose(board):
            this_max = self.count_row(row)
            max_in_row = max(max_in_row, this_max)
        for row in self.up_diagonal(board):
            this_max = self.count_row(row)
            max_in_row = max(max_in_row, this_max)
        for row in self.down_diagonal(board):
            this_max = self.count_row(row)
            max_in_row = max(max_in_row, this_max)
        return max_in_row

    def transpose(self, matrix):
        """
        returns transposed matrix
        """
        return list(map(list, zip(*matrix)))

    def up_diagonal(self, matrix):
        """
        returns a 2D-list that contains the lower-left to upper-right diagonals of matrix
        """
        m_coln = len(matrix)
        m_rown = len(matrix[0])
        diagonal = []
        iterate_x = 0
        while iterate_x < (m_coln + m_rown - 1):
            diagonal.append([])
            iterate_x += 1
        for m_row in range(m_rown):
            for m_col in range(m_coln):
                element = matrix[m_col][m_row]
                diagonal[m_rown - 1 - m_row + m_col].append(element)
        return diagonal

    def down_diagonal(self, matrix):
        """
        returns a 2D-list that contains the upper-left to lower-right diagonals of matrix
        """
        m_coln = len(matrix)
        m_rown = len(matrix[0])
        diagonal = []
        iterate_x = 0
        while iterate_x < (m_coln + m_rown - 1):
            diagonal.append([])
            iterate_x += 1
        for m_col in range(m_coln):
            for m_row in range(m_rown):
                element = matrix[m_col][m_row]
                diagonal[m_rown + m_coln - 2 - m_row - m_col].append(element)
        return diagonal

    def count_row(self, row):
        """
        Function that returns the maximum number of continous tiles in a given row
        """
        last_tile = " "
        max_in_row = 0
        in_row = 0
        for tile in row:
            if tile == " ":
                max_in_row = max(in_row, max_in_row)
                last_tile = tile
                in_row = 0
            elif tile != last_tile:
                max_in_row = max(in_row, max_in_row)
                last_tile = tile
                in_row = 1
            else:
                in_row += 1
        return max(in_row, max_in_row)

    def render_game(self, my_moves):
        """
        takes the list of moves and turns it into a list of tiles placed on a board.
        """
        #Clean the board, a list of 7 lists, each representing a column.
        my_board = [[], [], [], [], [], [], []]

        #Iterate throught the moves, alternate between the player tiles
        # and place them in the correct column.
        if len(my_moves) > 2:
            for move_nr in range(2, len(my_moves), 1):
                if move_nr%2 == 1:
                    tile = "@"
                else:
                    tile = "O"
                my_board[my_moves[move_nr] - 1].append(tile)
        #Then we want to fill the rest of the board with " "
        for column in my_board:
            while len(column) < 7:
                column.append(" ")
        return my_board

    def print_board(self, my_board):
        """
        takes the the board and prints it in a somewhat pleasing format.
        """
        print("\n\n\n\n\n")
        print("   -------------------")
        for row in range(5, -1, -1):
            print_line = " "
            for column in range(7):
                if row < len(my_board[column]):
                    tile = my_board[column][row]
                    print_line = print_line + "  " + tile
            print(print_line)
        print("   -------------------")
        print("   1  2  3  4  5  6  7")

    def undo_move(self):
        """
        Turns the game back in time to the point before the last non-computer move was made.
        """
        #check which players turn it is _to_make_a_move!!
        print(self.moves)
        if len(self.moves) < 4:
            print("You have no moves to undo!")
            return
        self.moves.pop()
        self.moves.pop()
        self.print_board(self.render_game(self.moves))

class User:
    """
    The human player object handles input from the console.
    """
    def __init__(self, game):
        self.game = game

    def make_move(self, name, is_full):
        """
        asks for input from user, validates it and returns the validated input
        """
        move = -1
        while move < 0:
            print(f"{name},  enter a move 1-7), undo last move 8),")
            print("  save game 9) or return to start menu 0).")
            try:
                move = int(input(" >> "))
                if move == 9:
                    print("Trying to save the game.")
                    self.game.save_game()
                    print("Game Saved!")
                    move = -1
                if move > -1 and move < 9:
                    if is_full.count(move):
                        print(f"{name}, you cannot place more than six tiles in a column.")
                        move = -1
                    else:
                        return int(move)
                if move < 0 or move > 9:
                    move = -1
                    print("Please enter a single number.")
            except: # pylint: disable=bare-except
                print("Please enter a single number.")
                move = -1


class Computer:
    """
    The computer player
    """
    def __init__(self, game):
        self.game = game

    def make_move(self, name, is_full):
        """
        Returns a move (I.E an integer 1-7)
        """
        #Version 2) Evaluate move:
        best_moves = []
        best_value = 10000 #Should be enough to allow for one valid move
        for move in range(1,8):
            if not is_full.count(move):
                moves = self.game.moves.copy()
                move_value = self.evaluate_move(move, moves)
                if move_value < best_value:
                    best_value = move_value
                    best_moves.clear()
                    best_moves.append(move)
                elif move_value == best_value:
                    best_moves.append(move)
        move = best_moves[random.randint(0, len(best_moves) - 1)]
        print(f"{name} places a tile in column {move}")
        return move

    def evaluate_move2(self, move, moves, move_values):
        """
        An attempt at using recursion to find the best move
        As of now not used
        """
        #to use this change the evaluation numbers to where 0 is average.
        my_moves = moves.copy()
        my_moves.append(move)
        my_move_values = move_values.copy()
        #move_values[0] = number of future moves we're looking at.
        for index in range(1,8):
            if my_move_values[index] == 10000:
                #Do not pursue this move.
                pass
            elif my_move_values[index] == -10000:
                #This branch leads to victory
                return my_move_values
            else:
                move_evaluation = self.evaluate_move(index, my_moves)
                if move_evaluation == -1:
                    if my_move_values[0]%2:
                        #Opponent wins
                        my_move_values[index] = 10000
                    else:
                        #I win
                        my_move_values[index] = -10000
                        return my_move_values
                else:
                    my_move_values[index] += move_evaluation
                self.evaluate_move2(index, my_moves, move_values)

    def evaluate_move(self, move, moves):
        """
        returns an evaluation of a move. Lower is better
        """
        if len(moves)%2:
            my_tile = "@"
        else:
            my_tile = "O"
        moves.append(move)
        my_board = self.game.render_game(moves)
        in_line = self.game.count_rows(my_board)
        #If this move wins me the game right away return -1
        if in_line == 4:
            return -1
        return_value = 50
        return_value += abs(move - 4)
        for column in my_board:
            evaluation = self.evaluate_row(column, my_tile)
            if evaluation:
                return_value += self.evaluate_row(column, my_tile)
        for row in self.game.transpose(my_board):
            evaluation = self.evaluate_row(row, my_tile)
            if evaluation:
                return_value += evaluation
        for row in self.game.up_diagonal(my_board):
            evaluation = self.evaluate_row(row, my_tile)
            if evaluation:
                return_value += evaluation
        for row in self.game.down_diagonal(my_board):
            evaluation = self.evaluate_row(row, my_tile)
            if evaluation:
                return_value += evaluation
        return return_value

    def evaluate_row(self, row, my_tile):
        """
        Evaluates a row according to number of tiles in line in it
        """
        if my_tile == "O":
            your_tile = "@"
        else:
            your_tile = "O"
        row_value = 0
        last_tile = " "
        my_in_line = 0
        yours_in_line = 0
        open_tile = 0
        for tile in row:
            if tile == " ":
                open_tile += 1
                if last_tile == my_tile:
                    value_change = self.calculate_row_value(1, open_tile, my_in_line)
                    row_value -= value_change
                    my_in_line = 0
                elif last_tile == your_tile:
                    value_change = self.calculate_row_value(-4, open_tile, yours_in_line)
                    row_value -= value_change
                    yours_in_line = 0
            elif tile == my_tile:
                my_in_line += 1
                if last_tile == your_tile:
                    value_change = self.calculate_row_value(-4, open_tile, yours_in_line)
                    row_value -= value_change
                    yours_in_line = 0
                    open_tile = 0
            else:
                yours_in_line += 1
                if last_tile == my_tile:
                    value_change = self.calculate_row_value(1, open_tile, my_in_line)
                    row_value -= value_change
                    my_in_line = 0
                    open_tile = 0
            last_tile = tile
            open_tile = min(1, open_tile)
            if tile == my_tile:
                value_change = self.calculate_row_value(1, open_tile, my_in_line)
                row_value -= value_change
            elif tile == your_tile:
                value_change = self.calculate_row_value(-4, open_tile, yours_in_line)
                row_value -= value_change
        return row_value

    def calculate_row_value(self, mine, open_ends, length):
        """
        Returns an adjustment to the rows value according to how it looks
        """
        value = 0
        if length == 3:
            value = 8 * open_ends * mine
        elif length == 2:
            value = 1 * open_ends * open_ends * mine
        return value

def main():
    """
    Main function
    """
    game = FourInARowGame()
    game.welcome()

main()
#remove teststuff from main()
# To do - cleanup of code, save & load.
# debug messages commented out, remove before deploying.
# possibly rewrite the computer player logic a bit to see if I can take advantage
# of recursion.
# ----------------------------------------
#
