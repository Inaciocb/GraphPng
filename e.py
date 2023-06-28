import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import ttk

def plot_function():
    global ax  # Make ax a global variable

    slope = float(entry_slope.get())
    intercept = float(entry_intercept.get())

    x = np.linspace(-100, 100, 200)  # Generate 200 x-values from -100 to 100
    y = slope * x + intercept  # Define the linear function y = mx + c
    
    # Clear the previous plot
    ax.clear()

    # Set the plot limits to cover a larger range
    ax.set_xlim(-200, 200)
    ax.set_ylim(-200, 200)
    
    ax.plot(x, y, color=line_color.get())  # Use the chosen line color
    ax.axhline(0, color=line_color.get(), lw=0.5)  # Add horizontal line at y = 0
    ax.axvline(0, color=line_color.get(), lw=0.5)  # Add vertical line at x = 0
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Graph of y = mx + c')

    # Draw grid lines
    ax.grid(True)

    canvas.draw()

def on_entry_change(event):
    plot_function()

def toggle_dark_mode():
    # Dark mode color scheme
    bg_color = '#212121'
    fg_color = '#F2F2F2'
    entry_bg = '#424242'
    entry_fg = '#F2F2F2'
    button_bg = '#303030'
    button_fg = '#F2F2F2'

    # Light mode color scheme
    if dark_mode.get() == 0:
        bg_color = '#F2F2F2'
        fg_color = 'black'
        entry_bg = '#EAEAEA'
        entry_fg = 'black'
        button_bg = '#F2F2F2'
        button_fg = 'black'

    # Configure the style with the selected color scheme
    style.configure('TEntry', fieldbackground=entry_bg, foreground=entry_fg)
    style.configure('TButton', background=button_bg, foreground=button_fg)
    root.config(bg=bg_color)
    label_slope.config(background=bg_color, foreground=fg_color)
    label_intercept.config(background=bg_color, foreground=fg_color)
    canvas.get_tk_widget().config(bg=bg_color)
    toolbar.config(bg=bg_color)

def invert_color(color):
    # Convert color to RGB format
    r, g, b = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))

    # Invert the color by subtracting each RGB component from 255
    inverted_r = 255 - r
    inverted_g = 255 - g
    inverted_b = 255 - b

    # Convert the inverted RGB components back to hexadecimal
    inverted_color = f"#{format(inverted_r, '02x')}{format(inverted_g, '02x')}{format(inverted_b, '02x')}"

    return inverted_color

def create_widgets():
    global label_slope, label_intercept, entry_slope, entry_intercept, canvas, toolbar, ax, line_color

    # Create the slope label and entry field
    label_slope = ttk.Label(root, text='Slope (m):')
    label_slope.pack()
    entry_slope = ttk.Entry(root, width=15)
    entry_slope.pack()
    entry_slope.bind('<KeyRelease>', on_entry_change)

    # Create the intercept label and entry field
    label_intercept = ttk.Label(root, text='Intercept (c):')
    label_intercept.pack()
    entry_intercept = ttk.Entry(root, width=15)
    entry_intercept.pack()
    entry_intercept.bind('<KeyRelease>', on_entry_change)

    # Create the line color label and entry field
    line_color_label = ttk.Label(root, text='Line Color:')
    line_color_label.pack()
    line_color = tk.StringVar(value='#000000')  # Default color is black
    line_color_entry = ttk.Entry(root, textvariable=line_color, width=15)
    line_color_entry.pack()
    line_color_entry.bind('<KeyRelease>', on_entry_change)

    # Create the plot button
    plot_button = ttk.Button(root, text='Plot', command=plot_function)
    plot_button.pack()

    # Create a figure and axis for the plot
    fig, ax = plt.subplots()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Graph of y = mx + c')
    ax.axhline(0, color=line_color.get(), lw=0.5)  # Add horizontal line at y = 0
    ax.axvline(0, color=line_color.get(), lw=0.5)  # Add vertical line at x = 0
    ax.grid(True)

    # Create a Tkinter canvas for the plot
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    # Create a toolbar with zoom functionality
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    toolbar.pack()

root = tk.Tk()
root.title('Function Plotter')

# Configure the style for dark mode
style = ttk.Style()
style.configure('TEntry', padding=5, relief=tk.FLAT, foreground='black')
style.configure('TButton', padding=8, relief=tk.RAISED, foreground='black')

dark_mode = tk.IntVar(value=0)

create_widgets()

# Create a dark mode toggle button
dark_mode_button = ttk.Checkbutton(root, text='Dark Mode', variable=dark_mode, command=toggle_dark_mode)
dark_mode_button.pack()

toggle_dark_mode()  # Apply initial color scheme based on dark mode state

root.mainloop()
