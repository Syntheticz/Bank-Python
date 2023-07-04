from tkinter import *
import subprocess
import os
from PIL import ImageTk, Image


#Windows specifications
window = Tk()

window.title("Balance Inquiry")
window.configure(background = "#E7E6DD")
window.resizable(False, False)

window_height = 600
window_width = 900

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry("{}x{}+{}+{}".format(window_width, window_height, 318, 100))

# Function to go to Transaction Menu
def next():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "loading_2.py")
    subprocess.run(["python", script_path]) 

def no_click():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "remove.py")
    subprocess.run(["python", script_path]) 

# Current Balance
bal = Label(window, text=("₱ " + "30000"), font=("Arial", 20), fg='#162F65', bg="#E7E6DD")
bal.grid(row=0, column=0, sticky="nsew")
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

# Insert Instructions for User
instruct = Label(window, text="Current Balance:", font=("Arial", 16), fg='#162F65', bg="#E7E6DD")
instruct.place(x=373, y=180)

# Insert Instructions for User
goBack = Label(window, text="Do you want a printed receipt?", font=("Arial", 16), fg='#162F65', bg="#E7E6DD")
goBack.place(x=310, y=390)

exit_border = Frame(window, highlightbackground = "#651616", highlightthickness = 2, bd=0)
exit = Button(exit_border, text='EXIT', fg='white', bg='#AC3333', font='bold',
              command=lambda: no_click(), height=1, width=7)
exit.pack()
exit_border.place(x=305, y=440)

ok_border = Frame(window, highlightbackground = "#1C6516", highlightthickness = 2, bd=0)
ok = Button(ok_border, text=' OK ', fg='white', bg='#5AAC33', font='bold',
                    command=lambda: next(), height=1, width=7)
ok.pack()
ok_border.place(x=505, y=440)

window.mainloop()