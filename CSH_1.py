import tkinter as tk
import tkinter.ttk as ttk

# Creates new window and assigned to variable
window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 4], minsize=100)

greeting = tk.Label(
    text="NEW FEATURE",
    width=20,
    height=3
)

greeting.grid(row=0, column=0, sticky="n")

line_1 = tk.Label(
    text="You can now convert to 5 additional currencies using the"
         "drop down list.",
    width=60,
    height=3
)
line_1.grid(row=2, column=0, sticky="n")

convert = tk.Button(
    text="OK!",
    width=25,
    height=5,
)
convert.grid(row=4, column=0, sticky="n")

window.mainloop()
