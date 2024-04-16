#!/usr/bin/env python3

import tkinter as tk

from UI.sudoku_app import SudokuApp


def main():
    new_puzzle = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
    root = tk.Tk()
    root.geometry("500x500")
    SudokuApp(root, new_puzzle)

    root.mainloop()


if __name__ == "__main__":
    main()
