import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.SUNKEN, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(side=tk.TOP, fill=tk.BOTH)
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font="Arial 18", height=2, width=5)
        button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        button.bind("<Button-1>", click)

root.mainloop()