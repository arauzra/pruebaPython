print("Dame un texto y te digo cuántas palabras tiene")

texto_usuario = input("Ingresa tu texto: ").strip() # .strip() elimina espacios al inicio y al final

# parámetros
PALABRAS_POR_SEGUNDO = 2
VELOCIDAD_DALTO = 1.3

# conteo de palabras
palabras = texto_usuario.split()
cantidad_palabras = len(palabras)

print(f"Tu texto tiene {cantidad_palabras} palabras.")

# tiempo hablando
tiempo_hablando = cantidad_palabras / PALABRAS_POR_SEGUNDO

if tiempo_hablando > 60:
    print("Calmate, tampoco te pedí un testamento 😅")
else:
    print(
        f"Si lo dijeras en voz alta, te tomaría "
        f"{tiempo_hablando:.1f} segundos."
    )

# tiempo estilo Dalto
tiempo_dalto = tiempo_hablando / VELOCIDAD_DALTO

print(
    f"Si lo dijeras como Dalto, te tomaría "
    f"{tiempo_dalto:.1f} segundos."
)