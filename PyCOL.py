from tkinter import *
from tkinter import messagebox
import matplotlib.colors as col
import pyperclip as cc

window = Tk()
window['bg'] = "white"
window.title("PyCOL by Dhanush H V")
window.iconbitmap("iconImage.ico")
window.resizable(0, 0)

v1 = DoubleVar()
v2 = DoubleVar()
v3 = DoubleVar()
v1.set(255), v2.set(255), v3.set(255)
cols = StringVar()


def getColor():
    r = v1.get()
    g = v2.get()
    b = v3.get()

    r, g, b = (r / 255), (g / 255), (b / 255)
    hexcc = col.to_hex((r, g, b), False)
    window['bg'] = hexcc
    colorget.config(bg="white", text=hexcc.upper())
    disp.config(bg=hexcc)
    window.after(5, getColor)


def putColor():
    try:
        hexcc = cols.get()
        if "#" in hexcc:
            c = col.to_rgb(hexcc)
            r, g, b = round(c[0] * 255), round(c[1] * 255), round(c[2] * 255)

            v1.set(r)
            v2.set(g)
            v3.set(b)

        else:
            c1 = hexcc.split(",")
            r, g, b = int(c1[0]), int(c1[1]), int(c1[2])
            r, g, b = (r / 255), (g / 255), (b / 255)
            c = col.to_hex((r, g, b), False).upper()
            window['bg'] = c

            v1.set(r * 255)
            v2.set(g * 255)
            v3.set(b * 255)

    except:
        messagebox.showerror("PyCOL: Error", "Please enter a valid HEX colo-code / RGB value")

'''
def getInfo():
    f = open("moreInfo.txt", 'r')
    r = f.read()
    f.close()
    messagebox.showinfo("More Info", r.replace("*", "•"))

'''
def getInfo():
    win = Tk()
    win['bg'] = "white"
    win.title("Welcome to PyCOL")

    f = open("moreInfo.txt", "r")
    r = f.read()
    f.close()

    logo = Label(win, text="PyCOL", font=("Arial", 50, "bold"),
                fg="green", bg="white")
    logo.pack(side="left", padx=120, pady=12)

    lbl = Label(win, text=r.replace("*", "•"), font=("consolas", 11, "bold"),
                justify="left", bg="white")
    lbl.pack(side="top", padx=5, pady=5, expand=True, fill="both")

    btn = Button(win, text="Close", bg="white", fg="blue", width=12, bd=2,
                highlightbackground="blue", highlightcolor="white", relief="ridge",
                command=lambda: win.destroy(), font=("Arial", 12, "bold"))
    btn.pack(side="right", padx=20, pady=20)
    win.mainloop()


def copycode():
    getCode = colorget['text']
    cc.copy(getCode)
    print(f"{getCode} copied to clip board")


'''
def choose():
  color_code = colorchooser.askcolor(title ="Choose color")
  cc.copy(str(color_code))
  print(f"{color_code} copied to clip board")
'''

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
                  bg="white", bd=2, relief="ridge", command=copycode)

# enter Hex value and press the button to get RGB value
colorput = Entry(disp, textvariable=cols, width=20, justify="center",
                 font=("Arial", 12, "bold"), relief="ridge", bd=2)

colorGet = Button(disp, text="Apply", width=12, bg="white",
                  font=("Arial", 12, "bold"), bd=2,
                  relief="ridge", command=lambda: putColor())

info = Button(disp, text="Help", width=12, bg="white",
              font=("Arial", 12, "bold"), bd=2,
              relief="ridge", command=lambda: getInfo())

'''
colorChoose = Button(window, text = "Choose color", font=("Arial", 11, "bold"),
                 bg="white", bd=2, relief="ridge", command=choose)
'''

# place sliders
slide1.pack(side="top", padx=20, pady=20)
slide2.pack(side="top", padx=20, pady=20)
slide3.pack(side="top", padx=20, pady=20)
# colorChoose.pack(side="top", padx=20, pady=5)

# place the entities
colorget.pack(side="top", padx=5, pady=5, fill="x")
colorput.pack(side="top", padx=5, pady=5, fill="x")
colorGet.pack(side="left", padx=5, pady=5, fill="x")
info.pack(side="right", padx=5, pady=5, fill="x")
disp.pack(side="top", padx=20, pady=20, fill="both")
getColor()
window.mainloop()
