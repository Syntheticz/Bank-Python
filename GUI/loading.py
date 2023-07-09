from tkinter import *
from tkinter.ttk import Progressbar
import time
import subprocess
import os
import sys
from PIL import ImageTk, Image





#Windows specifications
window = Tk()

window.title("  ")
window.configure(background = "#E7E6DD")
window.resizable(False, False)

window_height = 600
window_width = 900

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry("{}x{}+{}+{}".format(window_width, window_height, 318, 100))

# Logo

script_dir = os.path.dirname(os.path.abspath('GUI/new.png'))
image_path = os.path.join(script_dir, 'new.png')
image = Image.open(image_path)

photo_label = Label(window, bg="#E7E6DD")
photo = ImageTk.PhotoImage(image)
photo_label.config(image=photo)
photo_label.place(x=350, y=20)

# Insert Instructions for User
instruct = Label(window, text="Loading Transaction...", font=("Arial", 16), fg='#162F65', bg="#E7E6DD")
instruct.place(x=356, y=230)

def next():

    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "accSuccess.py")
    subprocess.run(["python", script_path]) 

def start_loading():
    progress['value'] = 0
    progress.start(30)
    progress.after(3100, stop)

def stop():
    progress.stop()
    next()
    


progress = Progressbar(window, orient=HORIZONTAL, length = 300, mode='determinate')
progress.place(x= 310, y=280)
window.after(0, start_loading)




window.mainloop()