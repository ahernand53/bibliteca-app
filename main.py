import tkinter as tk
from typing import List
from models.bibliotecario import Bibliotecario

from models.libro import Libro


class MyTable:
    def __init__(self, master, title, data):
        self.master = master
        self.title = title
        self.data = data

        frame = tk.Frame(master)
        frame.pack(fill=tk.X)

        headers = ["Título", "Author",
                   "Numero de paginas", "Fecha Publicacion"]
        for i, header in enumerate(headers):
            label = tk.Label(frame, text=header)
            label.grid(row=0, column=i, padx=10, pady=10)

        for i, libro in enumerate(data):
            label = tk.Label(frame, text=libro.titulo)
            label.grid(row=i + 1, column=0, padx=10, pady=10)
            label = tk.Label(frame, text=libro.autor)
            label.grid(row=i + 1, column=1, padx=10, pady=10)
            label = tk.Label(frame, text=libro.numero_paginas)
            label.grid(row=i + 1, column=2, padx=10, pady=10)
            label = tk.Label(frame, text=libro.fecha_publicacion)
            label.grid(row=i + 1, column=3, padx=10, pady=10)

        # prestamos_frame = tk.Frame(master)
        # prestamos_frame.pack(fill=tk.X)

        # headers = ["Título", "Author",
        #            "Numero de paginas", "Fecha Publicacion"]
        # for i, header in enumerate(headers):
        #     label = tk.Label(prestamos_frame, text=header)
        #     label.grid(row=0, column=i, padx=10, pady=10)

        # for i, libro in enumerate(data):
        #     label = tk.Label(prestamos_frame, text=libro.titulo)
        #     label.grid(row=i + 1, column=0, padx=10, pady=10)
        #     label = tk.Label(prestamos_frame, text=libro.autor)
        #     label.grid(row=i + 1, column=1, padx=10, pady=10)
        #     label = tk.Label(prestamos_frame, text=libro.numero_paginas)
        #     label.grid(row=i + 1, column=2, padx=10, pady=10)
        #     label = tk.Label(prestamos_frame, text=libro.fecha_publicacion)
        #     label.grid(row=i + 1, column=3, padx=10, pady=10)


bibliotecario = Bibliotecario("libros.csv")
data = bibliotecario.lista_libros

root = tk.Tk()
table = MyTable(root, "Tabla de préstamos de libros", data)
root.mainloop()
