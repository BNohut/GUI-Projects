from tkinter import messagebox
from tkinter import *
from random import choice, shuffle, randint
import pyperclip
import json


# --------------------------- DELETED CODE FOR SEARCH -------------------- #
# data_websites = [key for key, value in data.items()]
# if website in data_websites:
#     email = data[website]["email"]
#     password = data[website]["password"]
#     messagebox.showinfo(title="Yey!",
#                         message=f"You have already an account on {website}. Information are:\n"
#                         f"E-Mail/ Username: {email}\nPassword: {password}")
# else:
#     messagebox.showinfo(title="Oops!", message=f"You have not any account on {website}")

# ---------------------------- SEARCH VALUE ------------------------------- #
def search():
    website = website_entry.get().title()
    if website == "":
        messagebox.showinfo(title="Oops!", message="You should entry a website name.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Oops!", message="There is not any .json data file.")
        else:
            try:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title="Yey!",
                                    message=f"You have already an account on {website}. Information are:\n"
                                            f"E-Mail/ Username: {email}\nPassword: {password}")
            except KeyError:
                messagebox.showinfo(title="Oops!", message=f"You have not any account on {website}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    char_list = [choice(letters) for _ in range(randint(0, 10))]
    num_list = [choice(numbers) for _ in range(randint(2, 4))]
    sym_list = [choice(symbols) for _ in range(randint(2, 4))]

    pass_list = char_list + num_list + sym_list
    shuffle(pass_list)

    password = "".join(pass_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().title()
    username = username_entry.get()
    password_user = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password_user
        }
    }
    print(new_data)

    if website == "" or username == "" or password_user == "":
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
background = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background, anchor='c')
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)

email_label = Label(text="E-Mail/UserName")
email_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

website_entry = Entry(width=24)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=42)
username_entry.insert(0, "your_email@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

generate_pass_button = Button(text="Generate Password", command=password_generator)
generate_pass_button.grid(column=2, row=3)

add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1)
window.mainloop()
