# Programmer: Mai Lillie
# Date: 11/15/24
# Program #1 Saying Window

import tkinter

# Creates a Window
class SayingGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("My Favorite Saying")
        self.label = tkinter.Label(self.main_window, text="Memento Vivere: Remember to live.")
        self.label.pack()
        tkinter.mainloop()

# Runs the program
if __name__ == '__main__':
    saying_gui = SayingGUI()
