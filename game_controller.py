import tkinter as tk
from itertools import cycle
from tkinter import font
from game_settings import BOARD_SIZE, DEFAULT_PLAYERS
from move import Move

"""
Every player’s move will trigger a bunch of operations on the TicTacToeGame class. These operations include:

Validating the move
Checking for a winner
Checking for a tied game
Toggling the player for the next move

"""

class GameController:

    def __init__(self):
                 
        self._players = cycle(DEFAULT_PLAYERS)         # Cyclical iterator over the input tuple
        self.board_size = BOARD_SIZE                  # Define the bord size
        self.current_player = next(self._players)      # Toggle the current player
        self.winner_combo = []                        # Combination of cells that defines a winner
        self._current_moves = []                      # The list of players’ moves in a given game
        self._has_winner = False                      # Determine if the game has a winner or not
        self._winning_combos = []                     # A list containing the cell combinations that define a win
        self._setup_board()



    def _get_winning_combos(self):
        rows = []
        # store the winning combination over the rows
        #[[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)]]
        for row in self._current_moves:
            rows.append([(move.row, move.col) for move in row])

        # store the winning combination over columns
        # [[(0, 0), (1, 0), (2, 0)],[(0, 1), (1, 1), (2, 1)],[(0, 2), (1, 2), (2, 2)]]
        columns = [list(col) for col in zip(*rows)]

        # store the winning combination over the first diagnol
        first_diagonal = [row[i] for i,row in enumerate(rows)]
        # [(0,0),(1,1),(2,2)]
        second_diagonal = [col[j] for j,col in enumerate(reversed(columns))]
        # [(0,2),(1,1),(2,0)]
        return rows + columns + [first_diagonal , second_diagonal]


    def _setup_board(self):
        '''
        This function setups the game all possible moves and winning combination
        '''
        for row in range(self.board_size):
            self._current_moves.append([Move(row, col) for col in range(self.board_size)])
        
        # stores the winning combos
        self._winning_combos = self._get_winning_combos()
        #[
        # [(0, 0), (0, 1), (0, 2)],
        # [(1, 0), (1, 1), (1, 2)],
        # [(2, 0), (2, 1), (2, 2)],
        # [(0, 0), (1, 0), (2, 0)],
        # [(0, 1), (1, 1), (2, 1)],
        # [(0, 2), (1, 2), (2, 2)],
        # [(0, 0), (1, 1), (2, 2)],
        # [(0, 2), (1, 1), (2, 0)],
        # ]

    
    def is_valid_move(self,move):
        '''
        This function checks is the passed requested move is valid or not,
        keywords arguments :
        move : a move object to be validated
        return True if the move is valid, False otherwise
        '''
        row, col = move.row, move.col
        return self._current_moves[row][col].label == None and not self._has_winner
    

    def process_move(self,move):
        '''
        Process the last move and check for aa winner
        keywords arguments :
        move : the last made move
        '''
        # retrieve the move coordinates
        row, col = move.row, move.col
        # store the move 
        self._current_moves[row][col] = move
        #
        for combo in self._winning_combos:
            results = set(self._current_moves[n][m].label for n,m in combo)
            if (len(results) == 1) and (None not in results):
                self._has_winner = True
                self.winner_combo = combo
                break
        
    def is_tied(self):
        '''
        Return True if the game is tied, False otherwise
        '''
        played_moves = (
            move.label for row in self._current_moves for move in row
        )
        return (not self._has_winner) and all(played_moves)
    

    def toggle_player(self):
        '''
        This function switch the current player
        '''
        self.current_player = next(self._players)

    
    def has_winner(self):
        return self._has_winner

                
            

