
#creando una lista con la función list()
lista = list([80,34])

#devuelve el número de elementos de la lista
cantidad_elementos = len(lista)

#agregando un nuevo elemento a la lista con el método append()
agregando_con_append = lista.append("12")

#agregar 8 elementos a la lista con el método insert()
lista.insert(0, "primero")

#agregar un elemento al final de la lista con el método extend()
lista.extend([300])

lista.pop(2) #elimina el elemento en el índice 2 de la lista

lista.remove ("primero") #elimina un elemento por su valor, en este caso "primero"

#eliminar todos los elementos de la lista con el método clear()
#lista.clear()


lista.sort(reverse = True) 
#ordena la lista de forma ascendente, (reverse = True) ordena de forma descendente

lista.reverse() #invierte el orden de los elementos en la lista

lista.index(34) #devuelve el índice del primer elemento que coincide con el valor especificado, en este caso 34

print(cantidad_elementos)

