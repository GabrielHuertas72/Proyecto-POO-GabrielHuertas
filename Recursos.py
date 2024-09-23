from color import Color as c 
from os import system , name
from sys import stdout
from Clases import Articulos as art
from Recursos import *
#Funciones 
def limpiar(): # Limpiar la pantalla 
    system('cls' if name == 'nt' else 'clear')
def borrar_ult_linea(r): # Funcion para borrar lineas sin perder el menu ya establecido
    for r in range(r): 
        stdout.write(c.CURSOR_UP_ONE) 
        stdout.write(c.ERASE_LINE) 
def continuar():
    system("Pause")
def terminar():
    espacio()
    print(c.WHITE+c.BOLD+'{}'.format(' '*44)+"Gracias por usar el programa. !Tenga un buen día¡")
    espacio()
    SystemExit  
#Funcionalidades del menu
def opc_inv(f,d):
    espacio()
    print(c.RED+c.BOLD+'{}'.format(' '*44)+"Seleccione una opción valida."+c.RESET)
    espacio()
    continuar()
    borrar_ult_linea(d) # Contar siempre desde el 3 teniendo en cuenta la propia funcion
    f()
def espacio():
    print("")
def est_inp_txt(i):
    a=i.upper()
    b=a.strip()
    c=b.replace(' ',"")
    return c
