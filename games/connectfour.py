from global_vars import LOG_LEVEL, LOG_DIR

import time
import logging

logger = logging.getLogger(__name__)

logging_dir = LOG_DIR + '/connectfour.log'
logging.basicConfig(filename=logging_dir,
                    level=LOG_LEVEL,
                    format='[%(asctime)s][%(levelname)s][%(filename)s] %(message)s')

class ConnectFour:

    def __init__(self):
        self._num_columns = 7
        self._column_height = 6
        self.board = [[" " for j in range(self._num_columns)] for i in range(self._column_height)]
        self._top = [self._column_height - 1 for _ in range(self._num_columns)]

        self._red_circle = "\xAE"
        self._blue_cross = "X" # \u5633 phan phan

        self.pieces_played = 0
    
        logger.info("Initialized Connect Four game board.")
    
    def resetBoard(self):
        self.board = [[" " for j in range(self._num_columns)] for i in range(self._column_height)]
        self.pieces_played = 0
    
    def checkWin(self):
        """
        Return 
        0   :   if game is not won yet and ongoing
        1   :   if Player 1 (Red) has won
        2   :   if Player 2 (Blue) has won
        3   :   if the game has finished in a draw
        """
        for i in range(self._column_height):
            for j in range(self._num_columns):
                if (i + 3) < self._column_height:
                    if self.board[i][j] == self.board[i+1][j] and \
                        self.board[i+1][j] == self.board[i+2][j] and \
                        self.board[i+2][j] == self.board[i+3][j]:
                            if self.board[i][j] == self._red_circle:
                                return 1
                            elif self.board[i][j] == self._blue_cross:
                                return 2
                if (j + 3) < self._num_columns:
                    if self.board[i][j] == self.board[i][j+1] and \
                        self.board[i][j+1] == self.board[i][j+2] and \
                        self.board[i][j+2] == self.board[i][j+3]:
                            if self.board[i][j] == self._red_circle:
                                return 1
                            elif self.board[i][j] == self._blue_cross:
                                return 2
                if (i + 3) < self._column_height and (j + 3) < self._num_columns:
                    if self.board[i][j] == self.board[i+1][j+1] and \
                        self.board[i+1][j+1] == self.board[i+2][j+2] and \
                        self.board[i+2][j+2] == self.board[i+3][j+3]:
                            if self.board[i][j] == self._red_circle:
                                return 1
                            elif self.board[i][j] == self._blue_cross:
                                return 2
                
                if (i + 3) < self._column_height and (j - 3) >= 0:
                    if self.board[i][j] == self.board[i+1][j-1] and \
                        self.board[i+1][j-1] == self.board[i+2][j-2] and \
                        self.board[i+2][j-2] == self.board[i+3][j-3]:
                            if self.board[i][j] == self._red_circle:
                                return 1
                            elif self.board[i][j] == self._blue_cross:
                                return 2
        
        if self.pieces_played == self._num_columns * self._column_height:
            return 3

        return 0

    def getColumnInput(self):
        col = input("Enter the column number where you want to drop your piece: ")
        while True:
            if (len(col) != 1) or (not col.isdigit()) or (int(col) >= self._num_columns):
                print(f"Invalid column number ! Please enter again.")
            elif self._top[int(col)] == -1:
                print(f"This column is already full! Please enter another column.")
            else:
                return int(col)

            col = input("Enter the column number where you want to drop your piece: ")


    def dropPiece(self, col, turn):
        if turn == 0:
            self.board[self._top[col]][col] = self._red_circle
        else:
            self.board[self._top[col]][col] = self._blue_cross
        
        self._top[col] -= 1
    
    def printBoard(self):
        print("-----------------------------")
        for i in range(len(self.board)):
            print("| " + " | ".join(self.board[i]) + " |")
        print("-----------------------------")
        print("| " + " | ".join([str(i) for i in range(self._num_columns)]) + " |")
    
    def printTurnInfo(self):
        try:
            if self.turn == 0:
                player_colour = "RED"
            else:
                player_colour = "BLUE"
        except Exception as e:
            print(f"Check if self.turn is defined, error: {e}")
        
        print()
        print(f"<---------- {player_colour} TO PLAY ---------->")
        print()
    
    def callResult(self, id):
        if id == 1:
            print(f"Red Player won the game !")
            logger.info(f"Red Player won the game !")
        elif id == 2:
            print(f"Blue Player won the game !")
            logger.info(f"Blue Player won the game !")
        elif id == 3:
            print(f"")
            logger.info(f"Game ended in a draw.")
    
    def begin(self):
        self.turn = 0
        while True:
            self.printBoard()
            self.printTurnInfo()
            
            col = self.getColumnInput()
            self.dropPiece(col, self.turn)

            self.pieces_played += 1

            winStatus = self.checkWin()
            if winStatus == 1:
                self.callResult(1)
                break
            elif winStatus == 2:
                self.callResult(2)
                break
            elif winStatus == 3:
                self.callResult(3)
                break
            else:
                self.turn = 1 - self.turn

        return


if __name__ == "__main__":
    game = ConnectFour()

    while True:
        game.begin()

        choice = input("< Press ENTER to Play Again, input Q to Quit >")
        while (choice != "" and choice != "Q" and choice != "q"):
            time.sleep(1)
            choice = input("< Press ENTER to Play Again, input Q to Quit >")
        
        if choice == "q" or choice == "Q":
            break
            
        game.resetBoard()
        
