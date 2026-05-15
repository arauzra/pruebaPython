
print("--- Analizador de Texto ---")
texto_usuario = input("Ingresa tu texto: ").strip()
    
if not texto_usuario:
        print("No ingresaste ningún texto. Intenta de nuevo.")
        
cantidad_palabras = len(texto_usuario.split())
print(f"\nTu texto tiene {cantidad_palabras} palabras.")

 # Constantes
PALABRAS_POR_SEGUNDO = 2
VELOCIDAD_DALTO = 1.3

 # Cálculos
tiempo_hablando = cantidad_palabras / PALABRAS_POR_SEGUNDO
tiempo_dalto = tiempo_hablando / VELOCIDAD_DALTO

if tiempo_hablando > 60:
        print("Calmate dog, tampoco te pedí un testamento.")
else:
        print(f"Si lo dijeras en voz alta, te llevaría {tiempo_hablando:.1f} segundos decirlo.")

print(f"Si lo dijera Dalto (30% más rápido), le llevaría {tiempo_dalto:.1f} segundos decirlo.")

