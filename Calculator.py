import tkinter as tk

def on_button_click(event):
    current = result_var.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif text == "C":
        result_var.set("")
    else:
        result_var.set(current + text)

root = tk.Tk()
root.title("thatguyaman's Calculator")
root.geometry("600x650")

result_var = tk.StringVar()

result_entry = tk.Entry(root, textvariable=result_var, font="Helvetica 20", bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
result_entry.pack(fill=tk.BOTH, expand=True)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()

    for button_text in row:
        button = tk.Button(frame, text=button_text, font="Helvetica 16", padx=20, pady=20, bd=4, relief=tk.RAISED)
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        button.bind("<Button-1>", on_button_click)

root.mainloop()