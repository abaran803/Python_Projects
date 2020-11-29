# Module Imported
from tkinter import *
import random
from PIL import ImageTk ,Image

# App Window
root = Tk()

# Window Size
root.minsize(360,240)
# root.maxsize(720,480)

# Window title bar
root.title("Dice Roller")
p1 = ImageTk.PhotoImage(Image.open("./images/icon2.jpg"))
root.iconphoto(False, p1)

# Values on dice
def dice_roll(val):
    w = root.winfo_width()
    h = root.winfo_height()
    if val == "1":
        print("One")
        img = Image.open("./images/one_.png")
    elif val == "2":
        print("Two")
        img = Image.open("./images/two_.png")
    elif val == "3":
        print("Three")
        img = Image.open("./images/three_.png")
    elif val == "4":
        print("Four")
        img = Image.open("./images/four_.png")
    elif val == "5":
        print("Five")
        img = Image.open("./images/five_.png")
    elif val == "6":
        print("Six")
        img = Image.open("./images/six_.png")
    elif val == "exit":
        print("Program Ended")
        return
    else:
        print("Invalid Query")
        print("Try Again")
        InsVal = random.randrange(1, 6)
        dice_roll(str(InsVal))
    img = img.resize((int(w/2),int(h/2)), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    pannn.configure(image=img, width = int(root.winfo_width()/2), height = int(root.winfo_height()/2))
    pannn.image = img

# Roll button action
def dice_Val():
    val = random.randrange(1, 7)
    dice_roll(str(val))
    # B.grid(row = 1,column = 1, columnspan = 2)
    # C.grid(row = 1,column = 3)

# Background image
background_image = ImageTk.PhotoImage(Image.open("./images/background.jpg"))
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Dice image
imggg = Image.open("./images/icon2.jpg")
# imggg = imggg.resize((int(root.winfo_width()), int(root.winfo_height())), Image.ANTIALIAS)
imggg = imggg.resize((360, 240), Image.ANTIALIAS)
imgggg = ImageTk.PhotoImage(imggg)
pannn = Label(root, image=imgggg)#, width = root.winfo_width(), height = root.winfo_height())
pannn.pack(pady = 80, padx = 80)
B = Button(root, text = "Press to Roll", command = dice_Val)
C = Button(root, text = "Exit", command = root.destroy)
B.pack(side = BOTTOM)
C.pack(side = BOTTOM)
# B.grid(row = 1,column = 1)
# C.grid(row = 1,column = 3)

# pannn.grid(row = 0, column = 1, columnspan = 3)

# Buttons - Roll and Exit
# B = Button(root, text = "Press to Roll", command = dice_Val, bd = 4, relief = RAISED)
# C = Button(root, text = "Exit", command = root.destroy, bd = 4, relief = RAISED)
# B.grid(row = 1,column = 1, columnspan = 2, sticky='ew')
# C.grid(row = 1,column = 3, sticky = 'ew')

# End of App
root.mainloop()