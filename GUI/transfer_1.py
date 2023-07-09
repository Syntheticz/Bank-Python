from tkinter import *
import subprocess
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import account
from PIL import ImageTk, Image


#Windows specifications
window = Tk()

window.title("Transfer")
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
instruct = Label(window, text="Enter Account Number of Receiver.", font=("Arial", 16), fg='#162F65', bg="#E7E6DD")
instruct.place(x=285, y=180)

#Text Field for Account Number
pin =""

def get_receiver():
    return account.receiver(enterPin.get())
    
    
    
# Function for pressing the button
def press(num):
    global pin
    if len(pin)<9:
        pin += str(num)
        enterPin.set(pin)

# Function that shows error message if PIN is invalid
def error():
    global errorlb
    errorlb = Label(window, text="Invalid Account Number.", font=("Arial", 12), fg='#AC3333', bg="#E7E6DD")
    errorlb.place(x=400, y=280)

# Function to clear contents in text field
def clear():
    global pin
    pin = ""
    enterPin.set("")
    errorlb.config(text="", fg="#E7E6DD")

def next():
    if not get_receiver():
        error()
    else:
            recipient_acc_num = enterPin.get()
            window.destroy()
            current_directory = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(current_directory, "transfer_2.py")
            subprocess.run(["python", script_path, recipient_acc_num]) 

def back():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "trans_menu.py")
    subprocess.run(["python", script_path])

#Text Field
enterPin = StringVar()
entry_font = ("Arial", 14) 
pin_field = Entry(window, textvariable=enterPin, width=20, font=entry_font, state='readonly',
                  justify="center", fg='#162F65')
pin_field.place(x=335, y=225)

#Button Specifications
button_border1 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button1 = Button(button_border1, text=' 1 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(1), height=1, width=7)
button1.pack()
button_border1.place(x=255, y=320)

button_border2 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button2 = Button(button_border2, text=' 2 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white', 
                command=lambda: press(2), height=1, width=7)
button2.pack()
button_border2.place(x=355, y=320)

button_border3 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button3 = Button(button_border3, text=' 3 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(3), height=1, width=7)
button3.pack()
button_border3.place(x=455, y=320)

button_border4 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button4 = Button(button_border4, text=' 4 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(4), height=1, width=7)
button4.pack()
button_border4.place(x=255, y=370)

button_border5 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button5 = Button(button_border5, text=' 5 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(5), height=1, width=7)
button5.pack()
button_border5.place(x=355, y=370)

button_border6 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button6 = Button(button_border6, text=' 6 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white', 
                 command=lambda: press(6), height=1, width=7)
button6.pack()
button_border6.place(x=455, y=370)

button_border7 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button7 = Button(button_border7, text=' 7 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(7), height=1, width=7)
button7.pack()
button_border7.place(x=255, y=420)

button_border8 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button8 = Button(button_border8, text=' 8 ',  fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(8), height=1, width=7)
button8.pack()
button_border8.place(x=355, y=420)

button_border9 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button9 = Button(button_border9, text=' 9 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(9), height=1, width=7)
button9.pack()
button_border9.place(x=455, y=420)

button_border0 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button0 = Button(button_border0, text=' 0 ',  fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(0), height=1, width=7)
button0.pack()
button_border0.place(x=355, y=470)

cancel_border = Frame(window, highlightbackground = "#651616", highlightthickness = 2, bd=0)
cancel = Button(cancel_border, text='CANCEL', fg='white', bg='#AC3333', font='bold',
                command=back, height=1, width=7)
cancel.pack()
cancel_border.place(x=555, y=320)

clear_border = Frame(window, highlightbackground = "#E8AF30", highlightthickness = 2, bd=0)
clear = Button(clear_border, text='CLEAR', fg='white', bg='#E8C766', font='bold',
                    command=clear, height=1, width=7)
clear.pack()
clear_border.place(x=555, y=370)

ok_border = Frame(window, highlightbackground = "#1C6516", highlightthickness = 2, bd=0)
ok = Button(ok_border, text=' OK ', fg='white', bg='#5AAC33', font='bold',
                    command=lambda: next() if len(pin) == 9 else error(), height=1, width=7)
ok.pack()
ok_border.place(x=555, y=420)

window.mainloop()