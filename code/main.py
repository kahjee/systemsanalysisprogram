from email.mime import application
from tkinter import *
from datetime import *
import random

class Hotel:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="white")

    if __name__ == '__main__':
        root = Tk()
        application = Hotel (root)
        root.mainloop()
