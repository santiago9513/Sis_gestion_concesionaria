import Manejo_archivos
import datetime
#los registros son diccionarios de forma que las claves son los IDs 
registro_vehiculos = Manejo_archivos.cargar_archivo('vehiculos.json')
registro_clientes = Manejo_archivos.cargar_archivo('clientes.json')
registro_transacciones = Manejo_archivos.cargar_archivo('transacciones.json')

def registrar_vehiculo(dominio,marca,modelo,tipo,año,kilometraje,precio_compra,precio_venta,estado):   #Cada vehiculo es un diccionario con sus atributos
    if len(registro_vehiculos) == 0:  #si el diccionario esta vacio establece en 1 el id
        id_vehiculo = 1
    else:
        id_vehiculo = int(max((registro_vehiculos.keys()))) + 1 #si ya hay elementos, genera un ID, incrementando en 1 al mayor
    vehiculo = {
        'dominio':dominio,
        'marca':marca,
        'modelo':modelo,
        'tipo':tipo,
        'año':año,
        'kilometraje':kilometraje,
        'precio_compra':precio_compra,
        'precio_venta':precio_venta,
        'estado':estado
        }
    registro_vehiculos[id_vehiculo] = vehiculo
    Manejo_archivos.guardar_archivo('vehiculos.json',registro_vehiculos)
    return

def registrar_cliente(nombre,apellido,documento,telefono,direccion,correo): #Cada cliente es un diccionario con sus atributos
    if registro_clientes:
        id_cliente = int(max((registro_clientes.keys())))+1
    else:
        id_cliente = 1
    cliente = {
        'nombre':nombre,
        'apellido':apellido,
        'documento':documento,
        'direccion':direccion,
        'telefono':telefono,
        'correo':correo
        }
    registro_clientes[id_cliente] = cliente
    Manejo_archivos.guardar_archivo('clientes.json',registro_clientes)
    return

def registrar_transaccion(id_vehiculo,id_cliente,tipo,monto,observaciones): #Cada transaccion es un diccionario con sus atributos
    if registro_transacciones:
        id_transaccion = int(max((registro_transacciones.keys())))+1
    else:
        id_transaccion = 1
    transaccion = {
        'id_vehiculo':id_vehiculo,
        'id_cliente':id_cliente,
        'tipo':tipo,
        'fecha':datetime.datetime.now().strftime('%d/%m/%Y'),
        'monto':monto,
        'observaciones':observaciones       
        }
    registro_transacciones[id_transaccion] = transaccion
    Manejo_archivos.guardar_archivo('transacciones.json',registro_transacciones)
    return

def buscar_multiple(registro,atributo,valor):    #busqueda especificando en que registro, que atributo del registro y el valor de dicho atributo con resultado multiple
    lista_id = []
    for id in registro:
        if registro[id][atributo] == valor:
            lista_id.append(id)
    return lista_id #devuelve una lista de IDs que coincidieron con la busqueda

def buscar_unico(registro,atributo,valor):    #busqueda especificando en que registro, que atributo del registro y el valor de dicho atributo con resultado unico
    resultado_id = None
    for id in registro:
        if registro[id][atributo] == valor.lower():
            resultado_id = id
    return resultado_id

def editar_registro(archivo,registro,id):   #edita registro especificando atributo y valor
        while True:
            atributo = input(f'Ingrese atributo a editar ({list(registro[id].keys())}): ')
            if atributo not in registro[id].keys():
                print('Ingrese un atributo valido')
                continue
            valor = input(f'Ingrese nuevo valor de {atributo}: ').lower()
            registro[id][atributo] = valor
            Manejo_archivos.guardar_archivo(archivo,registro)
            print_centrado(f'Registro actualizado con exito:\n{registro[id]}\n')
            continuar = input('Ingrese "S" para seguir editando el registro: ').lower()
            if continuar != 's':
                break
        return

def eliminar_registro(archivo,registro,id):     #comprueba que el registro (vehiculo o cliente) no este asociado a una transaccion, caso contrario pide confirmacion antes de eliminar
    if registro == registro_clientes:
        tipo_id = 'id_cliente'
    elif registro == registro_vehiculos:
        tipo_id = 'id_vehiculo'
    if len(buscar_multiple(registro_transacciones,tipo_id,id)) != 0:
        return print_centrado(f'El registro: {registro[id]} esta asociado a una transaccion, no pude ser eliminado')
    print('Ingrese "s" si desea eliminar el siguiente registro:')
    print_centrado(registro[id])
    respuesta = input().lower()
    if respuesta == 's':
        del(registro[id])
        Manejo_archivos.guardar_archivo(archivo,registro)
        return print_centrado('Registro borrado con exito')
    else:
        return print_centrado('No se borro registro')

