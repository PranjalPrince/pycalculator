import tkinter as tk
from tkinter import ttk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        if isinstance(result, float):
            result = format(result, '.10f')  # Limit decimal precision
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

# Create the Tkinter root window
root = tk.Tk()
root.title("Calculator")
root.geometry("270x300")
root.configure(bg="#F2F2F2")

# Create a style for buttons
button_style = ttk.Style()
button_style.configure("TButton", font=("Arial", 12), width=5, background="#E0E0E0")

# Create an entry field for displaying the result
entry = tk.Entry(root, width=20, font=("Arial", 16), justify="right", bg="#FFFFFF")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 3)
]

for button_text, row, col in buttons:
    button = ttk.Button(root, text=button_text, style="TButton",
                        command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=col, padx=5, pady=5)

# Create a clear button
clear_button = ttk.Button(root, text="Clear", style="TButton",
                          command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Create an equal button
equal_button = ttk.Button(root, text="=", style="TButton",
                          command=button_equal)
equal_button.grid(row=4, column=2, padx=5, pady=5)

# # Create a division button
# division_button = ttk.Button(root, text="/", style="TButton",
#                              command=lambda: button_click("/"))
# division_button.grid(row=5, column=3, padx=5, pady=5)

# Create a backspace button
backspace_button = ttk.Button(root, text="⌫", style="TButton",
                              command=button_backspace)
backspace_button.grid(row=5, column=1,columnspan=2 , padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()