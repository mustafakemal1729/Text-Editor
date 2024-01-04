import tkinter as tk
from ui import TextEditorUI

def main():
    window = tk.Tk()
    text_editor_ui = TextEditorUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()
