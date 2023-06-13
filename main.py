from tkinter import Tk, Label, Frame, Button, LEFT, W
import calendar
import datetime
from tkinter import PhotoImage

calendario = Tk()
calendario.title('Calendar') #titulo de ventana
#ventana
calendario.geometry('580x900') #tamaño de ventana
calendario.resizable(False, False)
calendario.minsize(width=500, height=800)

#transparencia
calendario.attributes('-alpha', 0.9) # 0-transparente 1-opaco

#icono de ventana
image_icon = PhotoImage(file="calicono.png")
calendario.iconphoto(False, image_icon)

#imagen de cel
background = PhotoImage(file="fondo.png")

#etiqueta bg
etiqueta = Label(calendario, image=background)
etiqueta.place(x=0, y=0, relwidth=1, relheight=1)

year = datetime.date.today().year
month =datetime.date.today().month

def crearcalendario(_year, __month_):
    str1 = calendar.month(year, month)
    label1.configure(text=str1)

def mesanterior():
    global month, year
    month -=1
    if month == 0:
        month = 12
        year -= 1
    crearcalendario(year, month)

def messiguiente():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1
    crearcalendario(year, month)

#etiqueta Calendar
etiquetacalendario = Label(calendario, text="CALENDAR", font = ['courier', 40])

#etiqueta del formato del calendario
label1 = Label(calendario, text="", font=['courier', 35], justify=LEFT)
label1.grid(row=1, column=1, pady=150, padx=7)

#boton antes con formato
frame = Frame(calendario, bd=10)
antes = Button(frame, text="Antes", command=mesanterior, font=['courier', 15], bg="pink", fg="red")
antes.grid(row=1, column=1, sticky=W)

#boton después con formato
despues = Button(frame, text="Después", command=messiguiente, font=['courier', 15], bg="pink", fg="red")
despues.grid(row=1, column=2)
frame.grid(row=2, column=1)
crearcalendario(year, month)

calendario.mainloop()
