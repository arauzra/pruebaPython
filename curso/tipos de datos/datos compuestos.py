# crear una lista se puede modificar
lista = ["Rafael", 18, 1.71, True]

# crear una tupla no se puede modificar
tupla = ("Rafael", 18, 1.71, True)

# esto es válido
lista[1] = 19

# esto da error porque las tuplas son inmutables
#tupla[1] = 19  

#creando un conjunto (set) (no tiene orden y no permite elementos repetidos)
conjunto = {"Rafael", 18, 1.71, True}

#creando un diccionario (dict)
diccionario = {
    "nombre": "Rafael",
    "edad": 18,
    "altura": 1.71,
    "es_estudiante": True
}

print (diccionario["nombre"])