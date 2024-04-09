import tkinter as tk


class ButtonPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.notes_button = tk.Button(self, text="Notes", width=15)
        self.notes_button.grid(row=0, column=0, padx=5)


class SudokuEntry(tk.Entry):
    def __init__(self, parent):
        super().__init__(parent, width=5)
