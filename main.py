from tkinter import *

BACKGROUND = "#D6DAC8"
GEN_KEY_COLOR = "#FBF3D5"
ENTRY_BG = "#F7EFE5"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(width=500, height=350, bg=BACKGROUND)

# Grid system
rows = 5
columns = 3
for row in range(rows):
    window.grid_rowconfigure(index=row, weight=1)

for col in range(columns):
    window.grid_columnconfigure(index=col, weight=1)





window.mainloop()
