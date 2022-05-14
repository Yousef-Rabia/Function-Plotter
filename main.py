# Import needed libraries
from tkinter import messagebox
from tkinter import *
from matplotlib import pyplot as plot
from sympy import symbols, parse_expr
import numpy as np


def exit():
    answer=messagebox.askokcancel(title="Exit",message= "Are you sure you want to Exit!")
    if(answer):
        Func_plot.destroy()


def plot_function():
    try:
        min_value = int(min_x.get())
    except:
        messagebox.showerror('Input Error', 'Please fill Min value with valid input')
    try:
        max_value = int(max_x.get())   
    except:
        messagebox.showerror('Input Error', 'Please fill Max value with valid input')
    try:
        function_to_plot = Func.get()
    except:
        messagebox.showerror('Input Error', 'Please fill Function blank with valid input')
    if min_value < max_value:
        subs_function(min_value, function_to_plot)
        subs_function(max_value, function_to_plot)
        plot_it(function_to_plot)
        Func_plot.mainloop()
    else:
        messagebox.showerror('Limited Error', 'Max value should be greater than min value')


def subs_function(values,func_of_x):
    x=symbols('x')
    try:
        exp = parse_expr(func_of_x.replace('^','**'))
        exp_v = exp.subs(x,values)
    except:
        messagebox.showerror('Input Error', 'Please fill Function blank with valid input')
    return exp_v

def plot_it(function_to_plot):
    try:
        min_value = int(min_x.get())
    except:
        messagebox.showerror('Input Error', 'Invalid Min value')
    try:
        max_value = int(max_x.get())   
    except:
        messagebox.showerror('Input Error', 'Invalid Max value')

    x_axis = []
    y_axis = []
    i = float(min_x.get())


    while i<max_value:
        x_axis.append(i)
        i=i+0.15

    for values in x_axis:
        y_axis.append(subs_function(values, Func.get()))

    plot.title(function_to_plot)
    try:
        plot.plot(x_axis, y_axis)
    except:
        messagebox.showerror('Input Error', 'Please fill Function blank with valid input')
        return
    plot.axhline(y=0, color='black')
    plot.axvline(x=0, color='black')
    plot.xlabel("x-axis")
    plot.ylabel("y-axis")
    plot.grid(color='black',linewidth=0.2)

    plot.show()
# Create Main app window
Func_plot = Tk()

# Change app title
Func_plot.title("Function Plotter")

# Set dimension
Func_plot.geometry("600x400")

# Write info label
info_label = Label(Func_plot , text="Function Plotter",height=3,font=("Poppins",25))
info_label.pack(side=TOP)

# Create min x Min value"
min_x_label = Label(Func_plot , text="Min value",font=("Poppins",15))
min_x_label.pack()
min_x_label.place(x=100, y=140,width=100)

min_x = Entry()
min_x.pack()
min_x.place(x=100, y=180,height=30,width=100)

# Create max x 
min_x_label = Label(Func_plot , text="Max value",font=("Poppins",15))
min_x_label.pack()
min_x_label.place(x=400, y=140,width=100)

max_x = Entry()
max_x.pack()
max_x.place(x=400, y=180,height=30,width=100)
# Create input for function 
Func_label = Label(Func_plot , text="Function",font=("Poppins",20))
Func_label.pack()
Func_label.place(x=200, y=200,width=200)

Func = Entry()
Func.pack()
Func.place(x=200, y=240,height=50,width=200)


# Button for add plot action
btn_plot = Button(Func_plot,text="Plot", command=plot_function, font=("Poppins",15))
btn_plot.place(x=180, y=300, height=40, width=85)

# Button to exit the program
btn_exit = Button(Func_plot, text="Exit!", font=("Poppins",15), fg='red', command=exit)
btn_exit.place(x=330, y=300, height=40, width=85)

# Run app infinitely
Func_plot.mainloop()

