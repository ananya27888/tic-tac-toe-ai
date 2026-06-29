import tkinter as tk
from tkinter import messagebox
from ai import MinimaxAI

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI")
        self.root.geometry("420x580")
        self.root.configure(bg="#2C3E50")
        self.root.resizable(False, False)

        # Player configurations
        self.human_player = "X"
        self.ai_player = "O"
        self.current_player = self.human_player
        self.board = [""] * 9
        
        # Scoreboard
        self.score_human = 0
        self.score_ai = 0
        self.score_draw = 0
        
        # Initialize AI
        self.ai = MinimaxAI(self.ai_player, self.human_player)
        self.game_active = True

        self.setup_ui()

    def setup_ui(self):
        """Sets up the graphical user interface components."""
        # Title
        title_label = tk.Label(self.root, text="Tic-Tac-Toe", font=("Segoe UI", 28, "bold"), bg="#2C3E50", fg="#ECF0F1")
        title_label.pack(pady=15)

        # Scoreboard Display
        score_frame = tk.Frame(self.root, bg="#2C3E50")
        score_frame.pack(pady=5)

        self.score_label = tk.Label(score_frame, text=self.get_score_text(), font=("Segoe UI", 12), bg="#2C3E50", fg="#BDC3C7")
        self.score_label.pack()

        # Turn Indicator
        self.turn_label = tk.Label(self.root, text="Your Turn (X)", font=("Segoe UI", 16, "bold"), bg="#2C3E50", fg="#F1C40F")
        self.turn_label.pack(pady=10)

        # Game Board
        board_frame = tk.Frame(self.root, bg="#34495E", bd=5, relief=tk.RIDGE)
        board_frame.pack(pady=10)

        self.buttons = []
        for i in range(9):
            btn = tk.Button(board_frame, text="", font=("Helvetica", 28, "bold"), width=4, height=2,
                            bg="#ECF0F1", activebackground="#BDC3C7", relief=tk.FLAT,
                            command=lambda idx=i: self.on_button_click(idx))
            row = i // 3
            col = i % 3
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(btn)

        # Restart Button
        restart_btn = tk.Button(self.root, text="Restart Game", font=("Segoe UI", 14, "bold"), bg="#E74C3C", fg="white",
                                activebackground="#C0392B", activeforeground="white", relief=tk.FLAT,
                                width=15, command=self.reset_board)
        restart_btn.pack(pady=15)

    def get_score_text(self):
        return f"Human (X): {self.score_human}  |  Draws: {self.score_draw}  |  AI (O): {self.score_ai}"

    def update_score_display(self):
        self.score_label.config(text=self.get_score_text())

    def on_button_click(self, idx):
        """Handles user clicks on the game board."""
        if self.board[idx] == "" and self.game_active and self.current_player == self.human_player:
            self.make_move(idx, self.human_player)
            if self.game_active:
                self.current_player = self.ai_player
                self.turn_label.config(text="AI is thinking...", fg="#E74C3C")
                self.root.update()
                # Brief delay to make the AI feel more natural
                self.root.after(400, self.ai_move)

    def ai_move(self):
        """Executes the AI's move."""
        if not self.game_active:
            return
            
        best_move = self.ai.get_best_move(self.board)
        if best_move is not None:
            self.make_move(best_move, self.ai_player)
            if self.game_active:
                self.current_player = self.human_player
                self.turn_label.config(text="Your Turn (X)", fg="#F1C40F")

    def make_move(self, idx, player):
        """Updates the board state and the UI."""
        self.board[idx] = player
        color = "#2980B9" if player == "X" else "#C0392B"
        self.buttons[idx].config(text=player, fg=color, state=tk.DISABLED, disabledforeground=color)

        # Check for win or draw after every move
        winner = self.ai.check_winner(self.board)
        if winner:
            self.handle_win(winner)
        elif "" not in self.board:
            self.handle_draw()

    def handle_win(self, winner):
        """Handles the game over state when someone wins."""
        self.game_active = False
        if winner == self.human_player:
            self.score_human += 1
            msg = "Congratulations! You won!"
            self.turn_label.config(text="You Won! 🎉", fg="#2ECC71")
        else:
            self.score_ai += 1
            msg = "AI wins! Better luck next time."
            self.turn_label.config(text="AI Won! 🤖", fg="#E74C3C")
            
        self.update_score_display()
        messagebox.showinfo("Game Over", msg)

    def handle_draw(self):
        """Handles the game over state for a draw."""
        self.game_active = False
        self.score_draw += 1
        self.turn_label.config(text="It's a Draw! 🤝", fg="#95A5A6")
        self.update_score_display()
        messagebox.showinfo("Game Over", "It's a draw!")

    def reset_board(self):
        """Resets the game board for a new match."""
        self.board = [""] * 9
        self.current_player = self.human_player
        self.game_active = True
        self.turn_label.config(text="Your Turn (X)", fg="#F1C40F")
        for btn in self.buttons:
            btn.config(text="", state=tk.NORMAL, bg="#ECF0F1")
