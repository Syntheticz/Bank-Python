from tkinter import *
import subprocess
import os
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
image = Image.open("C:/Users/simon/OneDrive/Desktop/school/progs/Second Year/Python/BankSystem/new.png")
photo_label = Label(window, bg="#E7E6DD")
photo = ImageTk.PhotoImage(image)
photo_label.config(image=photo)
photo_label.place(x=350, y=20)

# Insert Instructions for User
instruct = Label(window, text="Please enter money to transfer.", font=("Arial", 16), fg='#162F65', bg="#E7E6DD")
instruct.place(x=300, y=180)

#Text Field for Account Number
money = ""

# Function for pressing the button
def press(denom):
    global money
    if len(money)<1:            # User is only allowed to press 1 button
        money += str(denom)
        transfer.set(money)
    else:
        error()

# Function that shows error message if input is invalid
def error():
    global errorlb
    num = int(transfer.get())

    if len(money)>1:
        errorlb = Label(window, text="Press only ONE denomination.", font=("Arial", 12), fg='#AC3333', bg="#E7E6DD")
        errorlb.place(x=336, y=280)
    elif num < 100:
        errorlb = Label(window, text="Minimum amount is 100.", font=("Arial", 12), fg='#AC3333', bg="#E7E6DD")
        errorlb.place(x=360, y=280)
    elif num > 50000:
        errorlb = Label(window, text="Maximum amount is 50,000.", font=("Arial", 12), fg='#AC3333', bg="#E7E6DD")
        errorlb.place(x=345, y=280)
    elif num % 100 != 0:
        errorlb = Label(window, text="Amount should only be multiples of 100.", font=("Arial", 12), fg='#AC3333', bg="#E7E6DD")
        errorlb.place(x=305, y=280)
    #elif num : PAKI LAGAY NALANG DITO IF GREATER THAN CURRENT BALANCE
        #errorlb = Label(window, text="Amount is greater than current balance.", font=("Arial", 12), fg='#AC3333', bg="#E7E6DD")
        #errorlb.place(x=305, y=280) 
    else:
        errorlb = Label(window, text="Input is invalid.", font=("Arial", 12), fg='#AC3333', bg="#E7E6DD")
        errorlb.place(x=400, y=280)


# Function to clear contents in text field
def clear():
    global money
    money = ""
    transfer.set("")
    errorlb.config(text="", fg="#E7E6DD")   # Clears error message
    
# Function when 'custon' button is clicked
def custom():
    global money
    money = ""
    transfer.set("")
    transfer_field.configure(state='normal')    # Allows users to edit the text field

# Validates user input   
def check_input():
    custom_input = transfer_field.get()

    num = int(custom_input)
    if num%100==0 and num<50000:
        transfer.set(custom_input)
        # if you need to access the value of 'transfer' use transfer.get()
        next()
    else:
        error()

# Goes to next window and closes current window
def next():
    window.destroy()
    #current_directory = os.path.dirname(os.path.abspath(__file__))
    #script_path = os.path.join(current_directory, "trans_menu.py")
    #subprocess.run(["python", script_path]) 

def back():
    window.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_directory, "trans_menu.py")
    subprocess.run(["python", script_path])

#Text Field Specifications
transfer = StringVar()
entry_font = ("Arial", 14) 
transfer_field = Entry(window, textvariable=transfer, width=20, font=entry_font, state='readonly',      # Does not allow users to edit text field
                  justify="center", fg='#162F65')
transfer_field.place(x=335, y=225)

# Transfer Denominations 
button500_border = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button500 = Button(button500_border, text=' 500 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(500), height=1, width=7)
button500.pack()
button500_border.place(x=255, y=320)

button1000_border = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button1000 = Button(button1000_border, text=' 1000 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(1000), height=1, width=7)
button1000.pack()
button1000_border.place(x=355, y=320)

button2000_border = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button2000 = Button(button2000_border, text=' 2000 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(2000), height=1, width=7)
button2000.pack()
button2000_border.place(x=455, y=320)

button3000_border = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button3000 = Button(button3000_border, text=' 3000 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(3000), height=1, width=7)
button3000.pack()
button3000_border.place(x=255, y=370)

button5000_border = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button5000 = Button(button5000_border, text=' 5000 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(5000), height=1, width=7)
button5000.pack()
button5000_border.place(x=355, y=370)

button10000_border = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
button10000 = Button(button10000_border, text=' 10,000 ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=lambda: press(10000), height=1, width=7)
button10000.pack()
button10000_border.place(x=455, y=370)

buttonCust_border = Frame(window, highlightbackground = "#162F65", highlightthickness = 2, bd=0)
buttonCust = Button(buttonCust_border, text=' CUSTOM ', fg='#162F65', bg='#E7E6DD', font='bold', activebackground='#3361AC', activeforeground='white',
                 command=custom, height=1, width=8)
buttonCust.pack()
buttonCust_border.place(x=350, y=420)

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
            command = check_input, height=1, width=7)                    
ok.pack()
ok_border.place(x=555, y=420)




window.mainloop()