import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import IntVar

# Project is inspired from https://www.youtube.com/watch?v=je1LcqXQAhU

database = {
    "sidedish" : {
        "position":{
            "x":10,
            "y":100
        },
        "elements" : {
            "Fries":{
               "price":"50",
               "quantity":IntVar()
            },
            "Salad":{
                "price": "50",
                "quantity":IntVar()
            },
            "Mashed Potato":{
                "price": "50",
                "quantity":IntVar()
            }
        }
    },

    "pizza": {
        "position": {
            "x": 10,
            "y": 100
        },
        "elements": {
            "Cheese Pizza": {
                "price": "50",
                "quantity":tkinter.IntVar
            },
            "Pepperoni Pizza": {
                "price": "50",
                "quantity":tkinter.IntVar
            },
            "Hawaiian Pizza": {
               "price": "50",
                "quantity":tkinter.IntVar
            }
        }
    },

    "drinks": {
        "position": {
            "x": 10,
            "y": 100
        },
        "elements": {
            "Tea": {
                "price": "50",
                "quantity":tkinter.IntVar
            },
            "Coffee": {
                "price": "50",
                "quantity":tkinter.IntVar
            },
            "Cola": {
                "price": "50",
                "quantity":tkinter.IntVar
            }
        }
    }
}


def reset_ds(ds):
    for category in ds:
        for element in ds[category]["elements"]:
            print(f'test {ds[category]["elements"][element]["quantity"]}')
            ds[category]["elements"][element]["quantity"].set(0)
            print(f'test {ds[category]["elements"][element]["quantity"]}')
#            element["quantity"].set("0")



database2 = reset_ds(database)


print(database2)


window2 = Tk()
window2.title("Eazy Peazy")

# fonts
btnfonts = Font(family="Helvetica", size=12, weight="normal")
ttlfonts = Font(family="Times", size=50, weight="bold")
cntfonts = Font(family="Times", size=12, weight="normal")

screen_width = window2.winfo_screenwidth()
screen_height = window2.winfo_screenheight()
window2_width = screen_width
window2_height = screen_height

c = (screen_width / 2) - (window2_width / 2)
d = (screen_height / 2) - (window2_height / 2)

window2.geometry(F'{window2_width}x{window2_height}+{int(c)}+{int(d)}')

# logo


# name
lbl1 = Frame(window2, width=1350, height=110, bd=12, relief="raised")
lbl1.pack(side=TOP)
ttl = Label(window2, text="Eazy Pizzy", font=ttlfonts)
ttl.place(x=500, y=10)

# menusetup
BottomMainFrame = Frame(window2, width=1350, height=650, bd=12, relief="raised")
BottomMainFrame.pack(side=BOTTOM)

f1 = Frame(BottomMainFrame, width=450, height=650, bd=12, relief="raised")
f1.pack(side=LEFT)
f2 = Frame(BottomMainFrame, width=450, height=650, bd=12, relief="raised")
f2.pack(side=LEFT)
f3top = Frame(BottomMainFrame, width=450, height=500, bd=12, relief="raised")
f3top.pack(side=TOP)
f3bot = Frame(BottomMainFrame, width=450, height=150, bd=12, relief="raised")
f3bot.pack(side=BOTTOM)

# vars
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)

# FRAME1----------------------------------------------------------------------------------------------------------------

lblMeal = Label(f1, font=('arial', 18, 'bold'), text="Side Dish")
lblMeal.grid(row=0, column=0)

Checkbutton(f1, text="Fries\t\t P50.00", variable=var1, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=1, column=0, sticky=W)

Checkbutton(f1, text="Salad\t\t P55.00", variable=var2, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=2, column=0, sticky=W)

Checkbutton(f1, text="Mashed Potato\t P50.00", variable=var3, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=3, column=0, sticky=W)

Checkbutton(f1, text="Chicken Sandwich P55.00", variable=var4, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=4, column=0, sticky=W)

Checkbutton(f1, text="Nachos\t\t P50.00", variable=var5, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=5, column=0, sticky=W)

lblspace = Label(f1, text="\n\n\n\n\n\n\n\n\n")
lblspace.grid(row=9, column=0)

# FRAME2-----------------------------------------------------------------------------------------------------------------
lblMeal = Label(f2, font=('arial', 18, 'bold'), text="Pizza")
lblMeal.grid(row=0, column=0)

Checkbutton(f2, text="Cheese Pizza\t P50.00", variable=var6, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=1, column=0, sticky=W)

Checkbutton(f2, text="Pepperoni Pizza\t P50.00", variable=var7, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=2, column=0, sticky=W)

Checkbutton(f2, text="Hawaiian Pizza\t P50.00", variable=var8, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=3, column=0, sticky=W)

Checkbutton(f2, text="Supreme Pizza\t P50.00", variable=var9, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=4, column=0, sticky=W)

Checkbutton(f2, text="Stuffed Pizza\t P50.00", variable=var10, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=5, column=0, sticky=W)

lblspace = Label(f2, text="\n\n\n\n\n\n\n\n\n")
lblspace.grid(row=9, column=0)

# FRAME3-----------------------------------------------------------------------------------------------------------------

lblMeal = Label(f3top, font=('arial', 18, 'bold'), text="Drinks\n")
lblMeal.grid(row=0, column=0)

Checkbutton(f3top, text="Tea\t\t P50.00", variable=var11, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=1, column=0, sticky=W)

Checkbutton(f3top, text="Cola\t\t P50.00", variable=var12, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=2, column=0, sticky=W)

Checkbutton(f3top, text="Coffee\t\t P50.00", variable=var13, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=3, column=0, sticky=W)

Checkbutton(f3top, text="Orange\t\t P50.00", variable=var14, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=4, column=0, sticky=W)

Checkbutton(f3top, text="Bottle Water\t P50.00", variable=var15, onvalue=1, offvalue=0,
            font=('arial', 18, 'bold')).grid(row=5, column=0, sticky=W)


# FRAME3bot-----------------------------------------------------------------------------------------------------------------

def checkout():
    chkwindow = Toplevel()

    screen_width = chkwindow.winfo_screenwidth()
    screen_height = chkwindow.winfo_screenheight()
    chkwindow_width = screen_width
    chkwindow_height = screen_height

    c = (screen_width / 2) - (chkwindow_width / 2)
    d = (screen_height / 2) - (chkwindow_height / 2)

    window2.geometry(F'{window2_width}x{window2_height}+{int(c)}+{int(d)}')


chkout = Button(f3bot, text="Check out", command=checkout)
chkout.pack()

window2.mainloop()
