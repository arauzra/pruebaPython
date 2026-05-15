#pedirle un numero al usuario
numero = input("Ingrese un numero: ")
#el dato ingresado por el usuario es un texto, para convertirlo a numero
#utilizamos la funcion int() para convertirlo a entero
numero = int(numero) * 2
print ("El numero ingresado es: " + str(numero)) #concatenamos el texto con el 
#numero ingresado por el usuario
