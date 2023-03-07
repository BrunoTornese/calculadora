from tkinter import *
from tkinter import ttk
import math

def ingresar(tecla): # funcion para ingresar los datos de la ventana
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla) # .set() es un metodo para modificar el valor de una variable y el .get() es un metodo para obtener el valor de una variable
    if tecla == '+' or tecla == '-' or tecla == '*' or tecla == '/':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')
        entrada2.set(entrada2.get() + tecla)

        entrada2.set('')

    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada1.set(resultado)

def raiz_cuadrada(): # funcion para calcular la raiz cuadrada
    entrada1.set('')
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)

def borrar(): # funcion para borrar los datos
    inicio = 0
    final = len(entrada2.get()) # obtiene la longitud del entrada 2
    entrada2.set(entrada2.get()[inicio:final-1])

def borrar_todo(): # funcion para borrar todo
    entrada1.set('')
    entrada2.set('')

def ingresar_teclado(event): # funcion para ingresar los datos de la ventana por el teclado
    tecla = event.char
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla) # .set() es un metodo para modificar el valor de una variable y el .get() es un metodo para obtener el valor de una variable
    if tecla == '+' or tecla == '-' or tecla == '*' or tecla == '/':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')
        entrada2.set(entrada2.get() + tecla)

        entrada2.set('')

    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada1.set(resultado)

root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1) # esta linea es para que el tamaño de la ventana sea 100%
root.rowconfigure(0, weight=1) # esta linea es para que el tamaño de la ventana sea 100%

#formato de la calculadora
estilos = ttk.Style()
estilos.configure("TFrame", background="#DBDBDB")
estilos.theme_use('clam')

mainframe = ttk.Frame(root, style='mainframe.TFrame')
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

estilos_label1 = ttk.Style()
estilos_label1.configure("Label.TLabel", font = 'arial 15', anchor='E')

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style= 'Label.TLabel') 
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W,N,E,S))

estilos_label2= ttk.Style()
estilos_label2.configure("Label.TLabel", font = 'arial 40', anchor='E')

entrada2 = StringVar()
laber_entrada2 = ttk.Label(mainframe,textvariable= entrada2,  style= 'Laber2.TLabel')
laber_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,N,E,S))

#estilos botones
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('Botones_numeros.TButton', font = 'arial 22', Widget=5, background='#ffffff', relief='flat')
estilos_botones_numeros.map('Botones_numeros.TButton', background=[('active', '#B9B9B9')])

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('Botones_borrar.TButton', font = 'arial 22', Widget = 6, relief='flat' , background='#CECECE')
estilos_botones_borrar.map('Botones_borrar.TButton',foreground=[('active', '#FF0000')], background=[('active', '#858585')])

estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure('Botones_restantes.TButton', font = 'arial 22', Widget = 6, relief='flat', background='#CECECE')
estilos_botones_restantes.map('Botones_restantes.TButton',background=[('active', '#858585')])

#creando los botones
button0 = ttk.Button(mainframe, text="0", style= 'Botones_numeros.TButton',command=lambda:ingresar('0'))
button1 = ttk.Button(mainframe, text="1", style= 'Botones_numeros.TButton',command=lambda:ingresar('1'))
button2 = ttk.Button(mainframe, text="2", style= 'Botones_numeros.TButton',command=lambda:ingresar('2'))
button3 = ttk.Button(mainframe, text="3", style= 'Botones_numeros.TButton',command=lambda:ingresar('3'))
button4 = ttk.Button(mainframe, text="4", style= 'Botones_numeros.TButton',command=lambda:ingresar('4'))
button5 = ttk.Button(mainframe, text="5", style= 'Botones_numeros.TButton',command=lambda:ingresar('5'))
button6 = ttk.Button(mainframe, text="6", style= 'Botones_numeros.TButton',command=lambda:ingresar('6'))
button7 = ttk.Button(mainframe, text="7", style= 'Botones_numeros.TButton',command=lambda:ingresar('7'))
button8 = ttk.Button(mainframe, text="8", style= 'Botones_numeros.TButton',command=lambda:ingresar('8'))
button9 = ttk.Button(mainframe, text="9", style= 'Botones_numeros.TButton',command=lambda:ingresar('9'))

#creando funcionalidad de los operadores
button_borrar = ttk.Button(mainframe, text= chr(9003), style= 'Botones_borrar.TButton', command= lambda: borrar())
button_borrar_todo = ttk.Button(mainframe, text= ('C'), style= 'Botones_borrar.TButton', command= lambda: borrar_todo())
button_parentesis1 = ttk.Button(mainframe, text= ('('), style= 'Botones_restantes.TButton',command=lambda:ingresar('('))
button_parentesis2 = ttk.Button(mainframe, text= (')'), style= 'Botones_restantes.TButton',command=lambda:ingresar(')'))
button_punto = ttk.Button(mainframe, text= '.', style= 'Botones_restantes.TButton',command=lambda:ingresar('.'))
button_division = ttk.Button(mainframe, text= chr(247), style= 'Botones_restantes.TButton',command=lambda:ingresar('/'))
button_multiplicaion = ttk.Button(mainframe, text='x', style= 'Botones_restantes.TButton',command=lambda:ingresar('*'))
button_rersta = ttk.Button(mainframe, text= '-', style= 'Botones_restantes.TButton',command=lambda:ingresar('-'))
button_suma = ttk.Button(mainframe, text= '+' , style= 'Botones_restantes.TButton',command=lambda:ingresar('+'))
button_igual = ttk.Button(mainframe, text='=', style= 'Botones_restantes.TButton',command=lambda:ingresar('='))
button_raiz_cuadrada = ttk.Button(mainframe, text='√', style= 'Botones_restantes.TButton',command=lambda:raiz_cuadrada('√'))

#colocando botones en pantalla
button_parentesis1.grid(column=0, row=2, sticky=((W,N,E,S)))
button_parentesis2.grid(column=1, row=2, sticky=((W,N,E,S)))
button_borrar_todo.grid(column=2, row=2, sticky=((W,N,E,S)))
button_borrar.grid(column=3, row=2, sticky=((W,N,E,S)))
button7.grid(column=0, row=3, sticky=((W,N,E,S)))
button8.grid(column=1, row=3, sticky=((W,N,E,S)))
button9.grid(column=2, row=3, sticky=((W,N,E,S)))
button_division.grid(column=3, row=3, sticky=((W,N,E,S)))
button4.grid(column=0, row=4, sticky=((W,N,E,S)))
button5.grid(column=1, row=4, sticky=((W,N,E,S)))
button6.grid(column=2, row=4, sticky=((W,N,E,S)))
button_multiplicaion.grid(column=3, row=4, sticky=((W,N,E,S)))
button1.grid(column=0, row=5, sticky=((W,N,E,S)))
button2.grid(column=1, row=5, sticky=((W,N,E,S)))
button3.grid(column=2, row=5, sticky=((W,N,E,S)))
button_suma.grid(column=3, row=5, sticky=((W,N,E,S)))
button0.grid(column=0, row=6, columnspan=2, sticky=(W,N,E,S))
button_punto.grid(column=2, row=6, sticky=((W,N,E,S)))
button_rersta.grid(column=3, row=6, sticky=((W,N,E,S)))
button_igual.grid(column=0, row=7, columnspan=3, sticky= (W,N,E,S))
button_raiz_cuadrada.grid(column=3, row=7, sticky=((W,N,E,S)))
# se agrega el , sticky=((W,N,E,S)) para hacer que el boton se muestre en toda la celda

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1) # acoomodo en la separacion de botones

root.bind('<Key>', ingresar_teclado)
root.mainloop()

                             
