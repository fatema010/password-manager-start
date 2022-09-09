from tkinter import *
from tkinter import messagebox

from random import choice, randint, shuffle
# import pyperclip


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    # pyperclip.copy(password)


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't miss anything ")
    else:
        ask_information = messagebox.askokcancel(title=website,
                                                 message=f"Here are the information given:\nEmail:{email}"
                                                         f"\nPassword: {password} \n Do you want to save?")
    if ask_information:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website}|{email}|{password}\n")
            website_input.delete(0, END)
            password_input.delete((0, END))


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
image_pass = canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

label_one = Label(text="Website:")
label_one.grid(column=0, row=1)
label_two = Label(text="Email/Username:")
label_two.grid(column=0, row=2)
label_three = Label(text="Password:")
label_three.grid(column=0, row=3)

# Entry

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "hania.makuta@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# button
button = Button(text="Generate Password")
button.grid(column=2, row=3)
add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
