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
        +Nombre 
        +Marca  
        +Precio 
        +Unidades 
        +Fecha de entrada 
        +Busqueda por nombre()
        +Busqueda por marca()
        +Busqueda por ramgo de precio()
        +Busqueda por fecha de almacenamiento()
    }
    class Articulo_Perecedero{
        +Fecha de vencimiento
        +Estado del articulo
        +Generar dias para el pereciimiento()
        +Generar prioridad de venta()
    }
    Articulos --*  Articulo_Perecedero 

```
