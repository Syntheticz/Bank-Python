from tkinter import *
import subprocess
import os
from PIL import ImageTk, Image


#Windows specifications
window = Tk()

window.title("Transaction Menu")
window.configure(background = "#E7E6DD")
window.resizable(False, False)

window_height = 600
window_width = 900

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry("{}x{}+{}+{}".format(window_width, window_height, 318, 100))


# Logo
image = Image.open("C:/Users/simon/OneDrive/Desktop/school/progs/Second Year/Python/BankSystem/new.png")
photo_label = Label(window, bg="#E7E6DD")
photo = ImageTk.PhotoImage(image)
photo_label.config(image=photo)
photo_label.place(x=350, y=20)

# Instructions for user
instruct = Label(window, text="Please select transaction.", font=("Arial", 16), fg='#162F65', bg="#E7E6DD")
instruct.place(x=330, y=180)

def nxtWithdraw():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "withdraw.py")
    subprocess.run(["python", script_path]) 

def nxtDeposit():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "deposit.py")
    subprocess.run(["python", script_path]) 

def nxtTransfer():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "transfer_1.py")
    subprocess.run(["python", script_path]) 

def nxtBalInq():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "bal_inq.py")
    subprocess.run(["python", script_path]) 

# Buttons Specifications
withdraw_border = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
withdraw = Button(withdraw_border, text=' WITHDRAW ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command= lambda:nxtWithdraw(), height=1, width=len(' BALANCE INQUIRY '))
withdraw.pack()
withdraw_border.place(x=350, y=250)

deposit_border = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
deposit = Button(deposit_border, text=' DEPOSIT ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command= lambda:nxtDeposit(), height=1, width=len(' BALANCE INQUIRY '))
deposit.pack()
deposit_border.place(x=350, y=305)

transfer_border = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
transfer = Button(transfer_border, text=' TRANSFER ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command= lambda:nxtTransfer(), height=1, width=len(' BALANCE INQUIRY '))
transfer.pack()
transfer_border.place(x=350, y=360)

balinq_border = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
balinq = Button(balinq_border, text=' BALANCE INQUIRY ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command= lambda:nxtBalInq(), height=1, width=len(' BALANCE INQUIRY '))
balinq.pack()
balinq_border.place(x=350, y=415)



window.mainloop()