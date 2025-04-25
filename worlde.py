print("Bienvenido a Penword Adivina la palabra de 5 letras tienes 6 intentos.")
print("Significados")
print("🟩=Letra de la palabra oculta en la posicion correcta")
print("🟨=Letra existente en la palabra oculta en la posicion incorrecta")
print("⬜=La letra no esta en la palabra oculta")
intentos=6
longitud=5
palabra_oculta="plomo"
def obtener_fila_verificada(palabra_oculta, palabra_usuario):
    resultado = ""
    for i in range(len(palabra_usuario)):
        if palabra_usuario[i] == palabra_oculta[i]:
            resultado += f"{palabra_usuario[i]}🟩 "
        elif palabra_usuario[i] in palabra_oculta:
            resultado += f"{palabra_usuario[i]}🟨 "
        else:
            resultado += f"{palabra_usuario[i]}⬜ "
    return resultado



for intento in range(1, intentos + 1):
    palabra_usuario = input(f"Intento {intento}/{intentos}: Ingresa una palabra de {longitud} letras: ")
    
    if len(palabra_usuario) != longitud:
        print(f"La palabra debe tener exactamente {longitud} letras.")
        continue
    
    if palabra_usuario == palabra_oculta:
        print("¡Felicidades! Adivinaste la palabra.")
        break

    linea_verificada = obtener_fila_verificada(palabra_oculta, palabra_usuario)
    print("Resultado:", ''.join(linea_verificada))
else:
    print(f"Lo siento, no adivinaste la palabra. La palabra era '{palabra_oculta}'.")