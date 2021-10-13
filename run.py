# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class FourInARowGame:
    """
    The main object of the game, handling the game board, the moves made and so forth.
    """
    def __init__(self):
        self.moves = []
        self.user = User()
        self.board = [[], [], [], [], [], [], []]

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

        self.print_board()
        while not self.winner():
            #check which players turn it is
            #if it is a player (I.E. not "Computer") ask user to make a move.

            player = self.moves[(len(self.moves))%2]
            move = self.user.make_move(player, self.full_columns())
            if move > 0:
                self.moves.append(move)
                self.render_game()
                self.print_board()
            else:
                self.end_game()
                break

    def winner(self):
        """
        Function to determine if the game is won
        """
        if len(self.moves) < 2:
            return 0
        elif self.count_rows() < 4:
            return 0
        else:
            return 1

    def count_rows(self):
        """
        Counts tiles in a row in columns, rows and both diagonals.
        """
        max_in_row = 0

        #For rows, columns & both diagonals, make a row list and send to count_row()
        print("Columns:")
        for row in self.board:
            this_max = self.count_row(row)
            self.print_row(row, this_max)
            max_in_row = max(max_in_row, this_max)
        #Then rows
        print("Rows:")

        for row in self.transpose(self.board):
            this_max = self.count_row(row)
            this_max = self.count_row(row)
            self.print_row(row, this_max)
            max_in_row = max(max_in_row, this_max)

        #Go through all "upwards" diagonals
        print("The 'upwards' diagonals:")
        for row in self.up_diagonal(self.board):
            this_max = self.count_row(row)
            this_max = self.count_row(row)
            self.print_row(row, this_max)
            max_in_row = max(max_in_row, this_max)
        print("The'downwards' diagonals:")
        for row in self.down_diagonal(self.board):
            this_max = self.count_row(row)
            this_max = self.count_row(row)
            self.print_row(row, this_max)
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
        while iterate_x < range(m_coln + m_rown - 1):
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
        while iterate_x < range(m_coln + m_rown - 1):
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

    def print_row(self, row, my_max):
        """
        Function mainly for debugging
        """
        if my_max == 0:
            return
        to_print = ", Row: "
        for element in row:
            to_print += str(element)
        to_print = f"Max: {my_max} " + to_print
        print(to_print)

    def render_game(self):
        """
        takes the list of moves and turns it into a list of tiles placed on a board.
        """
        #Clean the board, a list of 7 lists, each representing a column.
        self.board = [[], [], [], [], [], [], []]

        #Iterate throught the moves, alternate between the player tiles
        # and place them in the correct column.
        if len(self.moves) > 2:
            for move_nr in range(2, len(self.moves), 1):
                if move_nr%2 == 1:
                    tile = "@"
                else:
                    tile = "O"
                self.board[self.moves[move_nr] - 1].append(tile)
        #Then we want to fill the rest of the board with " "
        for column in self.board:
            while len(column) < 7:
                self.board.append(" ")

    def print_board(self):
        """
        takes the list of the board and prints it in a somewhat pleasing format.
        """
        print("\n\n\n\n\n")
        for row in range(5, -1, -1):
            print_line = " "
            for column in range(7):
                if row < len(self.board[column]):
                    tile = self.board[column][row]
                print_line = print_line + "  " + tile
            print(print_line)
        print("   -------------------")
        print("   1  2  3  4  5  6  7     8) 9) 0)")

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
    game = FourInARowGame()
    #game.welcome()
    #game.moves.append("Player O")
    #game.moves.append("Player @")
    #game.play_game()
    #game.print_row(["@", "@", "@", "@", "@"], 5)
    matrix = [["00","01","02"], ["10","11","12"], ["20","21","22"], ["30","31","32"]]
    diagonal = game.down_diagonal(matrix)
    print(matrix)
    print(diagonal)



main()

#Add human player
# - did last move win the game? - YAY
# calculates new board before adding the move?
