import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfile
from app import open_file, save_file

class TextEditorUI:
    def __init__(self, window):
        self.window = window
        self.setup_ui()

    def setup_ui(self):
        self.window.title("Modern Text Editor")
        self.window.geometry("600x600")
        self.window.rowconfigure(0, minsize=400)
        self.window.columnconfigure(1, minsize=500)

        self.text_edit = tk.Text(self.window, font="Helvetica 18")
        self.text_edit.grid(row=0, column=1)

        frame = tk.Frame(self.window, relief=tk.RAISED, bd=2)
        save_button = tk.Button(
            frame, text="Save", command=lambda: save_file(self.window, self.text_edit)
        )
        open_button = tk.Button(
            frame, text="Open", command=lambda: open_file(self.window, self.text_edit)
        )
        save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        open_button.grid(row=1, column=0, padx=5, sticky="ew")
        frame.grid(row=0, column=0, sticky="ns")

        self.window.bind("<Control-s>", lambda x: save_file(self.window, self.text_edit))
