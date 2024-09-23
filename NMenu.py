from Json import *
from color import Color as c
from Recursos import *
from datetime import date
from Clases import Almacen, Articulos as art
def menu_principal():# Funcion menu principal
    limpiar()
    espacio()
    print(c.BOLD + c.GREEN + '{}'.format(' '*44)+"╔"+'{}'.format('═'*60)+"╗")
    espacio()
    print('{}'.format(' '*64)+"Aplicacion de Gestion")
    espacio()
    print('{}'.format(' '*44)+"╚"+'{}'.format('═'*60)+"╝"+c.RESET)
    espacio()
    print(c.BOLD+ c.WHITE+'{}'.format(' '*58)+"Opciones de gestion del almacen")
    espacio()
    print('{}'.format(' '*55)+"1. Agregar articulos.")
    print('{}'.format(' '*55)+"2. Retirar articulos.")
    print('{}'.format(' '*55)+"3. Buscar articulos.")
    print('{}'.format(' '*55)+"4. Consultar lista de inventario.")
    espacio()
    print('{}'.format(' '*55)+"0. Cerrar programa."+c.RESET)
    espacio()
    menu_selec()
def menu_selec(): #Funcion seleccionador menu principal
        i = input(c.BOLD + c.BLUE+'{}'.format(' '*44) +"¿Que accion desea realizar?: "+c.WHITE).strip()
        if i == "1":
            limpiar()
            agregar_articulo()
        elif i == "2":
            limpiar()
            retirar_articulos()
        elif i == "3":
            limpiar()
            menu_busqueda()          
        elif i== "4":
            limpiar()
            menu_generar_lista()

        elif i == "0":
            terminar()
        else:
            opc_inv(menu_selec,5)
def agregar_articulo(): #Funcion del input de los articulos
    espacio()
    print(c.BOLD + c.BLUE + '{}'.format(' '*44)+"╔"+'{}'.format('═'*60)+"╗")
    print('{}'.format(' '*64)+"Agregar articulos")
    print('{}'.format(' '*44)+"╚"+'{}'.format('═'*60)+"╝"+c.RESET)
    espacio()
    in_agregar()
def in_agregar(): # Input para agregar articulos
        ia = input( c.YELLOW+c.BOLD+'{}'.format(' '*44)+"Ingrese el nombre del articulo a agregar (0 para volver): "+c.WHITE)
        inp=est_inp_txt(ia)
        datos = leer()
        if inp in datos:
            espacio()
            print(c.WHITE+c.BOLD+'{}'.format(' '*44)+"Ya hay existencias de ese articulo en el almacen.")
            continuar()
            nu_agregar(datos,inp)
        elif inp == "0":
            menu_principal()
        else:
            espacio()
            tipo = input(c.YELLOW+'{}'.format(' '*44)+"Escriba el tipo del articulo: "+c.WHITE)
            nt = est_inp_txt(tipo)
            espacio()
            marca = input(c.YELLOW+'{}'.format(' '*44)+"Escriba la marca del articulo: "+c.WHITE)
            nm = est_inp_txt(marca)
            espacio()
            precio = f_precio()
            espacio()
            unidades = f_unidades()
            espacio()
            fecha_e = f_fecha_e(unidades)
            espacio()
            datos[inp] = {
                "Tipo": nt,
                "Marca": nm,
                "Precio": precio,
                "Fecha de entrada":  fecha_e,
                "Unidades": unidades
        }
        borrar_ult_linea(9)
        escribir(datos)
        prn_art_cont(inp)
        espacio()
        print(c.GREEN+c.BOLD+'{}'.format(' '*44)+"Articulo añadido correctamente."+c.WHITE)
        espacio()
        print('{}'.format(' '*44)+"Volviendo al menu principal.")
        espacio()
        continuar()
        menu_principal()
def prn_art_cont(key):#Print de articulos
    datos=leer()
    f1=str(datos[key]["Fecha de entrada"])
    fecha = f1.replace("'","")
    print('{}'.format(' '*44)+'{}'.format('═'*62))
    print('{}'.format(' '*46)+"Tipo: "+str(datos[key]["Tipo"]))
    print('{}'.format(' '*46)+"Marca: "+str(datos[key]["Marca"]))
    print('{}'.format(' '*46)+"Precio: "+str(datos[key]["Precio"]))
    print('{}'.format(' '*46)+"Fecha de entrada: "+ fecha)
    print('{}'.format(' '*46)+"Unidades: "+str(datos[key]["Unidades"]))
def f_fecha_e(): # funcion de la fecha
    fecha = date.today()
    dia = fecha.day
    mes = fecha.month
    año = fecha.year
    key = f"{dia}/{mes}/{año}"
    return key
def f_precio(): # funcion del precio
    p = input(c.YELLOW+c.BOLD+'{}'.format(' '*44)+"Digite el precio de la unidad del articulo: "+c.WHITE).strip()
    if p.isnumeric() == True and  0<= int(p):
        return int(p)
    else:
        opc_inv(f_precio,5)
