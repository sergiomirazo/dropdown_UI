from tkinter import ttk
import tkinter as tk

menu = [
    'Avena',
    'Huevos con jamón',
    'Huevos con salchicha',
    'Huevos con tocineta',
    'Huevos estrellados',
    'Huevos benedictos',
    'Huevos revueltos con papas hashbrown',
    'Huevos con bistec'
]

global precio


def pedido():
    menu = click.get()
    print(str(menu))
    precio = ' '
    match menu:
        case 'Avena':
            precio = '35 MXN'
        case 'Huevos con jamón':
            precio = '30 MXN'
        case 'Huevos con salchicha':
            precio = '30 MNX'
        case 'Huevos con tocineta':
            precio = '50 MXN'
        case 'Huevos estrellados':
            precio = '30 MXN'
        case 'Huevos benedictos':
            precio = '80 MXN'
        case 'Huevos revueltos con papas hashbrown':
            precio = '95 MXN'
        case 'Huevos con bistec':
            precio = '108 MXN'
    l.config( text ='Sale ' + click.get() +'\n' + 'Precio: '+precio )


window = tk.Tk()
window.config(width=500, height=500)

window.title("Restaurant El Pelón de Hospicio")
titulo = tk.Label(window, bg='orange', fg='red', width=100, text='Bienvenido al Pelón de Hospicio ', font = ("sansserif", 16, "bold"))
titulo.pack(fill='x', ipadx=15, ipady=15)
slogan = tk.Label(window, bg='orange', fg='white', width=100, text='Aquí en el Pelón de Hospicio nadie se va sin comer', font = ("sansserif", 12, "bold"))
slogan.pack(fill='x', ipadx=15, ipady=15)
l = tk.Label(window, bg='orange', width=100, text='¿Qué desea ordenar?', font = ("sansserif", 12, "bold"))
l.pack(fill='x', ipadx=15, ipady=15)

click = tk.StringVar()
click.set('Menú')

drop = tk.OptionMenu( window, click, *menu )
drop.pack(ipadx=5, ipady=5, pady=15)

btn = tk.Button( window, bg='blue', fg='white', width = 20, text = 'Ordenar', command = pedido )
btn.pack(ipadx=5, ipady=5, pady=15)


window.mainloop()
