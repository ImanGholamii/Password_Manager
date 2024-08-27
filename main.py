from tkinter import *

BACKGROUND = "#F1F8E8"
GEN_KEY_FG_COLOR = "#D8EFD3"
GEN_KEY_BG_COLOR = "#95D2B3"
ENTRY_BG = "#F7EFE5"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=50, bg=BACKGROUND)

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
canvas.grid_configure(row=0, column=1, pady=10, padx=10)

#  Labels
web_label = Label(text="Website:", font=(FONT_NAME, 10), bg=BACKGROUND, pady=10)
web_label.grid_configure(row=1, column=0)

email_username_label = Label(text="Email/Username:", font=(FONT_NAME, 10), bg=BACKGROUND, pady=10)
email_username_label.grid_configure(row=2, column=0)

password_label = Label(text="Password:", font=(FONT_NAME, 10), bg=BACKGROUND, pady=10)
password_label.grid_configure(row=3, column=0)

window.mainloop()
