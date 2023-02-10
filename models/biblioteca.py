

import csv
from typing import List
from models.libro import Libro


class Biblioteca:

    def __init__(self, nombre_archivo):
        self.NOMBRE_ARCHIVO = nombre_archivo
        self.lista_libros: List[Libro] = []

    def cargar_libros_csv(self):
        with open(self.NOMBRE_ARCHIVO, 'r') as file:
            for line in file:
                propiedades = line.split(",")
                libro = Libro(*propiedades)
                self.lista_libros.insert(libro)

    def listar_libros(self):
        if self.lista_libros.__len__ == 0:
            print("No hay libros que en la biblioteca.")
            return

        for libro in self.lista_libros:
            print(libro.__str__)

    def buscar_libro(self, titulo: str) -> Libro:
        if self.lista_libros.__len__ == 0:
            print("No hay libros que en la biblioteca.")
            return

        for libro in self.lista_libros:
            if (libro.titulo == titulo):
                return libro

        return None

    def agregar_libro(self, libro: Libro):
        with open(self.NOMBRE_ARCHIVO, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(libro.obtener_modelo())

        self.cargar_libros_csv()
        print("Se ha agregado un nuevo libro con titulo: {}", libro.titulo)