def f_unidades(): # funcion de las unidades
    u = input(c.YELLOW+c.BOLD+'{}'.format(' '*44)+"Digite la cantidad de unidades del articulo: "+c.WHITE).strip()
    if u.isnumeric() == True and 0 <= int(u):
        return int(u)
    else:
        opc_inv(f_unidades,5)
def nu_agregar(y,a): # funcion de agregar mas existencias
    u = y[a]["Unidades"]
    print(c.YELLOW+c.BOLD+'{}'.format(' '*44)+f"Actualmente hay almacenadas {u} unidades")
    p = input(c.YELLOW+c.BOLD+'{}'.format(' '*44)+"Ingrese la cantidad de articulos que desea ingresar: "+c.WHITE)
    if p.isnumeric() == True and int(p) > 0:
        fecha = date.today()
        dia = fecha.day
        mes = fecha.month
        año = fecha.year
        key = f"{dia}/{mes}/{año}"
        nn = y[a]["Unidades"] + int(p)
        y[a]["Unidades"] = nn
        y[a]["Fecha de entrada"] = key
        escribir(y) 
        espacio()
        print(c.GREEN+c.BOLD+'{}'.format(' '*44)+f"Cantidad de articulos actual: {nn}")
        espacio()
        print('{}'.format(' '*44)+"Articulos añadidos correctamente."+c.WHITE)
        espacio()
        print('{}'.format(' '*44)+"Volviendo al menu principal."+c.WHITE)
        continuar()
        menu_principal()
    else:
            opc_inv(nu_agregar(y,a),6)
def retirar_articulos(): # Retirar articulos
    espacio()
    print(c.BOLD + c.BLUE + '{}'.format(' '*44)+"╔"+'{}'.format('═'*60)+"╗")
    print('{}'.format(' '*64)+"Retirar articulos")
    print('{}'.format(' '*44)+"╚"+'{}'.format('═'*60)+"╝"+c.RESET)
    espacio()
    in_retirar()
def in_retirar():
    ir = input( c.YELLOW+c.BOLD+'{}'.format(' '*44)+"Ingrese el nombre del articulo a retirar (0 para volver): "+c.WHITE)
    inp = est_inp_txt(ir)
    datos = leer()
    if inp in datos:
        u = datos[inp]["Unidades"]
        espacio()
        print(c.YELLOW+c.BOLD+'{}'.format(' '*44)+f"Actualmente hay almacenadas {u} unidades"+c.WHITE)
        art_restar(inp)
    elif inp == "0":
        menu_principal()
    else:
        opc_inv(in_retirar,5)
def art_restar(a):
    espacio()
    datos=leer()
    u = datos[a]["Unidades"]
    p = input(c.BOLD+c.YELLOW+'{}'.format(' '*44)+"Ingrese la cantidad de articulos que desea retirar: "+c.WHITE).strip()
    if p.isnumeric() == True and 0 <= int(p) and u >= int(p):
        u = u- int(p)
        datos[a]["Unidades"] = u
        escribir(datos) 
        espacio()
        print(c.GREEN+c.BOLD+'{}'.format(' '*44)+f"Cantidad de articulos actual: {u}")
        espacio()
        print('{}'.format(' '*44)+"Articulos retirados correctamente."+c.WHITE)
        espacio()
        print('{}'.format(' '*44)+"Volviendo al menu principal."+c.WHITE)
        continuar()
        menu_principal()
    else:
            opc_inv(art_restar,5)
def menu_busqueda():
    espacio()
    print(c.BOLD + c.CYAN + '{}'.format(' '*44)+"╔"+'{}'.format('═'*60)+"╗")
    espacio()
    print('{}'.format(' '*64)+"Busqueda de articulos")
    espacio()
    print('{}'.format(' '*44)+"╚"+'{}'.format('═'*60)+"╝"+c.RESET)
    espacio()
    print('{}'.format(' '*55)+"1. Buscar por tipo.")
    print('{}'.format(' '*55)+"2. Buscar por marca.")
    print('{}'.format(' '*55)+"3. Buscar por rango de precio.")
    espacio()
    print('{}'.format(' '*55)+"0. Volver al menu."+c.RESET)
    espacio()
    i_menu_bus()
