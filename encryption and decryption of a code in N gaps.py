# Función para normalizar el texto
def normalizar_texto(texto):
    # Convertir a minúsculas
    texto = texto.lower()
    # Reemplazar vocales con tilde por sus equivalentes sin tilde
    reemplazos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u', 'ñ': 'n'}
    texto_normalizado = ""
    for caracter in texto:
        if caracter in reemplazos:
            texto_normalizado += reemplazos[caracter]
        elif 'a' <= caracter <= 'z' or caracter == ' ':  # Generar los espacios
            texto_normalizado += caracter
    return texto_normalizado

# Función para descifrar y cifrar texto
def traducir_texto(texto, n):
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    texto_traducido = ""
    
    for caracter in texto:
        if caracter in abecedario:
            # Encontrar la posición del caracter y mover n lugares hacia la derecha
            indice = abecedario.index(caracter)
            nuevo_indice = (indice + n) % 26  # 26 es la longitud del abecedario
            texto_traducido += abecedario[nuevo_indice]
        else:
            # Mantener espacios y otros caracteres tal cual los escribio la persona
            texto_traducido += caracter
    
    return texto_traducido


# Definir la funcionalidad del programa a ejecutar
funcionalidad= input("Si quiere descifrar un texto escriba \"d\" y para cifrarlo ingrese \"c\": " )

# Validación de datos
while funcionalidad !="d" and funcionalidad!="c":
    funcionalidad= input("Instrucción incorrecta, si quiere descifrar un texto escriba \"d\" y para cifrarlo ingrese \"c\": ")

# Leer el texto a descifrar/cifrar el número de saltos
texto = input("Introduce el texto a traducir: ")
n = int(input("Introduce el número de saltos (N): "))

# Normalizar el texto
texto_normalizado = normalizar_texto(texto)

# Descifrar el texto normalizado e imprimirlo en caso de que sea lo solicitado
if funcionalidad== "d":
    texto_traducido = traducir_texto(texto_normalizado, n)
    print(f"Código descifrado: {texto_traducido}")

# Cifrar el texto normalizado e imprimirlo en caso de que sea lo solicitado
elif funcionalidad== "c":
    texto_traducido = traducir_texto(texto_normalizado, -n)
    print(f"Código cifrado: {texto_traducido}")
