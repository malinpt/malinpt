from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
root.geometry("400x240")

textExample=tk.Text(root, height=10)
textExample.pack()

fontExample = tkFont.Font(family='Comic Sans MS', size=16, weight="bold",)

textExample.configure(font=fontExample)

root.mainloop()