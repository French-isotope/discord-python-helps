from tkinter import *

window = Tk()
window.title("Calculator")
ent = Entry(window, bg="blue", width=25)
ent.grid(row=0, column=0)

op_pos = 0
op = ""
number = 0


def click(bt):
    ent.insert(25, bt)
    if bt == "AC":
        ent.delete(0, 'end')
    elif bt == "+" or bt == "-" or bt == "=":
        global op_pos
        global op
        global number
        entry_string = ent.get()
        if op_pos != 0:
            op_pos += 1
        print("input string: " + entry_string[op_pos:])
        number_str = entry_string[op_pos:-1]
        print("input number: " + number_str)
        # op_pos = operation position (character wise)
        # Len is length
        if op == "+":
            number = number + int(number_str)
        elif op == "-":
            number = number - int(number_str)
        else:
            number = int(number_str)
        op_pos = len(entry_string) - 1
        op = entry_string[-1:]
        if op == "=":
            ent.delete(0, 'end')
            ent.insert(25, str(number))
        print(op)
        print(str(op_pos))
        print(str(number))

def draw_button(number, row_index, column_index):
    button = Button(window, text=number, command=lambda: click(number))
    button.grid(row=row_index, column=column_index)


draw_button("7", 1, 1)
draw_button("8", 1, 2)
draw_button("9", 1, 3)
draw_button("4", 2, 1)
draw_button("5", 2, 2)
draw_button("6", 2, 3)
draw_button("3", 3, 1)
draw_button("2", 3, 2)
draw_button("1", 3, 3)
draw_button("0", 4, 1)
draw_button("-", 4, 2)
draw_button("+", 4, 3)
draw_button("=", 4, 4)
draw_button("AC", 3, 4)

window.mainloop()