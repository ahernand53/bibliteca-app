from datetime import datetime


class Libro:

    def __init__(self, titulo: str, autor: str, numero_paginas: int, fecha_publicacion: str):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.fecha_publicacion = fecha_publicacion

    def obtener_fecha_publicacion(self):
        fecha = datetime.date(self.fecha_publicacion.split('/'))

        return str(fecha)

    def obtener_modelo(self):
        return "{},{},{},{}", self.titulo, self.autor, self.numero_paginas, self.__fecha_publicacion

    def __str__(self) -> str:
        return "[Titulo: {}, Autor: {}, fecha de publicacion: {}, numero de paginas: {}]", self.titulo, self.autor, self.__fecha_publicacion, self.numero_paginas
