import tkinter as tk
from tkinter import messagebox

def showErrorAlert(title:str, subtitle:str):
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning(title, subtitle)