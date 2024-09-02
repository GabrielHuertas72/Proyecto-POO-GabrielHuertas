from color import Color as c 
from os import system , name
from sys import stdout
from Articulos import Articulos as art
#from Clases import *
#Funciones default 
def limpiar(): # Limpiar la pantalla 
    system('cls' if name == 'nt' else 'clear')
def borrar_ult_linea(r): # Funcion para borrar lineas sin perder el menu ya establecido
    for r in range(r): 
        stdout.write(c.CURSOR_UP_ONE) 
        stdout.write(c.ERASE_LINE) 
def continuar():
    system("Pause")
def terminar():
    print("")
    print(c.WHITE+c.BOLD+'{}'.format(' '*44)+"Gracias por usar el programa. !Tenga un buen día¡")
    print("")
    continuar()
    SystemExit  
#Funcionalidades del menu
def opc_inv(f,d):
    print("")
    print(c.RED+c.BOLD+'{}'.format(' '*44)+"Seleccione una opción valida."+c.RESET)
    print("")
    continuar()
    borrar_ult_linea(d) # Contar siempre desde el 3 teniendo en cuenta la propia funcion
    f()
def volver_menu():
    vm = input(c.BLUE+c.BOLD+'{}'.format(' '*44)+"¿Desea volver al menu? (Y/N): "+c.WHITE).upper()    
    if vm == "Y":
        launcher()
    elif vm  == "N":
        terminar()
    else:
        opc_inv(volver_menu,5)
def placeholder():
    print(c.YELLOW+c.BOLD+'{}'.format(' '*44)+"!Hola¡ soy Guybrush Threepwood, no, espera, soy un placeholder")
    volver_menu()
#Abajo se encontraran las funciones relativas a la interfaz       
def launcher():
    limpiar()
    print("")
    print(c.BOLD + c.GREEN + '{}'.format(' '*44)+"╔"+'{}'.format('═'*60)+"╗")
    print('{}'.format(' '*64)+"Aplicacion de Gestion")
    print('{}'.format(' '*69)+"ver.0.707106")
    print('{}'.format(' '*44)+"╚"+'{}'.format('═'*60)+"╝"+c.RESET)
    continuar()
    borrar_ult_linea(1)
    menu_principal()
def menu_principal():
    print(c.BOLD+ c.WHITE+'{}'.format(' '*58)+"Opciones de gestion del almacen")
    print("")
    print('{}'.format(' '*55)+"1. Buscar articulo.")
    print('{}'.format(' '*55)+"2. Generar lista de inventario.")
    print('{}'.format(' '*55)+"3. Generar prioridad de venta.")
    print("")
    print('{}'.format(' '*55)+"0. Cerrar programa."+c.RESET)
    print("")
    sel_mindice()
def sel_mindice():
    i = input(c.BOLD + c.BLUE+'{}'.format(' '*44) +"¿Que accion desea realizar?: "+c.WHITE+c.RESET)
    if i == "1":
        limpiar()
        mbusqueda()
    elif i == "2":
        limpiar()
        placeholder()
    elif i == "3":
        limpiar()
        placeholder()          
    elif i== "4":
        limpiar()
        placeholder()
    elif i == "0":
        terminar()
    else:
        opc_inv(sel_mindice,5) 
def mbusqueda():
    print("")
    print(c.BOLD + c.CYAN + '{}'.format(' '*44)+"╔"+'{}'.format('═'*60)+"╗")
    print("")
    print('{}'.format(' '*64)+"Busqueda de articulos")
    print("")
    print('{}'.format(' '*44)+"╚"+'{}'.format('═'*60)+"╝"+c.RESET)
    print("")
    print('{}'.format(' '*55)+c.BOLD+c.WHITE+"1. Buscar por nombre.")
    print('{}'.format(' '*55)+"2. Buscar por marca.")
    print('{}'.format(' '*55)+"3. Buscar por rango de precio.")
    print('{}'.format(' '*55)+"4. Buscar por antiguedad.")
    print("")
    print('{}'.format(' '*55)+"0. Volver al menu."+c.RESET)
    print("")
    ib = input(c.BOLD + c.BLUE+'{}'.format(' '*44)+"Seleccione una opcion: "+c.WHITE)
    if ib == "1":
        placeholder()
    elif ib == "2":
        placeholder()
    elif ib == "3":
        placeholder()
    elif ib == "4":
        placeholder()
    else:
        opc_inv(mbusqueda,18)

