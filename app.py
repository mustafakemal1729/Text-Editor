from tkinter.filedialog import askopenfilename, asksaveasfile

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    text_edit.delete(1.0, "end")
    with open(filepath, "r") as file:
        content = file.read()
        text_edit.insert("end", content)
    window.title(f"Open file: {filepath}")

def save_file(window, text_edit):
    file = asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

    if not file:
        return

    filepath = file.name
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, "end")
        f.write(content)
    window.title(f"Saved: {filepath}")
