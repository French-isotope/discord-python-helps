from tkinter import *

root = Tk()
root.title("Chess Thing")

#PUT WINDOW IN THE MIDDLE
app_width = 400
app_height = 175

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

#WIDGETS NO 0
filler_1 = Label(root, text=" ")
filler_2 = Label(root, text=" ")
label_header = Label(root, text="Choose One", font=20)
button_add_window = Button(root, text="Adding Window", padx=20, pady=20)
button_get_window = Button(root, text="Get Data Window", padx=20, pady=20)

#PUTTING WIDGETS NO 0
filler_1.grid(row=0, column=0)
label_header.grid(row=1, column=1)
filler_2.grid(row=2, column=0)
button_add_window.grid(row=3, column=2)
button_get_window.grid(row=3, column=0)

root.mainloop()