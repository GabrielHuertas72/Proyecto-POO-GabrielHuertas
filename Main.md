# Aplicación de gestion de inventario
## Programación Orientada a Objetos - Gabriel Huertas 
Repositorio del desarrollo de un programa en python el cual servira para la gestión del inventario de un almacen
## Funcionalidades propuestas
- Busqueda de articulospor nombre, marca, rango de precio, fecha de almacenamiento.
- Funcionalidad de registro de las operaciones realizadas en la operación.
- Funcionalidad de crear un documento con la lista de los articulos en el almacen.
- funcionalidad de crear prioridades de venta teniendo en cuenta la fecha de almacenamiento.
## Diagrama de clases 
```mermaid
classDiagram
    class Articulos{
        + Nombre (str)
        + Marca  (str)
        + Precio (int)
        + Unidades (int)
        + Fecha de entrada (list)
        Articulos: +Busqueda por nombre()
        Articulos: +Busqueda por marca()
        Articulos: +Busqueda por ramgo de precio()
        Articulos: +Busqueda por fecha de almacenamiento()
    }
    class Articulo_Perecedero{
        + Fecha de vencimiento
        + Estado del articulo
        Articulo_Perecedero: Generar dias para el pereciimiento()
        Articulo_Perecedero: Genera prioridad de venta()
    }
    Articulos --*  Articulo_Perecedero 

```
