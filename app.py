import tkinter as tk

def click(event):
    text = event.widget.cget("text") if event.widget else event.char  # Handle both button clicks and key presses
    if text == "=":
        try:
            result = str(eval(entry.get()))  # Evaluate the expression
            entry.delete(0, tk.END)         # Clear the entry field
            entry.insert(tk.END, result)   # Display the result
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")  # Handle invalid inputs
    elif text == "C":
        entry.delete(0, tk.END)            # Clear the entry field
    else:
        entry.insert(tk.END, text)         # Add the input (button or key) to the entry field

def key_press(event):
    valid_keys = "0123456789+-*/=C"  # Define valid keys
    if event.char in valid_keys or event.keysym == "Return":
        click(event)

# Set up the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry field for user input
entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.SUNKEN, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8)

# Create button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Generate buttons dynamically
button_frame = tk.Frame(root)
button_frame.pack()

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(side=tk.TOP, fill=tk.BOTH)
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font="Arial 18", height=2, width=5)
        button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        button.bind("<Button-1>", click)  # Bind click events to buttons

# Bind keyboard keys
root.bind("<Key>", key_press)

# Run the application
root.mainloop()
