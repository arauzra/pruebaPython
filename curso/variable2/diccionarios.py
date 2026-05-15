#creando diccionario con dict()
diccionario = dict(nombre="Rafael", edad=18, altura=1.71, es_estudiante=True)

#las listas no pueden ser claves de un diccionario porque son mutables,
# pero las tuplas sí porque son inmutables. Usamos frozenset para crear
# un conjunto inmutable que también puede ser clave de un diccionario

diccionario = { frozenset({"nombre", "apellido"}): "Rafael Arauz" }

#crear un diccionarion con fromkeys() a partir de una lista de claves
diccionario = dict.fromkeys(["nombre", "edad", "altura", "es_estudiante"])

#crear un diccionario con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(("nombre", "edad", "altura", "es_estudiante"), "no se")

print(diccionario)