# Programmer: Mai Lillie
# Date: 11/15/24
# Program #1 Name and Address Window

import tkinter
import tkinter.messagebox

# Creates a window and two buttons
class NameGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Nice to meet you!")

        # Adds the show info button
        self.info_button = tkinter.Button(self.main_window, text="Show Info", command=self.show_info)
        self.info_button.pack()

        # Adds the quit button
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)
        self.quit_button.pack()
        tkinter.mainloop()

    # Adds a function to the info button
    def show_info(self):
        tkinter.messagebox.showinfo("Personal Info", "Name: Mai Lillie \nAddress: 3677 White Pine Way")

# Runs the program
if __name__ == '__main__':
    name_gui = NameGUI()
