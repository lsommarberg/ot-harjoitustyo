#!/usr/bin/env python3

import tkinter as tk

from UI.sudoku_app import SudokuApp


def main():
    root = tk.Tk()

    SudokuApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()
