diccionario = {
    "nombre": "Rafael",
    "edad": 18,
    "altura": 1.71,
    "es_estudiante": True,
    0: "cero"
}

claves = diccionario.keys()
#keys nos sirve para obtener una vista de las claves del diccionario, 
# tambien nos sirve para iterar sobre las claves del diccionario en un bucle for

clave1 = diccionario[0] #nos sirve para acceder al valor asociado a una clave específica, en este caso la clave es 0, 
#si la clave no existe, se lanzará un error KeyError.
valor_de_nombre = diccionario.get("nombre")
#get nos sirve para obtener el valor asociado a una clave específica, si la clave no existe,
#devuelve None en lugar de lanzar un error.

#diccionario.clear()    #clear nos sirve para eliminar todos los elementos del diccionario, dejándolo vacío.

diccionario.pop("nombre") #pop nos sirve para eliminar un elemento específico del diccionario,
#en este caso la clave es "nombre", si la clave no existe, se lanzará un error KeyError.

diccionario_iterable = diccionario.items() #items nos sirve para obtener una vista de los pares clave-valor del diccionario,
#también nos sirve para iterar sobre los pares clave-valor del diccionario en un bucle for.

print ("el programa continua ejecutándose")
print (diccionario_iterable) 

