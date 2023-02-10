import datetime
from models.biblioteca import Biblioteca


class Bibliotecario(Biblioteca):

    def __init__(self):
        super().__init__("libros.csv")
        self.lista_prestamos = []

    def prestar_libro(self, titulo: str, fecha_prestamo: datetime, fecha_devolucion: datetime):
        self.lista_prestamos.insert(titulo, {
                                    "titulo": titulo, "fecha_prestamo": fecha_prestamo, "fecha_devolucion": fecha_devolucion})

    def buscar_prestamo(self, titulo: str):
        return self.lista_prestamos[titulo]

    def devolver_libro(self, titulo: str):
        del self.lista_prestamos[titulo]

        print("Libro devuelto exitoxamente.")

    def listar_prestamos(self):
        for prestamo in self.lista_prestamos:
            print("Titulo: {}, fecha de prestamo: {}, fecha de devolucion: {}",
                  prestamo["titulo"], prestamo["fecha_prestamo"], prestamo["fecha_devolucion"])
