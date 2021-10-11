# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class Four_In_A_Row_Game:
    """
    The main object of the game, handling
    """
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

def get_input():
    """
    asks for input from user, validates it and returns the validated input
    """
    try:
        move = int(input("Make your move (1-7) or 0(end game): "))
        if move < 0 or move > 7:
            move = -1
            print("Please enter a number in the range of 0-7")
        return move
    except:
        print("Please enter a single number")
        return -1
    
def get_move_from_user():
    """
    
    """
    move = -1
    while move < 0:
        move = get_input()
    print("You chose to place you tile in column " + str(move))


def main():
    game = Four_In_A_Row_Game()

main()

#Proof of Concept is done - remake into OOP!
#Why oh why don't it accept the import!
#Need to add some checks 
# - is the column full?
# - did last move win the game?
