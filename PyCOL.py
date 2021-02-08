from tkinter import *
from tkinter import messagebox
import matplotlib.colors as col

window = Tk()
window['bg'] = "white"
window.title("PyCOL by Dhanush H V")
window.iconbitmap("iconImage.ico")
window.resizable(0, 0)

v1 = DoubleVar()
v2 = DoubleVar()
v3 = DoubleVar()
cols = StringVar()

def getColor():
    r = v1.get()
    g = v2.get()
    b = v3.get()

    r, g, b = (r/255), (g/255), (b/255)
    hexcc = col.to_hex((r, g, b), False)
    window['bg'] = hexcc
    colorget.config(bg="white", text=hexcc.upper())
    disp.config(bg=hexcc)
    window.after(5, getColor)


def putColor():
    try:
        hexcc = cols.get()
        c = col.to_rgb(hexcc)
        r, g, b = round(c[0]*255), round(c[1]*255), round(c[2]*255)

        v1.set(r)
        v2.set(g)
        v3.set(b)

    except:
        messagebox.showerror("PyCOL: Error", "Plese enter a valid HEX colo-code")


def getInfo():
    f = open("moreInfo.txt", 'r')
    r = f.read()
    f.close()
    messagebox.showinfo("More Info", r)


slide1 = Scale(window, variable=v1, from_ = 0, to = 255,
              orient = HORIZONTAL, background="white",
              length = 280, relief = "flat")

slide2 = Scale(window, variable=v2, from_ = 0, to = 255,
              orient = HORIZONTAL, background="white",
              length = 280)

slide3 = Scale(window, variable=v3, from_ = 0, to = 255,
              orient = HORIZONTAL, background="white",
              length = 280)

disp = Frame(window, relief="ridge", bd=2)

# display the background color in Hex Value
colorget = Label(disp, text = "#ffffff", font=("Arial", 11, "bold"),
                 bg="white", bd=2, relief="ridge")

# enter Hex value and press the button to get RGB value
colorput = Entry(disp, textvariable=cols, width=20, justify="center",
                 font=("Arial", 12, "bold"), relief="ridge", bd=2)
colorGet = Button(disp, text="Apply", width=12, bg="white",
                  font=("Arial", 12, "bold"), bd=2,
                  relief="ridge", command = lambda: putColor())

info = Button(disp, text="More Info", width=12, bg="white",
                  font=("Arial", 12, "bold"), bd=2,
                  relief="ridge", command = lambda: getInfo())

# place sliders
slide1.pack(side="top", padx=20, pady=20)
slide2.pack(side="top", padx=20, pady=20)
slide3.pack(side="top", padx=20, pady=20)

# place the entities
colorget.pack(side="top", padx=5, pady=5, fill="x")
colorput.pack(side="top", padx=5, pady=5, fill="x")
colorGet.pack(side="left", padx=5, pady=5, fill="x")
info.pack(side="right", padx=5, pady=5, fill="x")
disp.pack(side="top", padx=20, pady=20, fill="both")
getColor()
window.mainloop()
