def operaciones_minimas_para_producto_cero(lista):
    cantidad_ceros = 0
    cantidad_negativos = 0
    
    for numero in lista:
        if numero == 0:
            cantidad_ceros += 1
        elif numero < 0:
            cantidad_negativos += 1
    
    if cantidad_ceros > 0:
        return 0
    
    return cantidad_negativos

n = int(input("Ingrese la cantidad de números en la lista: "))
mi_lista = list(map(int, input("Ingrese los números separados por espacios: ").split()))

resultado = operaciones_minimas_para_producto_cero(mi_lista)
print("El número mínimo de operaciones para que el producto sea 0 es:", resultado)

