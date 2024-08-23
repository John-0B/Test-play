import tkinter as tk
from search import *

name = 'zero'
age = int


def find():
    global name
    names = list(dict1.keys())
    for i in range(len(names)):
        if name.casefold() in dict1[names[i]]:
            name = names[i]
            return name, ans1()
        else:
            ans1()


def result():

    def start():
        print4.destroy()
        button4.destroy()
        return answer()
    global name, age
    win.geometry('425x200')
    year = 2024
    day_b = year - int(age)
    print4 = tk.Label(win, text=f'{name.capitalize()}, вы родились в {day_b}', background='skyblue')
    print4.place(x=5, y=50)
    button4 = tk.Button(win, text='В начало', background='lightskyblue', command=start)
    button4.place(x=5, y=75)


def ans1():
    win.geometry('425x200')
    global name

    def age1():
        global age
        age = age_e.get()
        age_e.destroy()
        print3.destroy()
        button3.destroy()
        return age, result()

    print3 = tk.Label(win, text=f'{name.capitalize()}, cколько вам исполнится или исполнилось лет в этом году ?',
                      background='skyblue')
    print3.place(x=5, y=50)
    button3 = tk.Button(win, text='Ответить', background='lightskyblue', command=age1)
    button3.place(x=95, y=75)
    age_e = tk.Entry(win, width=13)
    age_e.place(x=5, y=78)


def answer():
    def entr1():
        global name
        name = name_e.get()
        name_e.destroy()
        print2.destroy()
        button2.destroy()
        return name, find()

    win.geometry('200x200')
    print1.destroy()
    button1.destroy()
    print2 = tk.Label(win, text='Как ваше имя?', background='skyblue')
    print2.place(x=55, y=50)
    name_e = tk.Entry(win, width=13)
    name_e.place(x=56, y=75)
    button2 = tk.Button(win, text='Ответить', background='lightskyblue', command=entr1)
    button2.place(x=70, y=150)


win = tk.Tk()
win.title('Test')
win.geometry('200x200')
win.configure(bg="skyblue")
win.resizable(False, False)
button1 = tk.Button(win, text='Привет', background='lightskyblue', command=answer)
button1.place(x=75, y=150)
print1 = tk.Label(win, text='Привет, я Test', background='skyblue')
print1.place(x=55, y=50)
win.mainloop()
