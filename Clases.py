from Recursos import * 

class Articulos :
    def __init__(self, tipo: str, marca:str ,precio: int, f_entrada: str,unidades: int ) :
        self.tipo = tipo
        self.marca = marca
        self.precio = precio
        self.unidades = unidades # Unidades en existencia en el almacen
        self.f_entrada = f_entrada # Fecha de entrada al almacen
    # Definimos las caracteristicas variables de la clase articulos
    def set_tipo(self,s):
        self.tipo = s
    def set_marca(self,s):
        self.marca = s
    def set_precio(self,s):
        self.precio = s
    def set_fentrada(self,s):
        self.f_entrada = s
    def set_unidades(self,s):
        self.unidades = s

    #Setters
    def get_tipo(self):
        return self.tipo
    def get_marca(self):
        return self.marca
    def get_precio(self):
        return self.precio
    def get_fentrada(self):
        return self.f_entrada
    def get_unidades(self):
        return self.unidades
    #getters
class Almacen:
    def __init__(self, l_nombre: str, articulos: list = [Articulos]) :
        self.l_nombre = l_nombre
        self.articulos = articulos
    def set_nombre(self,nombre):
        self.nombre = nombre
    def get_articulos(self, articulos):
        self.articulos = articulos 
   