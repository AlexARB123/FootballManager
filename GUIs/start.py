from tkinter import *


## Creating the start menu window
root = Tk()
root.title("Football Manager")
root.configure(background="white")
root.minsize(700, 700)  # width, height
root.maxsize(1080, 720)
root.geometry("1080x720+50+50")  # width x height + x + y


label = Label(root, text = "Football Manager")

root.mainloop()