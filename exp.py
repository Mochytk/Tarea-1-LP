import re

p_n_emp = re.compile("[A-Z]([a-z]|[A-Z]|\s|\d|\-)*")                                    # ER para el nombre de la empresa

p_rut = re.compile("[1-9]([0-9])*\-(\d|k)")                                             # Para el RUT

p_id = re.compile("\#([A-Z]|[1-9])([A-Z]|[\d])+")                                       # Para el ID de los productos

p_precio = re.compile("\$[1-9](\d)?(\d)?(\.\d\d\d)+")                                   # Para el precio

p_nom_prod = re.compile("([a-z]|\d)([a-z]|\d|\.|\-)+")                                  # Para el nombre de los productos

p_prod = re.compile(f"({p_id.pattern})\-({p_precio.pattern})\-({p_nom_prod.pattern})")  # Para los productos

p_list_pro = re.compile(f"\[({p_prod.pattern})(\,({p_prod.pattern}))*\]")               # Para la lista de productos

p_emp_ent = re.compile(f"{p_n_emp.pattern}\.{p_rut.pattern}\.{p_list_pro.pattern}")     # Para la empresa entera

p_num_dec = re.compile("(0|[1-9][\d]*)\.[\d]*[1-9]")                                    # Para el numero decimal

p_venta = re.compile(f"\(({p_n_emp.pattern}|{p_rut.pattern})\.({p_nom_prod.pattern}|{p_id.pattern})\-\>({p_n_emp.pattern}|{p_rut.pattern})\.x({p_num_dec.pattern})\)") # Para las ventas

p_v_emp = re.compile(f"ver_empresa\s({p_n_emp.pattern}|{p_rut.pattern})")               # Para ver los datos de una empresa

p_v_v = re.compile(f"ver_ventas\s({p_n_emp.pattern}|{p_rut.pattern})")                  # Para ver las ventas de una empresa

p_bus_mp = re.compile(f"buscar_MP\s({p_n_emp.pattern}|{p_rut.pattern})")                # Para buscar al productor de MP de todos los productos que ha comprado una empresa en especifico