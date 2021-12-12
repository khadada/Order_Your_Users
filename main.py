from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.config(padx=100,pady=100)
root.title('Success organistion of the time for users')
img = PhotoImage(file='tomato.png')
canvas = Canvas(root, width=200,height=230,highlightthickness=0)
canvas.grid(column=0,row=0)
canvas.create_image(100,115, image=img)
canvas.create_text(100,135,fill='#fff',text='00:00',font=(FONT_NAME,30,'bold'))
root.mainloop()