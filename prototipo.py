import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import ttk

def plot_function():
    global ax  

    slope = float(entry_slope.get())
    intercept = float(entry_intercept.get())

    x = np.linspace(-100, 100, 200)  
    y = slope * x + intercept  
   
    ax.clear()
    ax.set_xlim(-200, 200)
    ax.set_ylim(-200, 200)
    
    ax.plot(x, y, color=line_color.get())  
    ax.axhline(0, color=line_color.get(), lw=0.5)  
    ax.axvline(0, color=line_color.get(), lw=0.5)  
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Graph of y = mx + c')

    ax.grid(True)

    canvas.draw()

def on_entry_change(event):
    plot_function()

def toggle_dark_mode():
    bg_color = '#212121'
    fg_color = '#F2F2F2'
    entry_bg = '#424242'
    entry_fg = '#F2F2F2'
    button_bg = '#303030'
    button_fg = '#F2F2F2'

    if dark_mode.get() == 0:
        bg_color = '#F2F2F2'
        fg_color = 'black'
        entry_bg = '#EAEAEA'
        entry_fg = 'black'
        button_bg = '#F2F2F2'
        button_fg = 'black'

    style.configure('TEntry', fieldbackground=entry_bg, foreground=entry_fg)
    style.configure('TButton', background=button_bg, foreground=button_fg)
    root.config(bg=bg_color)
    label_slope.config(background=bg_color, foreground=fg_color)
    label_intercept.config(background=bg_color, foreground=fg_color)
    canvas.get_tk_widget().config(bg=bg_color)
    toolbar.config(bg=bg_color)

def invert_color(color):
   
    r, g, b = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
    inverted_r = 255 - r
    inverted_g = 255 - g
    inverted_b = 255 - b

    inverted_color = f"#{format(inverted_r, '02x')}{format(inverted_g, '02x')}{format(inverted_b, '02x')}"

    return inverted_color

def create_widgets():
    global label_slope, label_intercept, entry_slope, entry_intercept, canvas, toolbar, ax, line_color

    label_slope = ttk.Label(root, text='Slope (m):')
    label_slope.pack()
    entry_slope = ttk.Entry(root, width=15)
    entry_slope.pack()
    entry_slope.bind('<KeyRelease>', on_entry_change)

    label_intercept = ttk.Label(root, text='Intercept (c):')
    label_intercept.pack()
    entry_intercept = ttk.Entry(root, width=15)
    entry_intercept.pack()
    entry_intercept.bind('<KeyRelease>', on_entry_change)

    line_color_label = ttk.Label(root, text='Line Color:')
    line_color_label.pack()
    line_color = tk.StringVar(value='#000000') 
    line_color_entry = ttk.Entry(root, textvariable=line_color, width=15)
    line_color_entry.pack()
    line_color_entry.bind('<KeyRelease>', on_entry_change)

    plot_button = ttk.Button(root, text='Plot', command=plot_function)
    plot_button.pack()

    fig, ax = plt.subplots()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Graph of y = mx + c')
    ax.axhline(0, color=line_color.get(), lw=0.5)  
    ax.axvline(0, color=line_color.get(), lw=0.5) 
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    toolbar.pack()

root = tk.Tk()
root.title('Function Plotter')

style = ttk.Style()
style.configure('TEntry', padding=5, relief=tk.FLAT, foreground='black')
style.configure('TButton', padding=8, relief=tk.RAISED, foreground='black')

dark_mode = tk.IntVar(value=0)

create_widgets()

dark_mode_button = ttk.Checkbutton(root, text='Dark Mode', variable=dark_mode, command=toggle_dark_mode)
dark_mode_button.pack()

toggle_dark_mode()

root.mainloop()
