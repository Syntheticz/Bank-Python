from tkinter import *
import subprocess
import os
import re
import datetime
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry

#Windows specifications
window = Tk()

window.title("Account Register")
window.configure(background = "#E7E6DD")
window.resizable(False, False)

window_height = 700
window_width = 900

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry("{}x{}+{}+{}".format(window_width, window_height, 318, 30))


# Logo
script_dir = os.path.dirname(os.path.abspath('new.png'))
image_path = os.path.join(script_dir, 'new.png')
image = Image.open(image_path)
photo_label = Label(window, bg="#E7E6DD")
photo = ImageTk.PhotoImage(image)
photo_label.config(image=photo)
photo_label.place(x=350, y=20)

def onlyChar(new_text):
    return re.match("^[a-zA-Z\s]*$", new_text) is not None

def valid_Age(bd):
    global errorlb
    selected_date = bd.get_date()
    today = datetime.date.today()
    age_limit = today.replace(year=today.year - 18)

    if selected_date <= age_limit:
        errorlb.config(text="", fg="#E7E6DD")
    else:
        errorlb = Label(window, text="User should be 18 years old or above.", font=("Arial", 12), fg='#AC3333', bg="#E7E6DD")
        errorlb.place(x=325, y=418)
        

def press(num):
    global pin1, pin2
    if len(pin1)<4:
        pin1 += str(num)
        enterPin.set(pin1)
    elif len(pin1)==4:
        if len(pin2)<4:
            pin2 +=str(num)
            enterPin2.set(pin2)

# Function to clear contents in text field
def clear():
    global pin1, pin2
    pin1 = ""
    enterPin.set("")
    pin2 = ""
    enterPin2.set("")
    errorlb.config(text="", fg="#E7E6DD")   # Clears error message

def cancel_click():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "remove.py")
    subprocess.run(["python", script_path])

def error():
    global errorlb

    if nm_field.get() == '':
        errorlb = Label(window, text="Please enter name.", font=("Arial", 12), fg='#AC3333', bg="#E7E6DD")
        errorlb.place(x=355, y=418)
    elif len(pin2) != 4:
        errorlb = Label(window, text="PIN should be 4 digits.", font=("Arial", 12), fg='#AC3333', bg="#E7E6DD")
        errorlb.place(x=355, y=418)
    elif len(pin1) != 4:
        errorlb = Label(window, text="PIN should be 4 digits.", font=("Arial", 12), fg='#AC3333', bg="#E7E6DD")
        errorlb.place(x=355, y=418)
    elif bd_field.get_date() == datetime.date.today():
        errorlb = Label(window, text="Please enter valid birthdate.", font=("Arial", 12), fg='#AC3333', bg="#E7E6DD")
        errorlb.place(x=340, y=418)
    else:
        next()

def next():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "regSuccess.py")
    subprocess.run(["python", script_path]) 


# Insert Instructions for User
instruct = Label(window, text="Please enter account information.", font=("Arial", 16), fg='#162F65', bg="#E7E6DD")
instruct.place(x=299, y=180)

enterNm = StringVar()
entry_font = ("Arial", 14) 
nm = Label(window, text="Name:", font=("Arial", 16), fg='#162F65', bg="#E7E6DD")
nm.place(x=320, y=245)
isChar = (window.register(onlyChar), '%P')
nm_field = Entry(window, textvariable=enterNm, width=20, font=entry_font, fg='#162F65',
                 validate="key", validatecommand=(isChar))
nm_field.place(x=400, y=245)

enterBd = StringVar()
bd = Label(window, text="Birthdate:", font=("Arial", 16), fg='#162F65', bg="#E7E6DD")
bd.place(x=290, y=290)
bd_field = DateEntry(window, width=34, background='#162F65', foreground='#E7E6DD', date_pattern="yyyy/mm/dd")
bd_field.place(x=400, y=295)
bd_field.bind("<<DateEntrySelected>>", lambda event: valid_Age(bd_field))

pin1 = ""
enterPin = StringVar()
pin = Label(window, text="PIN:", font=("Arial", 16), fg='#162F65', bg="#E7E6DD")
pin.place(x=335, y=335)
pin_field = Entry(window, textvariable=enterPin, width=20, font=entry_font, show='*', state="readonly", fg='#162F65')
pin_field.place(x=400, y=335)

pin2 = ""
enterPin2 = StringVar()
pin_2 = Label(window, text="Re-enter PIN:", font=("Arial", 16), fg='#162F65', bg="#E7E6DD")
pin_2.place(x=254, y=380)
pin2_field = Entry(window, textvariable=enterPin2, width=20, font=entry_font, show='*', state="readonly", fg='#162F65')
pin2_field.place(x=400, y=380)

#Button Specifications
button_border1 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button1 = Button(button_border1, text=' 1 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(1), height=1, width=7)
button1.pack()
button_border1.place(x=255, y=460)

button_border2 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button2 = Button(button_border2, text=' 2 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white', 
                command=lambda: press(2), height=1, width=7)
button2.pack()
button_border2.place(x=355, y=460)

button_border3 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button3 = Button(button_border3, text=' 3 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(3), height=1, width=7)
button3.pack()
button_border3.place(x=455, y=460)

button_border4 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button4 = Button(button_border4, text=' 4 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(4), height=1, width=7)
button4.pack()
button_border4.place(x=255, y=510)

button_border5 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button5 = Button(button_border5, text=' 5 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(5), height=1, width=7)
button5.pack()
button_border5.place(x=355, y=510)

button_border6 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button6 = Button(button_border6, text=' 6 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white', 
                 command=lambda: press(6), height=1, width=7)
button6.pack()
button_border6.place(x=455, y=510)

button_border7 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button7 = Button(button_border7, text=' 7 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(7), height=1, width=7)
button7.pack()
button_border7.place(x=255, y=560)

button_border8 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button8 = Button(button_border8, text=' 8 ',  fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(8), height=1, width=7)
button8.pack()
button_border8.place(x=355, y=560)

button_border9 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button9 = Button(button_border9, text=' 9 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(9), height=1, width=7)
button9.pack()
button_border9.place(x=455, y=560)

button_border0 = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button0 = Button(button_border0, text=' 0 ',  fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(0), height=1, width=7)
button0.pack()
button_border0.place(x=355, y=610)

cancel_border = Frame(window, highlightbackground = "#651616", highlightthickness = 2, bd=0)
cancel = Button(cancel_border, text='CANCEL', fg='white', bg='#AC3333', font='bold',
                command=lambda: cancel_click(), height=1, width=7)
cancel.pack()
cancel_border.place(x=555, y=460)

clear_border = Frame(window, highlightbackground = "#E8AF30", highlightthickness = 2, bd=0)
clear = Button(clear_border, text='CLEAR', fg='white', bg='#E8C766', font='bold',
                    command=clear, height=1, width=7)
clear.pack()
clear_border.place(x=555, y=510)

ok_border = Frame(window, highlightbackground = "#1C6516", highlightthickness = 2, bd=0)
ok = Button(ok_border, text=' OK ', fg='white', bg='#5AAC33', font='bold',
                    command=lambda: error(), height=1, width=7)
ok.pack()
ok_border.place(x=555, y=560)


window.mainloop()


