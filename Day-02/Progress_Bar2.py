import tkinter as tk
from tkinter import ttk
import time


class progress_bar(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)                                                       # initialize the App
        self.winfo_toplevel().title("Progress Bar")                                                 # Set a title
        self.progress = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")  # Create my progress bar
        self.progress.pack()                                                                        # Pack geometry manager
        self.val = 0                                                                                # Initialize value 0%
        self.maxval = 1                                                                             # Initialize Max Value 100%
        self.progress["maximum"] = 1                                                                # Set Max to 1 (100%)

    def updating(self, val):                                                                        # Every time we iterate, call app.updating function
        self.val = val                                                                              # Set the current iterator value to variable self.val
        self.progress["value"] = self.val                                                           # Update Progress bar
        if self.val == self.maxval:                                                                 # if self.val variable is not 1 (100%) continue, else we finish task
            self.destroy()


def test(i=0):                                                                                      # This will be our iterator
    app.updating(i/100)                                                                             # will be iterating with float numbers 0.0, 0.01, 0.02, ,,,, , 1
    if i < 100:
        app.after(100, test, i+1)                                                                   # if its not 100, increment i and call test function again

app = progress_bar()
app.after(1, test)
app.mainloop()
