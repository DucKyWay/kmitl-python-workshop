import tkinter as tk

root = tk.Tk()
root.title("Grade Calculator")
root.geometry("400x200")
root.resizable(False, False)

label1 = tk.Label(root, text="Enter your score:")
label1.pack(pady=10)

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="")
label2.pack(pady=10)

def calculate_grade():
    score = int(entry1.get())
if score < 0 or score > 100:
    label2.config(text="Error")
elif score < 50:
    label2.config(text="F")
elif score < 60:
    label2.config(text="D")
elif score < 70:
    label2.config(text="C")
elif score < 80:
    label2.config(text="B")
else:
    label2.config(text="A")