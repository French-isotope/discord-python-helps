import tkinter
from tkinter import *
from tkinter.font import Font

window2 = Tk()
window2.title("Eazy Peazy")

# fonts
ttlfonts = Font(family="Times", size=50, weight="bold")

screen_width = window2.winfo_screenwidth()
screen_height = window2.winfo_screenheight()
window2_width = screen_width
window2_height = screen_height

c = (screen_width / 2) - (window2_width / 2)
d = (screen_height / 2) - (window2_height / 2)

window2.geometry(F'{window2_width}x{window2_height}+{int(c)}+{int(d)}')

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


database = {
    "sidedish" : {
        "font":{
            'font':'arial',
            'size':12,
            'weight':'bold'},
        "position":{
            "x":10,
            "y":100,
            "row":0,
            "f":f1
        },
        "elements" : {
            "Fries":{
               "price":"50",
               "quantity":tkinter.IntVar(value=0)
            },
            "Salad":{
                "price": "50",
                "quantity":tkinter.IntVar(value=0)
            },
            "Mashed Potato":{
                "price": "50",
                "quantity":tkinter.IntVar(value=0)
            },
            "Not Mashed Potato1":{
                "price": "50",
                "quantity":tkinter.IntVar(value=0)
            },
            "Not Mashed Potato2":{
                "price": "50",
                "quantity":tkinter.IntVar(value=0)
            },
            "Not Mashed Potato3":{
                "price": "50",
                "quantity":tkinter.IntVar(value=0)
            }
        }
    },
    "pizza": {
        "font": {
            'font': 'arial',
            'size': 12,
            'weight': 'bold'},
        "position": {
            "x": 10,
            "y": 100,
            "row":9,
            "f":f2
        },
        "elements": {
            "Cheese Pizza": {
                "price": "50",
                "quantity":tkinter.IntVar(value=0)
            },
            "Pepperoni Pizza": {
                "price": "50",
                "quantity":tkinter.IntVar(value=0)
            },
            "Hawaiian Pizza": {
               "price": "50",
                "quantity":tkinter.IntVar(value=0)
            }
        }
    },
    "drinks": {
        "font": {
            'font': 'arial',
            'size': 12,
            'weight': 'bold'},
        "position": {
            "x": 10,
            "y": 100,
            "row":9,
            "f":f3top
        },
        "elements": {
            "Tea": {
                "price": "50",
                "quantity":tkinter.IntVar(value=0)
            },
            "Coffee": {
                "price": "50",
                "quantity":tkinter.IntVar(value=0)
            },
            "Cola": {
                "price": "50",
                "quantity":tkinter.IntVar(value=0)
            }
        }
    }
}


def reset_quantity_in_datastructure(ds):
    ds_modified = ds.copy()
    for category in ds:
        for element in ds[category]["elements"]:
            ds_modified[category]["elements"][element]["quantity"] = 0
    return ds_modified


def checkout():
    chkwindow = Toplevel()

    screen_width = chkwindow.winfo_screenwidth()
    screen_height = chkwindow.winfo_screenheight()
    chkwindow_width = screen_width
    chkwindow_height = screen_height

    c = (screen_width / 2) - (chkwindow_width / 2)
    d = (screen_height / 2) - (chkwindow_height / 2)

    window2.geometry(F'{window2_width}x{window2_height}+{int(c)}+{int(d)}')

for category in database:
    font = database[category]["font"]["font"]
    size = database[category]["font"]["size"]
    grease = database[category]["font"]["weight"]

    lblMeal = Label(database[category]["position"]["f"], font=(font, size, grease), text=category)
    lblMeal.grid(row=0, column=0)
    lblspace = Label(database[category]["position"]["f"], text="\n\n\n\n\n\n\n\n\n")
    lblspace.grid(row=0, column=0)
    for id, element in enumerate(database[category]["elements"]):
        id += 1
        Checkbutton(database[category]["position"]["f"], text=f"{element}\t\t P50.00", variable=database[category]["elements"][element]["quantity"], onvalue=1, offvalue=0,
                    font=(font, size, grease)).grid(row=id, column=0, sticky=W)
        Entry(database[category]["position"]["f"], font=(font, size, grease), width=4).grid(row=id, column=1)


    lblspace = Label(database[category]["position"]["f"], text="\n\n\n\n\n\n\n\n\n")
    lblspace.grid(row=database[category]["position"]["row"], column=0)

chkout = Button(f3bot, text="Check out", command=checkout)
chkout.pack()



def task():
    print(database["sidedish"]["elements"]["Fries"]["quantity"].get())
    window2.after(10000, task)  # reschedule event in 2 seconds

window2.after(2000, task)

window2.mainloop()