def buscar_transacciones_fechas(fecha1,fecha2):    #busqueda de transacciones entre dos fechas
    lista_id = []
    for id in registro_transacciones:
        if fecha1 <= registro_transacciones[id]['fecha'] <= fecha2:
            lista_id.append(id)
    return lista_id #devuelve una lista de IDs que coincidieron con la busqueda

def imprimir_transaccion(id):   #imprime el cliente, el vehiculo y la transaccion para tener la informacion completa
    id_cliente = registro_transacciones[id]['id_cliente']
    id_vehiculo = registro_transacciones[id]['id_vehiculo']
    print(f'Cliente: {registro_clientes[id_cliente]}')
    print(f'Vehiculo: {registro_vehiculos[id_vehiculo]}')
    print(f'Transaccion: {registro_transacciones[id]}\n')

def imprimir_listado_transacciones(lista_id):   #imprime una lista de transacciones de compra y otra de venta
    lista_id_venta = []
    lista_id_compra = []
    for id in lista_id:
        if registro_transacciones[id]['tipo'] == 'venta':
            lista_id_venta.append(id)
        else:
            lista_id_compra.append(id)
    if len(lista_id_compra) != 0:
        total = 0
        print_centrado(f'Listado de transacciones de COMPRA:')
        for id in lista_id_compra:
            total = total + float(registro_transacciones[id]['monto'])
            imprimir_transaccion(id)
        print_centrado(f'Totalizador de monto: ${total}')
    else:
        print_centrado(f'No se encontro transacciones de COMPRA')
    print_centrado('-----')
    if len(lista_id_venta) != 0:
        total = 0
        print_centrado(f'Listado de transacciones de VENTA:')
        for id in lista_id_venta:
            total = total + float(registro_transacciones[id]['monto'])
            imprimir_transaccion(id)
        print_centrado(f'Totalizador de monto: ${total}')
    else:
        print_centrado(f'No se encontro transacciones de VENTA')

def print_centrado(texto):
    texto = str(texto)  #puede ser resultado de una funcion
    return print(f'\n{texto.center(150)}\n')


def menu_principal():
    while True:
        opcion = input('\nCon que desea trabajar: \n 1 - Clientes \n 2 - Vehiculos \n 3 - Transacciones\n S - Salir\n').lower()
        match opcion:
            case '1':
                menu_clientes()
            case '2':
                menu_vehiculos()
            case '3':
                menu_transacciones()
            case 's':
                break
            case _:
                print('Ingrese una opcion correcta')

def menu_clientes():
    opcion = input('\n1 - Registrar\n2 - Buscar por documento\n3 - Listar por apellido\n4 - Listar por nombre\n5 - Editar\n6 - Eliminar\nS - Volver al menu principal\n').lower()
    match opcion:
        case '1':   #Crear
            print_centrado('REGISTRAR CLIENTE')
            nombre = input('Ingrese nombre: ').lower()
            apellido = input('Ingrese apellido: ').lower()
            documento = input('Ingrese documento: ').lower()
            telefono = input('Ingrese telefono: ').lower()
            direccion = input('Ingrese direccion: ').lower()
            correo = input('Ingrese correo: ').lower()
            registrar_cliente(nombre,apellido,documento,telefono,direccion,correo)
            print_centrado('Cliente registrado con exito!')
        case '2':   #Buscar por documento (un resultado)
            print_centrado('BUSQUEDA POR DNI')
            documento = input('ingrese documento: ')
            id = buscar_unico(registro_clientes,'documento',documento)
            if id:
                print_centrado(registro_clientes[id])  
            else:
                print_centrado('No se encontro cliente en base de datos')
        case '3':   #Buscar por apellido (uno o mas resultados)
            print_centrado('LISTAR POR APELLIDO')
            apellido = input('ingrese apellido: ').lower()
            lista_id = buscar_multiple(registro_clientes,'apellido',apellido)
            if len(lista_id) != 0:
                for id in lista_id:
                    print_centrado(registro_clientes[id])
            else:
                print_centrado('No se encontro clientes en base de datos')
        case '4':   #Buscar por nombre (uno o mas resultados)
            print_centrado('LISTAR POR NOMBRE')
            nombre = input('ingrese nombre: ').lower()
            lista_id = buscar_multiple(registro_clientes,'nombre',nombre)
            if len(lista_id) != 0:
                for id in lista_id:
                    print_centrado(registro_clientes[id])
            else:
                print_centrado('No se encontro clientes en base de datos')  
        case '5':   #Editar
            print_centrado('EDITAR')
            documento = input('ingrese documento: ')
            id = buscar_unico(registro_clientes,'documento',documento)
            if id:
                print_centrado(registro_clientes[id])
                editar_registro('clientes.json',registro_clientes,id)
            else:
                print_centrado('No se encontro cliente')               
        case '6':   #eliminar cliente
            print_centrado('ELIMINAR')
            documento = input('ingrese documento: ')
            id = buscar_unico(registro_clientes,'documento',documento)
            if id:
                eliminar_registro('clientes.json',registro_clientes,id)
            else:
                print_centrado('No se encontro clientes')
        case 's':   #Volver al Menu Principal
            menu_principal()

