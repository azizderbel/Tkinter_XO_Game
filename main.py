import tkinter as tk
from board_gui import BoardGui
from home_gui import HomeGui
from game_controller import GameController

def start_game():
    # kick off the game
    game = GameController()
    # Create the game GUI interface
    board = BoardGui("XO game",game=game)
    board.resizable(height = False, width = False)
    board.create_borad_container(text="Ready?")
    board.create_board_grid()

def main():

    home_window = HomeGui()
    home_window.resizable(height = False, width = False)
    start_button = tk.Button(
        master = home_window,
        text = 'Play',
        bg='red',
        command = start_game
    )
    start_button.place(
        width=50,
        height=40,
        x= (home_window.width // 2) - 18,
        y= (home_window.height // 2) + 40
    )

    home_window.mainloop()

if __name__ == "__main__":
    main()