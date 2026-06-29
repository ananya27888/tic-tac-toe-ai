import tkinter as tk
from game import TicTacToeGame

def main():
    """
    Main entry point for the Tic-Tac-Toe application.
    Initializes the Tkinter root window and starts the game.
    """
    root = tk.Tk()
    
    # Initialize the game instance
    app = TicTacToeGame(root)
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
