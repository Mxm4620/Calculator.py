from tkinter import *

count = ""

def submit():
    username = entry.get()
    print(username)

def click(num):
    entry.insert(Tk.END, num)

window = Tk()

entry = Entry(window,bg="black")
entry.pack()

button_submit = Button(window,text="=",command=submit)
button_submit.pack()

button_1 = Button(window,text="1",command=lambda: 1)
button_1.pack(side=LEFT)
window.mainloop()