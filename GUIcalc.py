from tkinter import *
from tkinter import colorchooser
import tkinter as tk



def click_button(value):
    entry.insert(END, value)

def submit():
    try:
        expression = entry.get()
        result = eval(expression)  # Вычисляет выражение
        entry.delete(0, tk.END)  # Очищает поле ввода
        entry.insert(tk.END, str(result))  # Выводит результат
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

def color():
    window.config(bg=colorchooser.askcolor()[1])

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()
window.geometry("720x600")
window.title("Calcuator")

entry = Entry(window,font=("Arial",50))
entry.place(x=350)

button_1 = Button(window,text="1",command=lambda: click_button("1"),padx=20,pady=20)
button_1.place(x=25,y=0)

button_2 = Button(window,text="2",command=lambda: click_button("2"),padx=20,pady=20)
button_2.place(x=75,y=0)

button_3 = Button(window,text="3",command=lambda: click_button("3"),padx=20,pady=20)
button_3.place(x=125,y=0)

button_4 = Button(window,text="4",command=lambda: click_button("4"),padx=20,pady=20)
button_4.place(x=25,y=55)

button_5 = Button(window,text="5",command=lambda: click_button("5"),padx=20,pady=20)
button_5.place(x=75,y=55)

button_6 = Button(window,text="6",command=lambda: click_button("6"),padx=20,pady=20)
button_6.place(x=125,y=55)

button_7 = Button(window,text="7",command=lambda: click_button("7"),padx=20,pady=20)
button_7.place(x=25,y=110)

button_8 = Button(window,text="8",command=lambda: click_button("8"),padx=20,pady=20)
button_8.place(x=75,y=110)

button_9 = Button(window,text="9",command=lambda: click_button("9"),padx=20,pady=20)
button_9.place(x=125,y=110)

button_0 = Button(window,text="0",command=lambda: click_button("0"),padx=20,pady=20)
button_0.place(x=75,y=170)

button_plus = Button(window,text="+",command=lambda: click_button("+"),padx=20,pady=20)
button_plus.place(x=100,y=300)

button_minus = Button(window,text="-",command=lambda: click_button("-"),padx=20,pady=20)
button_minus.place(x=150,y=300)

button_multiply = Button(window,text="*",command=lambda: click_button("*"),padx=20,pady=20)
button_multiply.place(x=200,y=300)

button_divide = Button(window,text="/",command=lambda: click_button("/"),padx=20,pady=20)
button_divide.place(x=250,y=300)

button_degree = Button(window,text="**",command=lambda: click_button("**"),padx=20,pady=20)
button_degree.place(x=300,y=300)

button_withdraw = Button(window,text="=",command=submit,padx=20,pady=20)
button_withdraw.place(x=350,y=300)

button = Button(window,text="Change color of background",command=color)
button.pack(side=BOTTOM)

button_del = Button(window,text="delete",command= delete,padx=20,pady=20)
button_del.place(x=400,y=300)

button_back = Button(window,text="backspace",command=backspace,padx=20,pady=20)
button_back.place(x=475,y=300)

window.mainloop()