class Four_In_A_Row_Game:
    def __init__(self):
        self.moves = []
    

    def render_game(self):
        """
        takes the list of moves and turns it into a list of tiles placed on a board.
        """
        #Slice the actual moves out of the game.
        moves = self.moves
        
        #Create the board, a list of 7 lists, each representing a column.
        board = [[], [], [], [], [], [], []]
        
        #Iterate throught the moves, alternate between the player tiles and place them in the correct column.
        for move_nr in range(len(moves)):
            if move_nr%2 == 1:
                tile = "@"
            else:
                tile = "O"
            
            board[moves[move_nr] - 1].append(tile)

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