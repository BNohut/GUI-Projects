from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.label_score = Label(text=f"Score: 0", foreground="white", background=THEME_COLOR)
        self.label_score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250,  bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Questions display here",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, border=0, highlightthickness=0, command=self.is_true)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_img, border=0, highlightthickness=0, command=self.is_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR, text="You've reached the end of the quizler.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")



    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
            self.quiz.score += 1
            self.label_score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)
