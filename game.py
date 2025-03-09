import tkinter as tk
import random
import time  # For animations
import threading # For non-blocking animations

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")

        # Theme Colors
        self.bg_color = "#282c34"  # Dark background
        self.fg_color = "#abb2bf"  # Lighter text color
        self.button_bg = "#61afef"  # Blueish button
        self.button_fg = "#282c34"  # Button text
        self.win_color = "#98c379"   # Green for winning
        self.lose_color = "#e06c75"  # Red for losing

        master.configure(bg=self.bg_color)

        self.secret_number = random.randint(1, 100)
        self.guesses_left = 7

        self.label = tk.Label(master, text="I'm thinking of a number between 1 and 100.", bg=self.bg_color, fg=self.fg_color)
        self.label.pack(pady=10)  # Added padding

        self.instruction_label = tk.Label(master, text="You have 7 guesses.", bg=self.bg_color, fg=self.fg_color)
        self.instruction_label.pack(pady=5)

        self.guess_label = tk.Label(master, text="Enter your guess:", bg=self.bg_color, fg=self.fg_color)
        self.guess_label.pack(pady=5)

        self.guess_entry = tk.Entry(master, bg="#3e4451", fg=self.fg_color, insertbackground=self.fg_color)
        self.guess_entry.pack(pady=5)

        self.guess_button = tk.Button(master, text="Guess", command=self.guess, bg=self.button_bg, fg=self.button_fg, relief=tk.RAISED, borderwidth=2) #Added styling
        self.guess_button.pack(pady=10)
        self.guess_button.bind("<Enter>", self.on_button_hover)
        self.guess_button.bind("<Leave>", self.on_button_leave)

        self.feedback_label = tk.Label(master, text="", bg=self.bg_color, fg=self.fg_color)
        self.feedback_label.pack(pady=5)

        self.guesses_remaining_label = tk.Label(master, text=f"Guesses remaining: {self.guesses_left}", bg=self.bg_color, fg=self.fg_color)
        self.guesses_remaining_label.pack(pady=5)

        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game, bg=self.button_bg, fg=self.button_fg, relief=tk.RAISED, borderwidth=2) #Added styling
        self.play_again_button.pack(pady=10)
        self.play_again_button.bind("<Enter>", self.on_button_hover)
        self.play_again_button.bind("<Leave>", self.on_button_leave)
        self.play_again_button.pack_forget()  # Initially hide the play again button

    def on_button_hover(self, event):
        event.widget.config(relief=tk.SUNKEN) # Change style on hover

    def on_button_leave(self, event):
        event.widget.config(relief=tk.RAISED)

    def guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.feedback_label.config(text="Invalid input. Please enter a number.", fg=self.lose_color) #Use lose color for error
            self.shake_window()
            return

        if guess < 1 or guess > 100:
            self.feedback_label.config(text="Please enter a number between 1 and 100.", fg=self.lose_color) #Use lose color for error
            self.shake_window()
            return

        self.guesses_left -= 1
        self.guesses_remaining_label.config(text=f"Guesses remaining: {self.guesses_left}")

        if guess == self.secret_number:
            self.feedback_label.config(text=f"Congratulations! You guessed the number in {7 - self.guesses_left} guesses.", fg=self.win_color) #Use win color
            self.guess_button.config(state=tk.DISABLED)
            self.guess_entry.config(state=tk.DISABLED)
            self.play_again_button.pack()
            self.pulse_text(self.feedback_label, self.win_color) # Animate winning message
        elif guess < self.secret_number:
            self.feedback_label.config(text="Too low!", fg=self.fg_color)
        else:
            self.feedback_label.config(text="Too high!", fg=self.fg_color)

        if self.guesses_left == 0:
            self.feedback_label.config(text=f"You ran out of guesses. The number was {self.secret_number}.", fg=self.lose_color) #Use lose color
            self.guess_button.config(state=tk.DISABLED)
            self.guess_entry.config(state=tk.DISABLED)
            self.play_again_button.pack()
            self.flash_background(self.master, self.lose_color) #Flash background when losing.

        self.guess_entry.delete(0, tk.END)

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.guesses_left = 7
        self.feedback_label.config(text="", fg=self.fg_color) # Reset to default color
        self.guesses_remaining_label.config(text=f"Guesses remaining: {self.guesses_left}")
        self.guess_button.config(state=tk.NORMAL)
        self.guess_entry.config(state=tk.NORMAL)
        self.play_again_button.pack_forget()
        self.guess_entry.delete(0, tk.END)
        self.master.configure(bg=self.bg_color) # Reset background color



    def shake_window(self):
        x_offset = 5
        for i in range(10): #Shake ten times.
            if i % 2 == 0:
                self.master.geometry(f"+{self.master.winfo_x() + x_offset}+{self.master.winfo_y()}")
            else:
                self.master.geometry(f"+{self.master.winfo_x() - x_offset}+{self.master.winfo_y()}")
            self.master.update()
            time.sleep(0.02)  # Small delay for the animation

    def pulse_text(self, label, color):
        def animate(i=0):
            if not label.winfo_exists(): #Stop if window is closed
                return
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)

            #Adjust brightness (sin wave)
            brightness = int(127 * (1 + math.sin(i / 5)))
            r = min(255, r + brightness)
            g = min(255, g + brightness)
            b = min(255, b + brightness)

            hex_color = '#%02x%02x%02x' % (r, g, b)
            label.config(fg=hex_color)
            label.after(20, lambda: animate(i + 1))

        import math #Import here so it's only imported when the function runs.
        animate()

    def flash_background(self, window, color):
        def flash(i=0):
            if not window.winfo_exists(): #Stop if window is closed.
                return
            if i % 2 == 0:
                window.config(bg=color)
            else:
                window.config(bg=self.bg_color)  # Back to original
            window.after(300, lambda: flash(i + 1)) # Flash every 300 ms

        flash()


root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()