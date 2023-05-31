from tkinter import *
from random import choice
BACKGROUND = "#FFF6BD"
FONT = "#A8D1D1"
WORD_COLOR = "#FD8A8A"
TITLE = "#86C8BC"
BUTTON = "#FFD4B2"
FONT_NAME = "Courier"
seconds = 0

user_words = []


def display_words(e):
    if seconds !=0 :
        if seconds != 59:
            user_words.append(word_input.get())
        word_input.delete(0, END)
        word_input.focus_set()
        with open(file='assets/words.csv', mode='r') as words:
            list = words.readlines()
        word_list = [word.replace('\n', '').lower() for word in list]
        word_display.config(text=choice(word_list))
    if seconds == 0:
        count = len(user_words)
        word_display.config(text=f"Your wpm score is {count}")


def start_timer():
    count_down(59)
    display_words('e')


def count_down(count):
    global seconds, timer
    seconds = count
    second = str(count)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
        timer_label.config(text=second)
    if count < 10:
        timer_label.config(text=f"0{second}")
    elif count == 0:
        timer_label.config(text="00")


window = Tk()
window.title('Typing speed Test')
window. config(height=600, width=600, padx=30, pady=30, bg=BACKGROUND)
title_label = Label(text='Typing Speed Text', bg=BACKGROUND, font=(FONT_NAME, 36, 'bold'), fg=TITLE)
title_label.grid(row=0, column=1, columnspan=3, pady=20)
timer_label = Label(text='1: 00', bg=BACKGROUND, font=(FONT_NAME, 18, 'normal'), fg=FONT)
timer_label.grid(row=1, column=2)
word_input = Entry(width=80)
word_input.focus_set()
word_input.grid(row=3, column=2, pady=10)
word_display = Label(text='Words will display here', bg=BACKGROUND, font=(FONT_NAME, 16, 'normal'), fg=WORD_COLOR)
word_display.grid(row=2, column=2)
button = Button(text='Start', command=start_timer, bg=BUTTON, fg=WORD_COLOR, font=(FONT_NAME, 12, 'normal'))
button.grid(row=4, column=2)
window.bind('<space>', display_words)


window.mainloop()
