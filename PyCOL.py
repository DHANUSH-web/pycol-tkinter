from tkinter import *
from tkinter import messagebox, colorchooser
import matplotlib.colors as col
import pyperclip as cc
import pygame

window = Tk()
window['bg'] = "white"
window.title("PyCOL by Dhanush H V")
window.iconbitmap("iconImage.ico")  # comment this line if you are using Linux
window.attributes('-topmost', 1)
window.resizable(0, 0)
pygame.mixer.init()

v1 = DoubleVar()
v2 = DoubleVar()
v3 = DoubleVar()
v1.set(255), v2.set(255), v3.set(255)
cols = StringVar()


def getColor():
    r = v1.get()
    g = v2.get()
    b = v3.get()

    hexcc = getHex(r, g, b)
    window['bg'] = hexcc
    colorget.config(bg="white", text=hexcc.upper())
    disp.config(bg=hexcc)
    window.after(5, getColor)

def getRGB(hexColor):
    c = col.to_rgb(hexColor)
    r, g, b = round(c[0]*255), round(c[1]*255), round(c[2]*255)
    return (r, g, b)

def getHex(r, g, b):
    r, g, b = (r / 255), (g / 255), (b / 255)
    c = col.to_hex((r, g, b), False)
    return c

def setValue(n1, n2, n3):
    v1.set(n1)
    v2.set(n2)
    v3.set(n3)

def putColor():
    try:
        hexcc = cols.get()
        if "#" in hexcc:
            c = getRGB(hexcc)
            setValue(c[0], c[1], c[2])

        else:
            c1 = hexcc.split(",")
            r, g, b = int(c1[0]), int(c1[1]), int(c1[2])
            c = getHex(r, g, b).upper()
            window['bg'] = c
            setValue(r, g, b)

    except:
        messagebox.showerror("PyCOL: Error", "Please enter a valid HEX color-code / RGB value")

def sounds(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(loops=0)
'''
def getInfo():
    f = open("moreInfo.txt", 'r')
    r = f.read()
    f.close()
    messagebox.showinfo("Help", r.replace("*", "•"))
'''

def getInfo():
    win = Tk()
    win['bg'] = "white"
    win.title("Welcome to PyCOL")
    win.iconbitmap("iconImage.ico") # comment this line if you are using Linux

    f = open("moreInfo.txt", "r")
    r = f.read()
    f.close()

    def license():
      f = open("LICENSE", 'r')
      r = f.read()
      f.close()

      lbl.config(text=r)
      logo.config(padx=20)

    logo = Label(win, text="PyCOL", font=("Arial", 50, "bold"),
                fg="green", bg="white")
    logo.pack(side="right", padx=120, pady=12)

    lbl = Label(win, text=r.replace("*", "•"), font=("consolas", 11, "bold"),
                justify="left", bg="white")
    lbl.pack(side="top", padx=5, pady=5, expand=True, fill="both")

    btn1 = Button(win, text="Close", bg="white", fg="blue", width=12, bd=2,
                highlightbackground="blue", highlightcolor="white", relief="ridge",
                command=lambda: win.destroy(), font=("Arial", 12, "bold"))
    btn1.pack(side="left", padx=20, pady=20)

    btn2 = Button(win, text="License", bg="white", fg="blue", width=12, bd=2,
                highlightbackground="blue", highlightcolor="white", relief="ridge",
                command=lambda: license(), font=("Arial", 12, "bold"))
    btn2.pack(side="left", padx=20, pady=20)
    sounds("alert.wav")
    win.mainloop()


def copycode():
    getCode = colorget['text']
    cc.copy(getCode)
    print(f"{getCode} copied to clip board")
    sounds("alert.wav")

def choose():
  color_code = colorchooser.askcolor(title ="Choose color")
  c = str(color_code[1])
  cc.copy(c)
  # print(f"{c} copied to clip board")
  n = getRGB(c)
  setValue(n[0], n[1], n[2])
  sounds("alert.wav")


slide1 = Scale(window, variable=v1, from_=0, to=255,
               orient=HORIZONTAL, fg="red",
               length=280, relief="flat", font=("Arial", 11, "bold"))

slide2 = Scale(window, variable=v2, from_=0, to=255,
               orient=HORIZONTAL, fg="green",
               length=280, relief="flat", font=("Arial", 11, "bold"))

slide3 = Scale(window, variable=v3, from_=0, to=255,
               orient=HORIZONTAL, fg="blue",
               length=280, relief="flat", font=("Arial", 11, "bold"))

disp = Frame(window, relief="ridge", bd=2)

# display the background color in Hex Value
colorget = Button(disp, text="#ffffff", font=("Arial", 11, "bold"),
                  bg="white", bd=2, relief="ridge", command= lambda: copycode())

# enter Hex value and press the button to get RGB value
colorput = Entry(disp, textvariable=cols, width=20, justify="center",
                 font=("Arial", 12, "bold"), relief="ridge", bd=2)

colorGet = Button(disp, text="Apply", width=12, bg="white",
                  font=("Arial", 12, "bold"), bd=2,
                  relief="ridge", command=lambda: putColor())

info = Button(disp, text="Help", width=12, bg="white",
              font=("Arial", 12, "bold"), bd=2,
              relief="ridge", command=lambda: getInfo())


colorChoose = Button(window, text = "More colors", font=("Arial", 11, "bold"),
                    bd=2, relief="flat", bg="#746bd6", fg="white", command=choose)

# place sliders
slide1.pack(side="top", padx=20, pady=20, expand=True, fill="both")
slide2.pack(side="top", padx=20, pady=20, expand=True, fill="both")
slide3.pack(side="top", padx=20, pady=20, expand=True, fill="both")
colorChoose.pack(side="top", padx=20, pady=5, expand=True, fill="x")

# place the entities
colorget.pack(side="top", padx=5, pady=5, fill="x")
colorput.pack(side="top", padx=5, pady=5, fill="x")
colorGet.pack(side="left", padx=5, pady=5, fill="x")
info.pack(side="right", padx=5, pady=5, fill="x")
disp.pack(side="top", padx=20, pady=20, fill="both")
getColor()

window.mainloop()
