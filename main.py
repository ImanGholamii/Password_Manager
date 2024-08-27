from tkinter import *

BACKGROUND = "#F1F8E8"
KEY_BG_COLOR = "#D9EDBF"
KEY_ACTIVE_BG_COLOR = "#90D26D"
ENTRY_BG = "#F7EFE5"
FONT_NAME = "Courier"
FILE_NAME = "data.txt"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    text = f"{web_entry.get()} | {email_username_entry.get()} | {password_entry.get()}\n"
    with open(file=FILE_NAME, mode="a") as file:
        file.write(text)
    web_entry.delete(first=0, last=len(web_entry.get()))
    email_username_entry.delete(first=0, last=len(email_username_entry.get()))
    password_entry.delete(first=0, last=len(password_entry.get()))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND)
window.minsize(670, 470)
window.maxsize(670, 470)

# Grid system
rows = 5
columns = 3
for row in range(rows):
    window.grid_rowconfigure(index=row, weight=1)

for col in range(columns):
    window.grid_columnconfigure(index=col, weight=1)

# Photo
canvas = Canvas(width=200, height=200, background=BACKGROUND, highlightthickness=0)
my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid_configure(row=0, column=1, columnspan=2, pady=10, padx=10)

#  Labels
web_label = Label(text="Website:", font=(FONT_NAME, 12), bg=BACKGROUND, pady=10)
web_label.grid_configure(row=1, column=0)

email_username_label = Label(text="Email/Username:", font=(FONT_NAME, 12), bg=BACKGROUND, pady=10)
email_username_label.grid_configure(row=2, column=0)

password_label = Label(text="Password:", font=(FONT_NAME, 12), bg=BACKGROUND, pady=10)
password_label.grid_configure(row=3, column=0)

# Entries
web_entry = Entry(width=50, bg=ENTRY_BG)
web_entry.grid_configure(row=1, column=1, columnspan=2)
web_entry.focus()

pre_email = "Example@gmail.com"  # if You use One email always you can set it or Not
email_username_entry = Entry(width=50, bg=ENTRY_BG)
email_username_entry.grid_configure(row=2, column=1, columnspan=2)
email_username_entry.insert(index=0, string=pre_email)

password_entry = Entry(width=20, bg=ENTRY_BG)
password_entry.grid_configure(row=3, column=1, columnspan=1, padx=20)

# Button
pass_gen_btn = Button(text="Generate Password", bg=KEY_BG_COLOR, activebackground=KEY_ACTIVE_BG_COLOR, bd=0,
                      highlightthickness=0)
pass_gen_btn.grid_configure(row=3, column=2, columnspan=1, padx=20)

add_btn = Button(text="Add", bg=KEY_BG_COLOR, activebackground=KEY_ACTIVE_BG_COLOR, width=42, bd=1,
                 highlightthickness=1, command=save)
add_btn.grid_configure(row=4, column=1, columnspan=2)

window.mainloop()
