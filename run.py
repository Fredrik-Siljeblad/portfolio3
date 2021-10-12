# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class Four_In_A_Row_Game:
    """
    The main object of the game, handling the game board, the moves made and so forth.
    """
    def __init__(self):
        self.moves = []
        self.user = User()

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
        print("Please pick one of the following choiches:")
        print("0) End the game  1) Play the game.")
        user_input = input("Enter a choice. >>")

        # 0. End game
        if user_input == "0":
            self.end_game()
            return
        # 1. User vs User
        # - Perhaps - if the name is "Computer" make the computer play.
        elif user_input == "1":
            self.moves.append(input("Enter name of Player One. >>"))
            self.moves.append(input("Enter name of Player Two. >>"))
            self.play_game()
            return
        # Any other input.
        else:
            print("You need to make a valid choice.")
            self.start_game_menu()

    def end_game(self):
        """
        Ends the game
        """
        print("Goodbye, hope to see you again soon!")
        return

    def full_columns(self):
        """
        Returns a list of columns with 6 tiles in them.
        """
        is_full = []
        for column in range(1,7):
            if self.moves.count(column) > 5:
                is_full.append(column)
        return is_full

    def play_game(self):
        """
        The main game loop.
        """

        while not self.winner():
            #check which players turn it is
            #if it is a player (I.E. not "Computer") ask user to make a move.
            self.render_game()
            player = self.moves[(len(self.moves))%2]
            move = self.user.make_move(player, self.full_columns())
            if move > 0:
                self.moves.append(move)
            else:
                break
            self.end_game()

    def winner(self):
        """
        Function to determine if the game is won
        """
        #For testing purposes we just return 0.
        return 0

    def render_game(self):
        """
        takes the list of moves and turns it into a list of tiles placed on a board.
        """
        #Create the board, a list of 7 lists, each representing a column.
        board = [[], [], [], [], [], [], []]

        #Iterate throught the moves, alternate between the player tiles
        # and place them in the correct column.
        if len(self.moves) > 2:
            for move_nr in range(2, len(self.moves), 1):
                if move_nr%2 == 1:
                    tile = "@"
                else:
                    tile = "O"
                board[self.moves[move_nr] - 1].append(tile)

        print("\n\n\n\n\n")
        self.print_board(board)
        print("   -------------------")
        print("   1  2  3  4  5  6  7     8) 9) 0)")

    def print_board(self, board):
        """
        takes the list of the board and prints it in a somewhat pleasing format.
        """
        for line in range(5, -1, -1):
            print_line = " "
            for column in range(7):
                try:
                    tile = board[column][line]
                except:
                    tile = " "

                print_line = print_line + "  " + tile

            print(print_line)

class User:
    """
    The human player object handles input from the console.
    """
    def make_move(self, name, is_full):
        """
        asks for input from user, validates it and returns the validated input
        """
        move = -1
        while move < 0:
            try:
                move = int(input(f"{name},  make your move (1-7) or 0 (end game): >>"))
                if move > -1 and move < 8:
                    if is_full.count(move):
                        print(f"{name}, you cannot place more than six tiles in a column.")
                        move = -1
                    else:
                        return move
                if move < 0 or move > 7:
                    move = -1
                    print(f"{name}, please enter a number in the range of 0-7.")

            except:
                print("Please enter a single number.")
                move = -1

def main():
    """
    Main function
    """
    game = Four_In_A_Row_Game()
    game.welcome()


main()

#Proof of Concept is done - remake into OOP!
#Add human player

#Need to add some checks
# - is the column full?
# - did last move win the game?
# - must make each move twice, why?
# - need to make sure that each column doesn't take more than six tiles.
