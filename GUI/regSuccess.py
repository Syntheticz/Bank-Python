from tkinter import *
import subprocess
import os
from PIL import ImageTk, Image
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import filehandling
from account import current_user


#Windows specifications
window = Tk()

window.title("Account is Registered!")
window.configure(background = "#E7E6DD")
window.resizable(False, False)

window_height = 600
window_width = 900

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry("{}x{}+{}+{}".format(window_width, window_height, 318, 100))


card_path = f"{filehandling.get_card_path()}\\record.txt"

acc = filehandling.get_account_from_card(card_path)
key = filehandling.get_key(card_path)
filehandling.decrypt_account(acc, key)

name = acc.name
accNum = acc.account_number
currBal = str(acc.account_balance)

def next():
    filehandling.saveUserLogin(current_user.account_number)
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "trans_menu.py")
    subprocess.run(["python", script_path]) 

def hide_accNum():
    global accNum 
    accNum = "******" + accNum[6:]

hide_accNum()

goBack = Label(window, text="Account Registration Successful!", font=("Arial", 16, 'bold'), fg='#162F65', bg="#E7E6DD")
goBack.place(x=290, y=200)

mid = Frame(window, highlightbackground = "#651616", bd=0)
mid.place(x=330, y=280)

namelb = Label(mid, text=("Name: " + name), font=("Arial", 15), fg='#162F65', bg="#E7E6DD")
namelb.grid(row=0, column=0, sticky="nsew")

accNumlb = Label(mid, text=("Account Number: " + str(accNum)), font=("Arial", 15), fg='#162F65', bg="#E7E6DD")
accNumlb.grid(row=1, column=0, sticky="nsew")

ballb = Label(mid, text=("Current Balance: " + currBal + ""), font=("Arial", 15), fg='#162F65', bg="#E7E6DD")
ballb.grid(row=2, column=0, sticky="nsew")

mid.grid_rowconfigure(0, weight=1)
mid.grid_rowconfigure(1, weight=0)
mid.grid_rowconfigure(2, weight=0)
mid.grid_columnconfigure(0, weight=1)

ok_border = Frame(window, highlightbackground = "#1C6516", highlightthickness = 2, bd=0)
ok = Button(ok_border, text=' OK ', fg='white', bg='#5AAC33', font='bold',
                    command=lambda: next(), height=1, width=7)
ok.pack()
ok_border.place(x=410, y=440)



# Logo
script_dir = os.path.dirname(os.path.abspath('GUI/new.png'))
image_path = os.path.join(script_dir, 'new.png')
image = Image.open(image_path)
photo_label = Label(window, bg="#E7E6DD")
photo = ImageTk.PhotoImage(image)
photo_label.config(image=photo)
photo_label.place(x=350, y=20)


window.mainloop()

