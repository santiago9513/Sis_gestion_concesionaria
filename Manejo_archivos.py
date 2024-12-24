import os
import json

def cargar_archivo(ruta):
    if not os.path.exists(ruta):    #si el archivo no existe, lo crea con un diccionario vacio
        with open(ruta,'w',encoding='utf-8') as archivo:
            dic = {}
            archivo.write(json.dumps(dic))
        return dic
    
    with open(ruta,'r',encoding='utf-8') as archivo:    #Si el archivo existe, lo abre, lee su contenido y lo carga al programa en ejecucion
        obj_json = json.loads(archivo.read())
        return obj_json

def guardar_archivo(ruta,datos):
    with open(ruta,'w',encoding='utf-8') as archivo:
        archivo.write(json.dumps(datos))
    return True

