import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import glob


def loadCSV():
    csv = filedialog.askopenfile()




if __name__ == '__main__':
    master = tk.Tk()  # creating a tk application+

    master.title('CSVEdit')  # title of the program window

    master.geometry("")  # defining the window size

    for x in range(7):



    loadCSVButton = tk.Button(master, text='Load CSV', width=15, height=2, command=loadCSV)
    loadCSVButton.pack(side="left", padx=10, pady=10)

    master.mainloop()