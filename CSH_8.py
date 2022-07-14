import tkinter as tk
import tkinter.ttk as ttk

# Creates new window and assigned to variable
window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 4], minsize=100)

check = tk.Label(
    text="Are you sure you want to convert with these settings???",
    width=60,
    height=7
)

check.grid(row=0, column=0, sticky="n")



go_back = tk.Button(
    text="Go BACK!",
    width=25,
    height=5,
)
go_back.grid(row=4, column=0, sticky="w")

go_back = tk.Button(
    text="Yes!",
    width=25,
    height=5,
)
go_back.grid(row=4, column=0, sticky="e")

window.mainloop()
