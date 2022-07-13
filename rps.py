from random import choice, randint
import tkinter as tk
import tkinter as ttk
from PIL import Image
import outcome

def rps(choice):

    t = ['Rock', 'Paper', 'Scissors']
    computer = t[randint(0,2)]

    if computer == choice:
        outcome = 'Tied'
        result["text"] = "You have: " + str(outcome)
    elif choice == 'Paper' and computer == 'Scissors':
        outcome = 'Lost'
        result["text"] = "You have: " + str(outcome)
    elif choice == 'Paper' and computer == 'Rock':
        outcome = 'Won'
        result["text"] = "You have: " + str(outcome)
    elif choice == 'Rock' and computer == 'Paper':
        outcome = 'Lost'
        result["text"] = "You have: " + str(outcome)
    elif choice == 'Rock' and computer == 'Scissors':
        outcome = 'Won'
        result["text"] = "You have: " + str(outcome)
    elif choice == 'Scissors' and computer == 'Rock':
        outcome = 'Lost'
        result["text"] = "You have: " + str(outcome)
    elif choice == 'Scissors' and computer == 'Paper':
        outcome = 'Won'
        result["text"] = "You have: " + str(outcome)
    else:
        outcome = 'Error! Please check your option'
        result["text"] = "You have: " + str(outcome)

def buttonclicked():
    rps(f'{cc.get()}')

root = tk.Tk()

winwidth = 400
winheight = 400
swidth = root.winfo_screenwidth()
sheight = root.winfo_screenheight()

centx = int(swidth/2 - winwidth / 2)
centy = int(sheight/2 - winheight / 2)

root.geometry(f'{winwidth}x{winheight}+{centx}+{centy}')
root.title('Rock, Paper, Scissors')
root.iconphoto(False, tk.PhotoImage(file='/Users/User/Desktop/python/stuff/rps.jpg'))

signin= ttk.Frame(root)
signin.pack(padx=10., pady=10, fill='x', expand=True)

cc = tk.StringVar()

choice_label = ttk.Label(signin, text="Choice")
choice_label.pack(fill='x', expand=True)

choice_entry = ttk.Entry(signin, textvariable=cc)
choice_entry.pack(fill='x', expand=True)
choice_entry.focus()

button = ttk.Button(signin, text="Confim Choice", command=buttonclicked)
button.pack(fill='x', expand=True)

result = ttk.Label(signin, text="You have: ")
result.pack(fill='x', expand=True)

root.mainloop()