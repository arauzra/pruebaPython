cadena1 = "Hola, soy Rafa"
cadena2 = "Bienvenido maquinola"

#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minusculas
minus = cadena2.lower()

#primera letra en mayuscula
primera_l = cadena1.capitalize()

#buscamos una cadena dentro de otra
posicion = cadena1.find("Rafa")  # devuelve el índice de inicio o -1 si no se encuentra

#buscamos una cadena dentro de otra (otra forma)

posicion_index = cadena1.index("Rafa")  # devuelve el índice de inicio o lanza un error si no se encuentra

print(mayusc)
print(minus)
print(primera_l)
print("Posición de 'Rafa':", posicion)

#listar todos los metodos y atributos de un objeto
print(dir(cadena1))