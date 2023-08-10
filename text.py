#from tkinter import *

#def func():
    ##global k
    ##k += 1
    #label['text'] += 1

#k = 0
#window = Tk()
#height = window.winfo_screenheight()
#width = window.winfo_screenwidth()

#h=300
#w=400

#window.geometry(f'{w}x{h}+{(width-w)//2}+{(height-h)//2}')
#window.title('моя программа')

#label = Label(text='Мой текст', font=16, bg='#03fcfc', fg='black')
#label.place(x=100, y=100)

#btn = Button(text=0, font='16', bg='white', fg='gold', command=func)
#btn.place(x=200, y=200)

#window.mainloop()

from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today().strftime('%')

window = Tk()
height = window.winfo_screenheight()
width = window.winfo_screenwidth()

h=300
w=400

window.geometry(f'{w}x{h}+{(width-w)//2}+{(height-h)//2}')
window.title('Курс валют MAXI банк')

img = PhotoImage(file='logo.png')
logo = Label(image=img)
logo.place(x=0, y=0)

label = Label(text='Курс валют',font='Arial 22')
label.place(x=180, y=25)

course_info = Label(text=f"Курс на {today.replace('/', '.')}",font='Arial 18')
course_info.place(x=100, y=150)


window.mainloop()

