from tkinter import *
import tkinter

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125, text='Some Question Text', font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        right_button_photo = PhotoImage(file='./images/true.png')
        wrong_button_photo = PhotoImage(file='./images/false.png')
        self.right_button = Button(
            image=right_button_photo, highlightthickness=0)
        self.wrong_button = Button(
            image=wrong_button_photo, highlightthickness=0)
        self.right_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)

        self.window.mainloop()
