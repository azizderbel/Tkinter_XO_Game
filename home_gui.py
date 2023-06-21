import tkinter as tk
import game_settings as gs
from PIL import Image,ImageTk


class HomeGui(tk.Tk):

    def __init__(self):

        super().__init__()

        screen_width = self.winfo_screenwidth()  # Width of the screen
        screen_height = self.winfo_screenheight()

        # Calculate Starting X and Y coordinates for Window
        self.x = (screen_width/2) - (gs.home_window_width/2)
        self.y = (screen_height/2) - (gs.home_window_height/2)
        self.width = gs.home_window_width
        self.height = gs.home_window_height

        # Specify window dimensions
        self.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")

        # Set the window title
        self.title("Welcome to tic-tac-toe game")

        # set window backgound
        bg = tk.PhotoImage(file ="backg.png")
        # Show image using label
        label = tk.Label(self, image = bg)
        label.place(x=0,y=0)
        label.img = bg

        """canvas = tk.Canvas(master=self,
                           width=gs.home_window_width,
                           height=gs.home_window_height
                           )
        
        canvas.grid(columnspan=3)"""