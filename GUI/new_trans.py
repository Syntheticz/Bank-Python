from tkinter import *
import subprocess
import os
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

# Function to go to Transaction Menu
def next():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "trans_menu.py")
    subprocess.run(["python", script_path]) 

def cancel_click():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "remove.py")
    subprocess.run(["python", script_path])



# Logo
image = Image.open("C:/Users/simon/OneDrive/Desktop/school/progs/Second Year/Python/BankSystem/new.png")
photo_label = Label(window, bg="#E7E6DD")
photo = ImageTk.PhotoImage(image)
photo_label.config(image=photo)
photo_label.place(x=350, y=20)



# Insert Instructions for User
goBack = Label(window, text="Do you want to make another transaction?", font=("Arial", 16), fg='#162F65', bg="#E7E6DD")
goBack.place(x=260, y=250)

exit_border = Frame(window, highlightbackground = "#651616", highlightthickness = 2, bd=0)
exit = Button(exit_border, text='EXIT', fg='white', bg='#AC3333', font='bold',
              command=lambda: cancel_click() ,height=1, width=7)
exit.pack()
exit_border.place(x=305, y=300)

ok_border = Frame(window, highlightbackground = "#1C6516", highlightthickness = 2, bd=0)
ok = Button(ok_border, text=' OK ', fg='white', bg='#5AAC33', font='bold',
                    command=lambda: next(), height=1, width=7)
ok.pack()
ok_border.place(x=505, y=300)

window.mainloop()