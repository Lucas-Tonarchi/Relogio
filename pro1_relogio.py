import tkinter as tk
from tkinter import *
import os
from time import strftime

#frt 
root = tk.Tk()
root.title("Watch")
root.geometry("750x400")
root.maxsize(750, 400)
root.minsize(750, 400)
root.configure(background='#000000')
#

def get_hi():
    user_name = os.getlogin()
    hi.config(text="Hello, " + user_name)
    
def get_dt():
    crrt_dt = strftime("%a, %d, %b, %Y")
    dt.config(text=crrt_dt)
    
def get_tm():
    crrt_tm = strftime("%H:%M:%S")
    tm.config(text=crrt_tm)
    tm.after(1000, get_tm)
#    

mrgn = tk.Canvas(root, width=750, height=100, bg="#000000", bd=0, highlightthickness=0, relief="ridge")
mrgn.pack()
#

hi = Label(root, bg="#000000", fg="#32CD32", font=("Arial", 19))
hi.pack()

dt = Label(root, bg="#000000", fg="#6B8E23", font=("Arial", 17))
dt.pack(pady=2)

tm = Label(root, bg="#000000", fg="#006400", font=("Arial", 70, "bold"))
tm.pack(pady=2)

get_hi()
get_dt()
get_tm()

root.mainloop()