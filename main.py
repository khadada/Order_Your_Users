from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count_down():
    global reps
    reps+=1
    if reps % 2== 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text=" 'S' relax session")

    elif reps % 8== 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text=" 'L' relax session")
       
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work session")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minuts = math.floor(count/60)
    seconds = count % 60
    if minuts < 10:
        minuts = f'0{minuts}'
    if seconds < 10:
        seconds = f'0{seconds}'
    canvas.itemconfig(text_canvas, text=f'{minuts}:{seconds}')
    if count > 0:
        root.after(1000,count_down, count-1)
        print(count)
    else:
        start_count_down()
        marks = ""
        mark_session = math.floor(reps/2)
        for _ in range(mark_session):
            marks+="✓"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.config(padx=100,pady=100)
root.title('Success organistion of the time for users')

img = PhotoImage(file='tomato.png')
canvas = Canvas(root, width=200,height=230,highlightthickness=0)
canvas.grid(column=1,row=1)
canvas.create_image(100,115, image=img)
text_canvas = canvas.create_text(100,135,fill='#fff',text='00:00',font=(FONT_NAME,30,'bold'))

timer_label = Label(text='Timer',font=(FONT_NAME,30,'normal'),fg=GREEN)
timer_label.grid(row=0,column=1)


check_marks = Label(font=(FONT_NAME,30,'normal'),fg=GREEN)
check_marks.grid(row=3,column=1)




start_btn = Button(text='Start',pady=5,padx=9,command=start_count_down)
start_btn.grid(row=2,column=0)
reset_btn = Button(text='Rest',pady=5,padx=9)
reset_btn.grid(row=2,column=2)


root.mainloop()