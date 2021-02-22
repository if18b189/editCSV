import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import glob


class EntryData:
    def __init__(self):
        print("test")

    def getWeek(self):
        print("week")


def loadCSV():
    csv = filedialog.askopenfile()


if __name__ == '__main__':
    master = tk.Tk()  # creating a tk application+

    master.title('CSVEdit')  # title of the program window

    master.geometry("")  # defining the window size, "" means window will adjust to the widgets

    rowFrame = dict()

    for rowNumber in range(9):  # setting up the grid for the calendar entries
        rowFrame[rowNumber] = tk.Frame(master)
        rowFrame[rowNumber].pack(side='top')

        for columnNumber in range(8):
            if rowNumber == 0:
                Label = tk.Label(rowFrame[rowNumber], text='Hello', bg='white', fg='black', width=10, height=5,
                                 borderwidth=1, relief="solid")
                Label.pack(side="left")
            else:
                Label = tk.Label(rowFrame[rowNumber], text='Hello', bg='blue', fg='white', width=10, height=5,
                                 borderwidth=1, relief="solid")
                Label.pack(side="left")

    loadCSVButton = tk.Button(master, text='Load CSV', width=15, height=2, command=loadCSV)
    loadCSVButton.pack(side="bottom", padx=10, pady=10)

    master.mainloop()
