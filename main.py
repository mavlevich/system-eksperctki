from tkinter import *
from system import *

window = Tk()
window.title("System ekspertcki")
window.geometry('500x250')


def clicked_oblicz():
    if (progonza.CzyBędziePada_Deszcz() == True):
        btn1.configure(text="True")
    if (progonza.CzyBędziePada_Deszcz() == False):
        btn1.configure(text="False")

    if (progonza.CzyBędziePada_Snieg() == True):
        btn2.configure(text="True")
    if (progonza.CzyBędziePada_Snieg() == False):
        btn2.configure(text="False")

    if (progonza.CzySloneczna() == True):
        btn3.configure(text="True")
    if (progonza.CzySloneczna() == False):
        btn3.configure(text="False")

    if (progonza.CzyBedzieMgła() == True):
        btn4.configure(text="True")
    if (progonza.CzyBedzieMgła() == False):
        btn4.configure(text="False")

    if (progonza.CzyBedzieSmog() == True):
        btn5.configure(text="True")
    if (progonza.CzyBedzieSmog() == False):
        btn5.configure(text="False")

    if (progonza.CzyBiometrKorzystny() == True):
        btn6.configure(text="True")
    if (progonza.CzyBiometrKorzystny() == False):
        btn6.configure(text="False")


def clicked_zresetuj():
    btn1.configure(text="")
    btn2.configure(text="")
    btn3.configure(text="")
    btn4.configure(text="")
    btn5.configure(text="")
    btn6.configure(text="")


btn = Button(window, text="Oblicz", height=1, width=10, command=clicked_oblicz)
btn.grid(column=1, row=0)
btn = Button(window, text="Zresetuj", height=1, width=10, command=clicked_zresetuj)
btn.grid(column=1, row=1)

btn1 = Button(window, text="Czy będzie padać deszcz ?", height=1, width=25)
btn1.grid(column=2, row=0)
btn1 = Button(window, text="", height=1, width=10)
btn1.grid(column=3, row=0)

btn2 = Button(window, text="Czy będzie padać śnieg ?", height=1, width=25)
btn2.grid(column=2, row=1)
btn2 = Button(window, text="", height=1, width=10)
btn2.grid(column=3, row=1)

btn3 = Button(window, text="Czy będzie pogoda słonieczna ?", height=1, width=25)
btn3.grid(column=2, row=2)
btn3 = Button(window, text="", height=1, width=10)
btn3.grid(column=3, row=2)

btn4 = Button(window, text="Czy będzie mgła ?", height=1, width=25)
btn4.grid(column=2, row=3)
btn4 = Button(window, text="", height=1, width=10)
btn4.grid(column=3, row=3)

btn5 = Button(window, text="Czy będzie smog ?", height=1, width=25)
btn5.grid(column=2, row=4)
btn5 = Button(window, text="", height=1, width=10)
btn5.grid(column=3, row=4)

btn6 = Button(window, text="Czy biometr korzystny?", height=1, width=25)
btn6.grid(column=2, row=5)
btn6 = Button(window, text="", height=1, width=10)
btn6.grid(column=3, row=5)


window.mainloop()


