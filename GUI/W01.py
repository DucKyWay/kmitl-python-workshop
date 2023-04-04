import tkinter

counter = 0 
def increase():
global counter
counter = counter + 1
label1.configure(text=counter)

def decrease():
global counter
counter = counter - 1
label1.configure(text=counter)

def reset():
global counter
counter = 0
label1.configure(text=counter)


window = tkinter.Tk()

window.title('Counter')
window.geometry("400x200")
window.resizable(False ,False )

label1 = tkinter.Label(text="0",
font=("Angsana New",30,"bold"),
fg="#000000")
label1.place(x=180,y=0)

btn1 = tkinter.Button(text="เพิ่มขึ้น",
font=("Angsana New",30,"bold"),
fg="#FFFFFF",bg="#00AA00",
command=increase)
btn1.place(x=0,y=50,height=50)

btn2 = tkinter.Button(text="ลดลง",font=("Angsana New",30,"bold"),
fg="#FFFFFF",bg="#990000",command=decrease)
btn2.place(x=100,y=50,height=50)

btn3 = tkinter.Button(text="รีเซ็ต",font=("Angsana New",30,"bold"),
fg="#FFFFFF",bg="gold",command=reset)
btn3.place(x=180,y=50,height=50)

window.mainloop() 