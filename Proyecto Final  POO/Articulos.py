class Articulos :
    def __init__(self, nombre: str, marca:str ,precio: int, unidades: int, f_entrada: list = (int, int, int)) :
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.unidades = unidades # Unidades en existencia en el almacen
        self.f_entrada = f_entrada # Fecha de entrada al almacen
    # Definimos las caracteristicas variables de la clase articulos
    def busqueda_nombre(self):
        return self.nombre
ChocolatinaJet = Articulos(
    nombre = "Chocolatina", 
    marca = "Jet", 
    precio = 900, 
    unidades = 30, 
    f_entrada = (24,8,2020)  ) 
print(ChocolatinaJet.busqueda_nombre())