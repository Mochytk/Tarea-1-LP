from logging import info


grafo = {} # El grafo va a ser representado como un diccionario, con la clave siendo el rut, más detalles más adelante

def agregar_nodo(rut, nombre, l_prod):                          
    ventas = []                                                 
    compras = []                                                
    grafo.update({rut: [nombre, l_prod, compras, ventas]})      

# def agregar_nodo(rut, nombre, l_prod):
# rut: Un string con el rut de la empresa
# nombre: Un string con el nombre de la empresa
# l_prod: Una lista con todos los productos de la empresa
#
# Tipo de retorno: None
#
# Cuando se llama la función agregar_nodo, se crean dos listas, una de
# compras y una de ventas, entonces se le hace update al grafo, añadiendo
# un elemento, con su key siendo el rut y la data que guarda siendo una lista
# con el nombre, la lista de productos, la lista de compras y la lista de ventas
#
# Nota: Las listas de compras y ventas empiezan vacías porque recién se están agregando
# las empresas y no vienen con ninguna venta o compra.
#

def agregar_arco(comprador, vendedor, venta):
    for nodo, info in grafo.items():
        if nodo == vendedor or info[0] == vendedor:
            info[3].append(venta)
        if nodo == comprador or info[0] == comprador:
            info[2].append(venta)

# def agregar_arco(comprador, vendedor, venta):
# comprador: String con el rut o el nombre del comprador
# vendedor: String con el rut o el nombre del comprador
# venta: Lista con la venta en forma [producto, cantidad]
#
# Tipo de retorno: None.
#
# Cuando se genera una venta, se añade al grafo como arco, primero se busca en el nodo si es
# el rut o en el nombre de la empresa si es ese el caso, esto se representa
# al añadir la venta a la lista de ventas que existe en el gráfico, también
# se añade al comprador la compra en su lista respectiva, esto será útil luego.
#
# Recordar que la entrega mínima es añadir las ventas.
#

def esta_en_grafo (rut):
    for nodo in grafo.items():
        if grafo.get(rut) == nodo:
            return True
    return False

# def esta_en_grafo(rut):
# rut: Un string que contiene el rut de una empresa a revisar.
# 
# Tipo de Retorno: Booleano de True o False.
# 
# Se recorre el grafo y si la empresa existe retorna True.
# Y  si no, retorna False.
# 