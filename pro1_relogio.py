import tkinter as tk
from tkinter import *
import os
from time import strftime

#front 
root = tk.Tk()
root.title("Watch")
root.geometry("750x400")
root.maxsize(750, 400)
root.minsize(750, 400)
root.configure(background='#000000')
#

def get_hi():
    user_name = os.getlogin()
    hi.config(text="Olá, " + user_name)
    
def get_date():
    current_date = strftime("%a, %d, %b, %Y")
    date.config(text=current_date)
     
def get_time():
    current_time = strftime("%H:%M:%S")
    time.config(text=current_time)
    time.after(1000, get_time)
#    

margin = tk.Canvas(root, width=750, height=100, bg="#000000", bd=0, highlightthickness=0, relief="ridge")
margin.pack()
#

hi = Label(root, bg="#000000", fg="#32CD32", font=("Arial", 19))
hi.pack()

date = Label(root, bg="#000000", fg="#6B8E23", font=("Arial", 17))
date.pack(pady=2)

time = Label(root, bg="#000000", fg="#006400", font=("Arial", 70, "bold"))
time.pack(pady=2)

get_hi()
get_date()
get_time()

root.mainloop()