from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title("Calculadora")
root.geometry("+500+80")

#formato de la calculadora
estilos = ttk.Style()
estilos.configure("TFrame", background="#DBDBDB")

mainframe = ttk.Frame(root, style='mainframe.TFrame')
mainframe.grid(column=0, row=0)

estilos_label1 = ttk.Style()
estilos_label1.configure("Label.TLabel", font = 'arial 15', anchor='E')

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style= 'Label.TLabel') 
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W,E))

estilos_label2= ttk.Style()
estilos_label2.configure("Label.TLabel", font = 'arial 40', anchor='E')

entrada2 = StringVar()
laber_entrada2 = ttk.Label(mainframe,textvariable= entrada2,  style= 'Laber2.TLabel')
laber_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,E))

#estilos botones
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('Botones_numeros.TButton', font = 'arial 22', Widget=5, background='#ffffff', relief='flat')

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('Botones_borrar.TButton', font = 'arial 22', Widget = 6, relief='flat' , background='#CECECE')
estilos_botones_borrar.map('Botones_borrar.TButton',foreground=[('active', '#FF0000')], background=[('active', '#858585')])

estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure('Botones_restantes.TButton', font = 'arial 22', Widget = 6, relief='flat', background='#CECECE')


#creando los botones
button0 = ttk.Button(mainframe, text="0", style= 'Botones_numeros.TButton')
button1 = ttk.Button(mainframe, text="1", style= 'Botones_numeros.TButton')
button2 = ttk.Button(mainframe, text="2", style= 'Botones_numeros.TButton')
button3 = ttk.Button(mainframe, text="3", style= 'Botones_numeros.TButton')
button4 = ttk.Button(mainframe, text="4", style= 'Botones_numeros.TButton')
button5 = ttk.Button(mainframe, text="5", style= 'Botones_numeros.TButton')
button6 = ttk.Button(mainframe, text="6", style= 'Botones_numeros.TButton')
button7 = ttk.Button(mainframe, text="7", style= 'Botones_numeros.TButton')
button8 = ttk.Button(mainframe, text="8", style= 'Botones_numeros.TButton')
button9 = ttk.Button(mainframe, text="9", style= 'Botones_numeros.TButton')

#creando funcionalidad de los operadores
button_borrar = ttk.Button(mainframe, text= chr(9003), style= 'Botones_borrar.TButton')
button_borrar_todo = ttk.Button(mainframe, text= ('C'), style= 'Botones_borrar.TButton')
button_parentesis1 = ttk.Button(mainframe, text= ('('), style= 'Botones_restantes.TButton')
button_parentesis2 = ttk.Button(mainframe, text= (')'), style= 'Botones_restantes.TButton')
button_punto = ttk.Button(mainframe, text= '.', style= 'Botones_restantes.TButton')
button_division = ttk.Button(mainframe, text= chr(247), style= 'Botones_restantes.TButton')
button_multiplicaion = ttk.Button(mainframe, text='x', style= 'Botones_restantes.TButton')
button_rersta = ttk.Button(mainframe, text= '-', style= 'Botones_restantes.TButton')
button_suma = ttk.Button(mainframe, text= '+' , style= 'Botones_restantes.TButton')
button_igual = ttk.Button(mainframe, text='=', style= 'Botones_restantes.TButton')
button_raiz_cuadrada = ttk.Button(mainframe, text='√', style= 'Botones_restantes.TButton')

#colocando botos en pantalla
button_parentesis1.grid(column=0, row=2)
button_parentesis2.grid(column=1, row=2)
button_borrar_todo.grid(column=2, row=2)
button_borrar.grid(column=3, row=2)
button7.grid(column=0, row=3)
button8.grid(column=1, row=3)
button9.grid(column=2, row=3)
button_division.grid(column=3, row=3)
button4.grid(column=0, row=4)
button5.grid(column=1, row=4)
button6.grid(column=2, row=4)
button_multiplicaion.grid(column=3, row=4)
button1.grid(column=0, row=5)
button2.grid(column=1, row=5)
button3.grid(column=2, row=5)
button_suma.grid(column=3, row=5)
button0.grid(column=0, row=6, columnspan=2, sticky=(W, E))
button_punto.grid(column=2, row=6)
button_rersta.grid(column=3, row=6)
button_igual.grid(column=0, row=7, columnspan=3, sticky= (W,E))
button_raiz_cuadrada.grid(column=3, row=7)


root.mainloop()

                             
