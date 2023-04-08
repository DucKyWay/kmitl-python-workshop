import tkinter as tk

class GradeCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Grade Calculator")
        self.root.geometry("400x200")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text="Enter score:")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.button.pack()

        self.result = tk.Label(self.root, text="")
        self.result.pack()

        self.root.mainloop()

    def calculate(self):

        score = self.entry.get()

        if score == "":
            self.result.config(text="Error: Please enter a score.")
        else:
            score = int(score)
            if score < 0 or score > 100:
                self.result.config(text="Error: Score must be between 0 and 100.")
            elif score < 50:
                self.result.config(text="Grade F")
            elif score < 60:
                self.result.config(text="Grade D")
            elif score < 70:
                self.result.config(text="Grade C")
            elif score < 80:
                self.result.config(text="Grade B")
            else:
                self.result.config(text="Grade A")

GradeCalculator()
