import tkinter as tk
import random
import time
import os

class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")

        self.text_list = self.get_text_list()
        self.text_to_type = random.choice(self.text_list)
        self.current_text = tk.StringVar()
        self.current_text.set(self.text_to_type)

        self.label = tk.Label(root, textvariable=self.current_text, font=("Arial", 12))
        self.label.pack(pady=10)

        self.input_entry = tk.Entry(root, font=("Arial", 12))
        self.input_entry.pack(pady=10)
        self.input_entry.bind("<KeyRelease>", self.check_typing)

        self.start_time = None
        self.end_time = None

        self.result_label = tk.Label(root, text="", font=("Arial", 14))

    def get_text_list(self):
        return [
            "The quick brown fox jumps over the lazy dog.",
            "Python is a powerful and versatile programming language.",
            "Practice makes perfect.",
            "Coding is fun and challenging.",
            "Type your way to success.",
        ]

    def check_typing(self, event):
        if not self.start_time:
            self.start_time = time.time()

        typed_text = self.input_entry.get()
        if typed_text == self.text_to_type:
            self.end_time = time.time()
            self.show_result()

    def show_result(self):
        if self.start_time and self.end_time:
            elapsed_time = self.end_time - self.start_time
            words = len(self.text_to_type.split())
            wpm = int(words / (elapsed_time / 60))
            result_text = f"Your Typing Speed: {wpm} WPM"

            self.result_label.config(text=result_text)
            self.input_entry.config(state=tk.DISABLED)

            # Center the result label on the screen
            self.label.pack_forget()  # Remove from its current position
            self.result_label.pack(side=tk.TOP, anchor=tk.CENTER, pady=50)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()
