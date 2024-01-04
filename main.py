""" import libraries """
import tkinter as tk
from ui import TextEditorUI


def main():
    """Main program entry point."""
    window = tk.Tk()
    text_editor_ui = TextEditorUI(window)
    window.mainloop()


if __name__ == "__main__":
    main()
