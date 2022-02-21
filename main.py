from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_entry = f"{website} | {email} | {password}\n"

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="You must enter all fields")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details:\nWebsite: "
                                                                f"{website}\nEmail/Username: {email}\nPassword: "
                                                                f"{password}\nIs this correct?")
        if is_okay:
            with open("data.txt", mode="a") as password_file:
                password_file.write(new_entry)
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title = "Password Manager"
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("arial", 12))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=("arial", 12))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("arial", 12))
password_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2, sticky='w')

email_input = Entry(width=35)
email_input.insert(0, "example@example.com")
email_input.grid(column=1, row=2, columnspan=2, sticky='w')

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky='w')

generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3, sticky='w')

add_btn = Button(text="Add", width=36, command=add_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()


