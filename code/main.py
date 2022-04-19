from cgitb import text
from email.mime import application
from tkinter import *
from tkinter import ttk
from datetime import *
from datetime import datetime, timedelta
import random
from tkinter.font import Font
import hotelDatabase

class Hotel:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Database Management System")
        self.root.geometry("1350x800+0+0")

        MainFrame = Frame(self.root)
        MainFrame.grid()

        # Design code, this is meant for the boxes within the program.

        TopFrame = Frame(MainFrame, bd=10, width=1350, height=550, padx=2, relief=RIDGE)
        TopFrame.pack(side=TOP)

        LeftFrame = Frame(MainFrame, bd=5, width=400, height=550, relief=RIDGE)
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(MainFrame, bd=5, width=400, height=550, relief=RIDGE)
        RightFrame.pack(side=RIGHT)

        BottomFrame = Frame(MainFrame, bd=10, width=1350, height=150, padx=2, relief=RIDGE)
        BottomFrame.pack(side=BOTTOM)


        RightFrame1 = Frame(MainFrame, bd=5, width=800, height=550, padx=10, relief=RIDGE)
        RightFrame1.grid(row=0, column=0)

        RightFrame2 = Frame(MainFrame, bd=5, width=800, height=550, padx=3, relief=RIDGE)
        RightFrame2.grid(row=1, column=0)

        RightFrame3 = Frame(MainFrame, bd=5, width=800, height=550, padx=4, relief=RIDGE)
        RightFrame3.grid(row=3, column=3)

        # Widgets for the program.

        self.lblCustomerID = Label(LeftFrame, Font('Arial', 12, 'bold'), text="Customer ID:", padx=1)
        self.lblCustomerID.grid(row=0, column=0, sticky=W)

        self.txtCustomerID = Label(LeftFrame, Font('Arial', 12, 'bold'), width=18)
        self.txtCustomerID.grid(row=0, column=1, padx=20, pady=3)


        if __name__ == '__main__':
            root = Tk()
            application = Hotel (root)
            root.mainloop

        pass

