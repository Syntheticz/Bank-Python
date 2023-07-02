from tkinter import *
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

removelb = Label(window, text=("Please insert flash drive."), font=("Arial", 20), fg='#162F65', bg="#E7E6DD")
removelb.grid(row=0, column=0, sticky="nsew")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Logo
image = Image.open("C:/Users/simon/OneDrive/Desktop/school/progs/Second Year/Python/BankSystem/new.png")
photo_label = Label(window, bg="#E7E6DD")
photo = ImageTk.PhotoImage(image)
photo_label.config(image=photo)
photo_label.place(x=350, y=20)


window.mainloop()