def menu_vehiculos():
    opcion = input('\n1 - Registrar\n2 - Buscar por patente\n3 - listar por marca\n4 - Listar por modelo\n5 - Listar por precio de compra\n6 - Listar por precio de venta\n7 - Editar\n8 - Eliminar\nS - Volver al menu principal \n').lower()
    match opcion:
        case '1':   #Crear
            print_centrado('REGISTRAR VEHICULO')
            dominio = input('Ingrese dominio: ').lower()
            marca = input('ingrese marca: ').lower()
            modelo = input('Ingrese modelo: ').lower()
            tipo = input('Ingrese tipo de vehiculo: ').lower()
            año = input('ingrese año del modelo: ').lower()
            kilometraje = input('Ingrese kilometraje: ').lower()
            precio_compra = input('Ingrese precio de compra: ').lower()
            precio_venta = input('Ingrese precio de venta: ').lower()
            estado = input('Ingrese estado (Disponible, Reservado, Vendido): ').lower()
            registrar_vehiculo(dominio,marca,modelo,tipo,año,kilometraje,precio_compra,precio_venta,estado)
            print_centrado('Vehiculo registrado con exito!')
        case '2':   #Buscar por patente (un resultado)
            print_centrado('BUSQUEDA POR DOMINIO')
            dominio = input('ingrese dominio del vehiculo: ').lower()
            id = buscar_unico(registro_vehiculos,'dominio',dominio)
            if id:
                print_centrado(registro_vehiculos[id]) 
            else:
                print_centrado('No se encontro vehiculo')
        case '3':   #Buscar por marca (uno o mas resultados)
            print_centrado('LISTAR POR MARCA')
            marca = input('ingrese marca: ').lower()
            lista_id = buscar_multiple(registro_vehiculos,'marca',marca)
            if len(lista_id) != 0:
                for id in lista_id:
                    print_centrado(registro_vehiculos[id])
            else:
                print_centrado('No se encontro vehiculo')
        case '4':   #Buscar por modelo (uno o mas resultados)
            print_centrado('LISTAR POR MODELO')
            modelo = input('ingrese modelo: ').lower()
            lista_id = buscar_multiple(registro_vehiculos,'modelo',modelo)
            if len(lista_id) != 0:
                for id in lista_id:
                    print_centrado(registro_vehiculos[id])
            else:
                print_centrado('No se encontro vehiculo')    
        case '5':   #Buscar por precio de compra (uno o mas resultados)
            print_centrado('LISTAR POR PRECIO DE COMPRA')
            precio_compra = input('ingrese precio de compra: ')
            lista_id = buscar_multiple(registro_vehiculos,'precio_compra',precio_compra)
            if len(lista_id) != 0:
                for id in lista_id:
                    print_centrado(registro_vehiculos[id])
            else:
                print_centrado('No se encontro vehiculo')
        case '6':   #Buscar por precio de venta (uno o mas resultados)
            print_centrado('LISTAR POR PRECIO DE VENTA')
            precio_venta = input('ingrese precio de venta: ')
            lista_id = buscar_multiple(registro_vehiculos,'precio_venta',precio_venta)
            if len(lista_id) != 0:
                for id in lista_id:
                    print_centrado(registro_vehiculos[id])
            else:
                print_centrado('No se encontro vehiculo')
        case '7':   #Editar
                print_centrado('EDITAR')
                dominio = input('ingrese dominio del vehiculo: ').lower()
                id = buscar_unico(registro_vehiculos,'dominio',dominio)
                if id:
                    print_centrado(registro_vehiculos[id])
                    editar_registro('vehiculos.json',registro_vehiculos,id)
                else:
                    print_centrado('No se encontro vehiculo')                   
        case '8':   #Eliminar
                print_centrado('ELIMINAR')
                dominio = input('ingrese dominio del vehiculo: ').lower()
                id = buscar_unico(registro_vehiculos,'dominio',dominio)
                if id:
                    eliminar_registro('vehiculos.json',registro_vehiculos,id)
                else:
                    print_centrado('No se encontro vehiculo')
        case 's':   #Volver al Menu Principal
            menu_principal()

