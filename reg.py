from exp import *
from grafo import *
import re

def procesar_productos(l_prod):                   # def procesar_productos(l_prod):
    lista_prod = []                               # l_prod : Un string con todos los productos
    for producto in p_prod.finditer(l_prod):      #
        index_i = producto.span(0)[0]             # Tipo de retorno: Lista de strings que tienen los productos
        index_f = producto.span(0)[1]             #
        prod = l_prod[index_i:index_f]            # Recorre el string de entrada y va por producto, agregándolos por la cola 
        lista_prod.append(prod)                   # a la lista uno por uno
    return lista_prod                             #

def procesar_empresa(linea):                                            # def procesar_empresa(linea):
    index_f_n = p_n_emp.search(linea).span(0)[1]                        # linea: Un string con la empresa, el rut y la lista de productos
    index_i_l_p = p_list_pro.search(linea).span(0)[0]                   #  
    index_f_l_p = p_list_pro.search(linea).span(0)[1]                   # Tipo de retorno: None
    nombre = linea[0:index_f_n]                                         #
    rut = linea[index_f_n+1:index_i_l_p-1]                              # Encuentra los index donde están los inicios y los finales de cada parte 
    l_p = linea[index_i_l_p:index_f_l_p]                                # para ir separando el nombre, el rut y la lista de productos, creando variables 
    list_producto = procesar_productos(l_p)                             # para cada una, luego se procesan los productos y  se comprueba si la empresa 
    if esta_en_grafo(rut):                                              # ya existe en el grafo, en caso de que no exista, salta un error, en caso opuesto,
        print("La empresa", nombre, " ya está en la base de datos")     # se añadirá sin problemas.
    else:                                                               #
        agregar_nodo(rut, nombre, list_producto)                        #

def procesar_venta(linea): 
    print(linea)                                        # def procesar_venta(linea):
    index_f_linea = p_venta.search(linea).span(0)[1]    # linea: Un string con la venta
    index_f_n = re.search("\.", linea).span(0)[1]       # 
    index_i_n_c = re.search("\-\>", linea).span(0)[0]   # Tipo de retorno: None
    index_f_n_c = re.search("\.x", linea).span(0)[1]    # 
    emp_vend = linea[1:index_f_n-1]                     # De forma similar a la función procesar_empresa, encuentra los index donde esta cada parte de la venta, esta siendo
    emp_comp = linea[index_i_n_c+2:index_f_n_c-2]       # la empresa compradora, la empresa vendedora, el producto de la venta y la cantidad, creando variables para cada una
    producto = linea[index_f_n:index_i_n_c]             # por último se crea la variable venta que será una lista donde estará el producto y la cantidad
    cantidad = linea[index_f_n_c:index_f_linea-1]       # 
    venta = [producto, cantidad]                        # Con todo eso listo se añade como arco al grafo.
    agregar_arco(emp_comp, emp_vend, venta)             # 

def ver_empresa(linea):
    print

def ver_ventas(linea):
    print

def buscar_MP(linea):
    
    print

arch_op = open("Ejemplos de prueba T1/input.txt", "r")

if arch_op.closed:
    print ("Error, el archivo está cerrado")

for line in arch_op:
    line = line.strip()
    if p_emp_ent.match(line):
        procesar_empresa(line)
    if p_venta.match(line):
        procesar_venta(line)
    if p_v_emp.match(line):
        ver_empresa(line)
    if p_v_v.match(line):
        ver_ventas(line)
    if p_bus_mp.match(line):
        buscar_MP(line)