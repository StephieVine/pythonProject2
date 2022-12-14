from tkinter import *
root = Tk()
root.title("My Calculator Design")

e = Entry(root, width=40, bg="grey", fg="white", borderwidth=40)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# e.insert()

def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# for clearing the screen
def button_clear():
    e.delete(0, END)


# for additon button
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


# for equal button
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "Division":
        e.insert(0, f_num / int(second_number))

    if math == "Percentage":
        e.insert(0, f_num % int(second_number))


def button_Sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_Divide():
    first_number = e.get()
    global f_num
    global math
    math = "Division"
    f_num = int(first_number)
    e.delete(0, END)


def button_Per():
    first_number = e.get()
    global f_num
    global math
    math = "Percentage"
    f_num = int(first_number)
    e.delete(0, END)


# Define buttons
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
button_clear = Button(root, text="Clear", padx=50, pady=20, command=button_clear)
button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_Sub = Button(root, text="-", padx=40, pady=20, command=button_Sub)
button_Per = Button(root, text="%", padx=40, pady=20, command=button_Per)
button_equal = Button(root, text="=", padx=70, pady=20, command=button_equal)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_Divide = Button(root, text="/", padx=40, pady=20, command=button_Divide)

# Put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=6, column=2, columnspan=1)
button_add.grid(row=4, column=1)

button_Sub.grid(row=5, column=0)
button_Per.grid(row=5, column=1)
button_equal.grid(row=6, column=0, columnspan=1)

button_multiply.grid(row=5, column=2)
button_Divide.grid(row=4, column=2)

root.mainloop()