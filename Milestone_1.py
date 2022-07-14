import tkinter as tk
import tkinter.ttk as ttk

# Creates new window and assigned to variable
window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 8], minsize=100)

greeting = tk.Label(
    text="Welcome to Milestone 1!",
    width=20,
    height=3
)

greeting.grid(row=0, column=0, sticky="n")

instructions = tk.Label(
    text=" CLICK for INSTRUCTIONS",
    width=60,
    height=4,
    bg="white",
    fg="black"

)

instructions.grid(row=1, column=0, sticky="e")

auto = tk.Button(
    text="AUTO",
    width=15,
    height=1,
)
auto.grid(row=2, column=0, sticky="ne")


convert = tk.Button(
    text="Convert",
    width=25,
    height=5,
)
convert.grid(row=2, column=0, sticky="s")

clear = tk.Button(
    text="Clear",
    width=25,
    height=5,
)

clear.grid(row=3, column=0, sticky="s")

previous_button = tk.Button(

    text="CLICK for Previous CONVERSION",
    width=25,
    height=5,
    bg="red",
    fg="white",

)
previous_button.grid(row=1, column=0, sticky="w")

current_button = tk.Button(

    text="input original currency here",
    width=25,
    height=5,
    bg="black",
    fg="orange",

)
current_button.grid(row=3, column=0, sticky="sw")

frame_e = tk.Frame()
input_entry = tk.Entry(
    width=50)
input_entry.grid(row=2, column=0, sticky="w")

input_amount = input_entry.get()

frame_f = tk.Frame()
desired_button = tk.Button(
    text="output",
    width=25,
    height=5,
    bg="black",
    fg="orange",
)
desired_button.grid(row=3, column=0, sticky="e")

frame_g = tk.Frame()
output = tk.Entry(
    width=50)
output.grid(row=2, column=0, sticky="e")

output.insert(0, "Output amount" + input_amount)


history_button = tk.Button(
    text="CLICK for MORE INFO ",
    width=27,
    height=5,
    bg="black",
    fg="green",
)
history_button.grid(row=6, column=0, sticky="n")

frame_h = tk.Frame()
input_history = tk.Label(text="INPUT INFO:'The Coinage Act of 1792 introduced the U.S. dollar at par with the Spanish "
                "silver dollar, divided it into 100 cents, and authorized the minting of coins denominated in dollars "
                "and cents. U.S. banknotes are issued in the form of Federal Reserve Notes,popularly called greenbacks "
                "due to their predominantly green color.'")

input_history.grid(row=7, column=0, sticky="n")
input_history = tk.Label(text="OUTPUT INFO")

input_history.grid(row=8, column=0, sticky="w")

# Place at the end of the program code. Tells python to tun the Tkinter event loop
window.mainloop()
