from distutils import command
import math
from sqlite3 import Row
from tkinter import *
from turtle import window_height

root = Tk()
root.title("Calculator")

#Config our Column rows and columns

#Config Rows
Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=1)
Grid.rowconfigure(root, 5, weight=1)
Grid.rowconfigure(root, 6, weight=1)


#Config Columns
Grid.columnconfigure(root, 0, weight=1 )
Grid.columnconfigure(root, 1, weight=1 )
Grid.columnconfigure(root, 2, weight=1 )

#Define Text Field
field = Entry(root, width=35, borderwidth=5)
field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Define commands
def button_click(number):
    current_number = field.get()
    field.delete(0, END)
    field.insert(0, str(current_number) + str(number))

def button_clear():
    field.delete(0, END)

def button_add():
    first_number = field.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    field.delete(0, END)

def button_subtract():
    first_number = field.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    field.delete(0, END)

def button_multiply():
    first_number = field.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    field.delete(0, END)   

def button_divide():
    first_number = field.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    field.delete(0, END)

def button_equal():
    second_number = field.get()
    field.delete(0, END)
    
    if math == "addition":
        field.insert(0, f_num + int(second_number))
    
    if math == "subtraction":
        field.insert(0, f_num - int(second_number))
    
    if math == "multiplication":
        field.insert(0, f_num * int(second_number))
    
    if math == "division":
        field.insert(0, f_num / int(second_number))

#Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)


#Place buttons on to the window
button_1.grid(row=3, column=0, sticky="nsew")
button_2.grid(row=3, column=1, sticky="nsew")
button_3.grid(row=3, column=2, sticky="nsew")

button_4.grid(row=2, column=0, sticky="nsew")
button_5.grid(row=2, column=1, sticky="nsew")
button_6.grid(row=2, column=2, sticky="nsew")

button_7.grid(row=1, column=0, sticky="nsew")
button_8.grid(row=1, column=1, sticky="nsew")
button_9.grid(row=1, column=2, sticky="nsew")

button_0.grid(row=4, column=0, sticky="nsew")

button_clear.grid(row=4, column=1, columnspan=2, sticky="nsew")
button_add.grid(row=5, column=0, sticky="nsew")
button_equal.grid(row=5, column=1, columnspan=2, sticky="nsew")

button_subtract.grid(row=6, column=0, sticky="nsew")
button_multiply.grid(row=6, column=1, sticky="nsew")
button_divide.grid(row=6, column=2, sticky="nsew")

root.mainloop()