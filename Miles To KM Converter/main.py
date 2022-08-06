from tkinter import *

window = Tk()
window.title("Coding is Magic Tho")
window.config(pady=20, padx=20)


def calculate():
    user_miles = float(inp.get())
    calc_km = round(user_miles * 1.609344, 2)
    label_result["text"] = calc_km


label_miles = Label(text="Miles")
label_miles.grid(column=2, row=2)
label_is_equal = Label(text="is equal to")
label_is_equal.grid(column=0, row=3)
label_result = Label(text=0)
label_result.grid(column=1, row=3)
label_km = Label(text="Km")
label_km.grid(column=2, row=3)

inp = Entry(width=7)
inp.grid(column=1, row=2)

my_button = Button(text="Calculate", width=10, command=calculate)
my_button.grid(column=1, row=4)

window.mainloop()