def menu_transacciones():
    opcion = input('\n1 - Registrar transaccion\n2 - Listado de transacciones de compra y venta\nS - Volver al menu principal\n').lower()
    match opcion:
        case '1':   #Crear
            print_centrado('REGISTRAR TRANSACCION')
            while True:
                tipo = input('Ingrese tipo de transaccion (compra/venta): ').lower()
                if tipo == 'compra' or 'venta':
                    break
                print_centrado('Tipo incorrecto')
            while True:
                dominio = input('Ingrese dominio del vehiculo: ').lower()
                id_vehiculo = buscar_unico(registro_vehiculos,'dominio',dominio)
                print_centrado(registro_vehiculos[id_vehiculo])
                if (tipo == 'venta') and (registro_vehiculos[id_vehiculo]['estado'] == 'vendido'):
                    print(f'El vehiculo con dominio: {dominio} ya esta vendido')
                else:
                    break
            documento = input('Ingrese documento del cliente: ')
            id_cliente = buscar_unico(registro_clientes,'documento',documento)
            print_centrado(registro_clientes[id_cliente])
            monto = input('Ingrese monto: ').lower()
            observaciones = input('Ingrese Observaciones: ').lower()
            registrar_transaccion(id_vehiculo,id_cliente,tipo,monto,observaciones)
            if tipo == 'venta':
                registro_vehiculos[id_vehiculo]['estado'] = 'vendido'
                Manejo_archivos.guardar_archivo('vehiculos.json',registro_vehiculos)
            print_centrado('Transaccion registrada con exito!')
        case '2':   #Listar
            opcion = input('1 - Buscar por dominio de vehiculo\n2 - Buscar por documento de cliente\n3 - Buscar por rango de fechas\n')
            match opcion:
                case '1':   #Buscar por dominio
                    print_centrado('BUSQUEDA POR DOMINIO')
                    dominio = input('Ingrese dominio del vehiculo: ').lower()
                    id_vehiculo = buscar_unico(registro_vehiculos,'dominio',dominio)
                    lista_id = buscar_multiple(registro_transacciones,'id_vehiculo',id_vehiculo)  #lista de IDs de transacciones asociadas
                    imprimir_listado_transacciones(lista_id)
                case '2':   #Buscar por DNI
                    print_centrado('\nBUSQUEDA POR DNI\n')
                    documento = input('Ingrese documento del cliente: ')
                    id_cliente = buscar_unico(registro_clientes,'documento',documento)
                    lista_id = buscar_multiple(registro_transacciones,'id_cliente',id_cliente)    #lista de IDs de transacciones asociadas
                    imprimir_listado_transacciones(lista_id)
                case '3':   #Buscar por rango de fechas
                    print_centrado('LISTAR POR FECHAS')
                    while True:
                        fecha_inicio = input('Ingrese fecha de inicio (formato dd/mm/aaaa): ')
                        if (fecha_inicio[2] and fecha_inicio[5]) == '/':
                            break
                    while True:
                        fecha_final = input('Ingrese fecha final (formato dd/mm/aaaa): ')
                        if (fecha_final[2] and fecha_final[5]) == '/':
                            break
                    lista_id = buscar_transacciones_fechas(fecha_inicio,fecha_final)  #lista de IDs de transacciones asociadas
                    imprimir_listado_transacciones(lista_id)
        case 's':   #Volver al Menu Principal
            menu_principal()

menu_principal()



