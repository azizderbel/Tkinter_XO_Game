import tkinter as tk
from tkinter import font
from game_settings import BOARD_SIZE
from move import Move


class BoardGui(tk.Toplevel):

    # This class inherits from Tk() class from the tkinter module
    def __init__(self,name,game):

        # initialize the parent class attributes
        super().__init__()

        # Connect the game logic
        self._game = game

        # Initiate the main window title
        self.title(name)

        # Create empty cells
        self._cells = {} #holds an empty dictionary

        # Create empty main container
        self.main_frame = tk.Frame(master=self)
        self.main_frame.pack(fill= tk.X)

        # create empty grid container
        self.grid_frame = tk.Frame(master=self)
        self.grid_frame.pack()

        self.text = None

    def create_borad_container(self,text):
        self.text = tk.Label(
            master = self.main_frame,
            text = text,
            font = font.Font(size=15, weight="bold"),
        )
        self.text.pack()

    def create_board_grid(self):
        for row in range(BOARD_SIZE):
            #self.rowconfigure(row, weight=1, minsize=50)
            #self.columnconfigure(row, weight=1, minsize=75)
            for col in range(BOARD_SIZE):

                # Create a button
                button = tk.Button(
                    master = self.grid_frame,
                    text = "",
                    font = font.Font(size=36, weight="bold"), # text font size and type
                    fg = "black",                             # text color
                    width = 2,                                # width of the button in text lines
                    height = 1,                               # Height of the button in text lines
                )

                # Store the created button as a cell
                self._cells[button] = (row,col)
                # connect the click event to a play function
                button.bind("<ButtonPress-1>", self.play)
                # place the button on the grid
                button.grid(
                    row = row,
                    column = col,
                    padx = 5,
                    pady = 5
                )

    def play(self,event):
        '''
        Handle a player move
        '''
        clicked_btn = event.widget
        # Get the click coordinates
        row, col = self._cells[clicked_btn]
        # Create a Move object
        move = Move(row, col, self._game.current_player.label)
        # 1 - check if the move is valid
        if self._game.is_valid_move(move):
            self._update_button(clicked_btn)
            # Process the request move
            self._game.process_move(move)
            # 2 - check if there is a winner
            if self._game.has_winner():
                msg = f'Player "{self._game.current_player.label}" won!'
                color = self._game.current_player.color
                self._update_display(msg, color)
            # 3 - check if there is a tie
            elif self._game.is_tied():
                self._update_display(msg="Tied game!", color="red")

            else:
                # apply the move and switch player
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg)

    def _update_button(self,clicked_btn):
        '''
        Update the clicked button state using the current player info
        '''
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)


    def _update_display(self, msg, color="black"):
        '''
        Update the interface text
        '''
        self.text["text"] = msg
        self.text["fg"] = color
        
    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")