def i_menu_bus():
    ib = input(c.BOLD + c.BLUE+'{}'.format(' '*44)+"Seleccione una opcion: "+c.WHITE).strip()
    espacio()
    if ib == "1":
        datos = leer()
        bn = input('{}'.format(' '*55)+c.YELLOW+"Ingrese el tipo de articulo a buscar: "+c.WHITE) 
        a=bn.upper()
        b=a.strip()
        d=b.replace(' ',"")  
        for i in datos:
            tipo = datos[i]["Tipo"]
            marca = datos[i]["Marca"]
            precio = datos[i]["Precio"]
            fecha_e = datos[i]["Fecha de entrada"]
            unidades = datos[i]["Unidades"]
            key = i
            if d == datos[i]["Tipo"]:
                print('{}'.format(' '*44)+"Nombre: "+key)
                print('{}'.format(' '*44)+"Tipo: "+tipo)
                print('{}'.format(' '*44)+"Marca: "+str(marca))
                print('{}'.format(' '*44)+"Precio: "+str(precio))
                print('{}'.format(' '*44)+"Fechas de entrada: "+str(fecha_e))
                print('{}'.format(' '*44)+"Unidades: "+str(unidades))
                espacio()
            else: 
                pass
        continuar()   
        menu_principal()
    elif ib == "2":
        ib = input(c.BOLD + c.BLUE+'{}'.format(' '*44)+"Seleccione una opcion: "+c.WHITE).strip()
        datos = leer()
        bn = input('{}'.format(' '*55)+c.YELLOW+"Ingrese la Marca del articulo a buscar: "+c.WHITE) 
        a=bn.upper()
        b=a.strip()
        d=b.replace(' ',"")  
        for i in datos:
            tipo = datos[i]["Tipo"]
            marca = datos[i]["Marca"]
            precio = datos[i]["Precio"]
            fecha_e = datos[i]["Fecha de entrada"]
            unidades = datos[i]["Unidades"]
            key = i
            if d == datos[i]["Marca"]:
                print('{}'.format(' '*44)+"Nombre: "+key)
                print('{}'.format(' '*44)+"Tipo: "+tipo)
                print('{}'.format(' '*44)+"Marca: "+str(marca))
                print('{}'.format(' '*44)+"Precio: "+str(precio))
                print('{}'.format(' '*44)+"Fechas de entrada: "+str(fecha_e))
                print('{}'.format(' '*44)+"Unidades: "+str(unidades))
                espacio()
            else: 
                pass
        continuar()   
        menu_principal()
    elif ib == "3":
        ib = input(c.BOLD + c.BLUE+'{}'.format(' '*44)+"Seleccione una opcion: "+c.WHITE).strip()
        datos = leer()
        bn = input('{}'.format(' '*55)+c.YELLOW+"Ingrese el rango de precio a buscar: "+c.WHITE) 
        a=bn.upper()
        b=a.strip()
        d=b.replace(' ',"")  
        for i in datos:
            tipo = datos[i]["Tipo"]
            marca = datos[i]["Marca"]
            precio = datos[i]["Precio"]
            fecha_e = datos[i]["Fecha de entrada"]
            unidades = datos[i]["Unidades"]
            key = i
            if int(d) == datos[i]["Precio"]:
                print('{}'.format(' '*44)+"Nombre: "+key)
                print('{}'.format(' '*44)+"Tipo: "+tipo)
                print('{}'.format(' '*44)+"Marca: "+str(marca))
                print('{}'.format(' '*44)+"Precio: "+str(precio))
                print('{}'.format(' '*44)+"Fechas de entrada: "+str(fecha_e))
                print('{}'.format(' '*44)+"Unidades: "+str(unidades))
                espacio()
            else: 
                pass
        continuar()   
        menu_principal()
    elif ib == "0":
        menu_principal()
    else:
        opc_inv(i_menu_bus,18)
def inst_articulo(nombre,var):
    datos = leer()
    tipo = datos[nombre]["Tipo"]
    marca = datos[nombre]["Marca"]
    precio = datos[nombre]["Precio"]
    fecha_e = datos[nombre]["Fecha de entrada"]
    unidades = datos[nombre]["Unidades"]
    key = nombre
    nombre = art(tipo, marca, precio, fecha_e, unidades)
    if var == 1:
        print('{}'.format(' '*44)+"Nombre: "+key)
        print('{}'.format(' '*44)+"Tipo: "+tipo)
        print('{}'.format(' '*44)+"Marca: "+str(marca))
        print('{}'.format(' '*44)+"Precio: "+str(precio))
        print('{}'.format(' '*44)+"Fechas de entrada: "+str(fecha_e))
        print('{}'.format(' '*44)+"Unidades: "+str(unidades))
        espacio()
    elif var == 0:
        return nombre,key
def inst_almacen(name,arti:list,var=int):
    datos = leer()
    for i in datos:
        iart = inst_articulo(i,var)
        arti.append(iart)
    objAlmacen = Almacen(name,arti)
    return objAlmacen
def menu_generar_lista():
    print(c.BOLD + c.BLUE + '{}'.format(' '*44)+"╔"+'{}'.format('═'*60)+"╗")
    print('{}'.format(' '*64)+"Generar lista")
    print('{}'.format(' '*44)+"╚"+'{}'.format('═'*60)+"╝"+c.RESET)
    espacio()
    inst_almacen("Consulta",arti=[] , var =1)
    espacio()
    print(c.GREEN+c.BOLD+"Lista impresa ")
    espacio()
    continuar()
    menu_principal()
