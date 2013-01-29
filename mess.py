from tkinter import *

def mss(frame):
    msg = Message(text=frame)
    msg.config(bg='pink', font=('times', 16, 'italic'))
    msg.pack()
    mainloop()
