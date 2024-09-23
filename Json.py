from json import loads, dump
def leer():
    with open('data.json','r', encoding="utf-8-sig") as file:
        datos = file.read()
    objeto = loads(datos)
    return objeto
def escribir(objeto):
    with open('data.json','w', encoding="utf-8" ) as file:
        dump(objeto, file, ensure_ascii= False, indent=2)
