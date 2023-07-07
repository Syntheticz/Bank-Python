from tkinter import *
import os
import sys
from PIL import ImageTk, Image
import subprocess
import time



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from filehandling import CARD_PATH, KEY, read_card, get_card_path, get_key
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
does_exist = False

def check_removable_drive():
    # Run system command to get drive information
    cmd = "wmic logicaldisk get caption, drivetype"
    output = subprocess.check_output(cmd, shell=True).decode("utf-8")

    # Parse the output to extract removable drives
    drives = []
    lines = output.strip().split("\n")[1:]
    for line in lines:
        drive, drivetype = line.split()
        if int(drivetype) == 2:
            drives.append(drive)

    return drives

def get_removeable_drive_path(drive_letter):
    cmd = "wmic logicaldisk where caption='{}' get name".format(drive_letter)
    output = subprocess.check_output(cmd, shell=True).decode("utf-8")
    lines = output.strip().split("\n")
    if len(lines) >= 2:
        drive_path = lines[1].strip()
        return drive_path
    return None


def initial_card_check():
    # Initial check for removable drives
    global CARD_PATH

    previous_drives = check_removable_drive()
    print("Please insert Flash Drive...")

    # Wait for a short interval before checking again
    interval = 0.5  # in seconds
    time.sleep(interval)

    # Check for removable drives
    current_drives = check_removable_drive()

    # Compare current and previous drives to detect changes
    added_drives = [drive for drive in current_drives if drive not in previous_drives]
    removed_drives = [drive for drive in previous_drives if drive not in current_drives]

    # Handle added and removed drives
    if added_drives:
        print("Card Inserted")
        print("Validating...")
        drive_path = get_removeable_drive_path(added_drives[0])
        file_path = f"{drive_path}\\record.txt"
      
        CARD_PATH = file_path 
        if not os.path.isfile(file_path):
            print("file not found")
            return 2
        else:   
            return 1

    if removed_drives:
        print("Removed Card")
        return 3
        

    # Update the previous drives list
    previous_drives = current_drives

def after_init():
    global does_exist
    # Call the initial_card_check function
    # Process the result
    result = initial_card_check()
    if result == 1:
        does_exist = True
    
    if does_exist:
        window.destroy()
        current_directory = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_directory, "log_in.py")
        subprocess.run(["python", script_path])

    if result == 2:
        window.destroy()
        current_directory = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_directory, "register.py")
        subprocess.run(["python", script_path])
    
    window.after(100, after_init)

       
    
after_init()

window.mainloop()


