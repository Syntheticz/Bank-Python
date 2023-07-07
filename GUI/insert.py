from tkinter import *
import os
import sys
from PIL import ImageTk, Image
import threading
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from filehandling import initial_card_check

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

removelb = Label(window, text=("Please insert flash drive."), font=("Arial", 20), fg='#162F65', bg="#E7E6DD")
removelb.grid(row=0, column=0, sticky="nsew")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Logo
script_dir = os.path.dirname(os.path.abspath('GUI/new.png'))
image_path = os.path.join(script_dir, 'new.png')
image = Image.open(image_path)
photo_label = Label(window, bg="#E7E6DD")
photo = ImageTk.PhotoImage(image)
photo_label.config(image=photo)
photo_label.place(x=350, y=20)


def after_init():
    # Actions to perform after the window is initialized
    print("After init")
    # Call the initial_card_check function
    does_exist = False
    # Process the result
    while True:
        result = initial_card_check()
        if result:
            print("test")
            does_exist = True
            break
    
    if does_exist:
        window.quit()
        current_directory = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_directory, "log_in.py")
        subprocess.run(["python", script_path]) 

       

       


thread = threading.Thread(target=after_init)
thread.start()



window.mainloop()


