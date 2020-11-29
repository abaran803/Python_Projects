from tkinter import *
import random
from PIL import ImageTk ,Image

root = Tk()
root.minsize(360,240)
root.maxsize(720,480)
root.title("Dice Roller")
root.config(bg = "grey")
p1 = ImageTk.PhotoImage(Image.open("./images/icon2.jpg"))
root.iconphoto(False, p1)

def dice_roll(val):
    w = root.winfo_width()
    h = root.winfo_height()
    print(w)
    print(h)
    if val == "1":
        print("One")
        img = Image.open("./images/one_.png")
        img = img.resize((int(w/2),int(h/2)), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        pannn.configure(image=img)
        pannn.image = img
    elif val == "2":
        print("Two")
        img = Image.open("./images/two_.png")
        img = img.resize((int(w/2),int(h/2)), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        pannn.configure(image=img)
        pannn.image = img
    elif val == "3":
        print("Three")
        img = Image.open("./images/three_.png")
        img = img.resize((int(w/2),int(h/2)), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        pannn.configure(image=img)
        pannn.image = img
    elif val == "4":
        print("Four")
        img = Image.open("./images/four_.png")
        img = img.resize((int(w/2),int(h/2)), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        pannn.configure(image=img)
        pannn.image = img
    elif val == "5":
        print("Five")
        img = Image.open("./images/five_.png")
        img = img.resize((int(w/2),int(h/2)), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        pannn.configure(image=img)
        pannn.image = img
    elif val == "6":
        print("Six")
        img = Image.open("./images/six_.png")
        img = img.resize((int(w/2),int(h/2)), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        pannn.configure(image=img)
        pannn.image = img
    elif val == "exit":
        print("Program Ended")
        return
    else:
        print("Invalid Query")
        print("Try Again")
        InsVal = random.randrange(1, 6)
        dice_roll(str(InsVal))

def dice_Val():
    val = random.randrange(1, 7)
    dice_roll(str(val))
    B.place(relx = 0.5, rely = 0.78-((root.winfo_height()-240)/3000), anchor = 'center')
    C.place(relx = 0.5, rely = 0.9-((root.winfo_height()-240)/1800), anchor = 'center')

background_image = ImageTk.PhotoImage(Image.open("./images/background.jpg"))
background_label = Label(root, image=background_image, borderwidth=10, relief="solid")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

imggg = Image.open("./images/icon2.jpg")
imggg = imggg.resize((int(root.winfo_width()/2), int(root.winfo_height()/2)), Image.ANTIALIAS)
imgggg = ImageTk.PhotoImage(imggg)
pannn = Label(root, image=imgggg, borderwidth=10, relief=SUNKEN)
pannn.place(relx = 0.5, rely = 0.4, anchor = 'center')

B = Button(root, text = "Press to Roll", command = dice_Val)
C = Button(root, text = "Exit", command = root.destroy)
B.place(relx = 0.5, rely = 0.78-((root.winfo_height()-240)/3000), anchor = 'center')
C.place(relx = 0.5, rely = 0.9-((root.winfo_height()-240)/1800), anchor = 'center')

root.mainloop()