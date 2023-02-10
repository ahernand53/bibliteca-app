# Ejercicio de programación orientada a objetos avanzado

## Sistema de gestión de biblioteca

### Clase `Libro`

Atributos:
- Título
- Autor
- Fecha de publicación
- Número de páginas

### Clase `Biblioteca`

Atributos:
- Lista de libros

Métodos:
- `agregar_libro(libro)`: permite agregar un libro a la biblioteca.
- `eliminar_libro(titulo)`: permite eliminar un libro de la biblioteca por título.
- `buscar_libro(titulo)`: permite buscar un libro en la biblioteca por título y devuelve el libro si se encuentra, de lo contrario devuelve `None`.
- `listar_libros()`: permite listar todos los libros en la biblioteca.

### Clase `Bibliotecario` (hereda de `Biblioteca`)

Atributos adicionales:
- Lista de préstamos

Métodos adicionales:
- `prestar_libro(titulo, fecha_prestamo, fecha_devolucion)`: permite prestar un libro de la biblioteca por título, fecha de préstamo y fecha de devolución. Se debe registrar el préstamo en el libro correspondiente y en una lista de préstamos en el bibliotecario.
- `devolver_libro(titulo)`: permite devolver un libro de la biblioteca por título. Se debe actualizar el estado de préstamo del libro correspondiente y la lista de préstamos en el bibliotecario.
- `buscar_prestamo(titulo)`: permite buscar un préstamo en la lista de préstamos del bibliotecario por título y devuelve los detalles del préstamo si se encuentra, de lo contrario devuelve `None`.
- `listar_prestamos()`: permite listar todos los préstamos en la lista de préstamos del bibliotecario.