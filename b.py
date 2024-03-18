def insertar(cadena, ch):
    return ch.join(cadena)

def reemplazar(cadena, ch):
    return cadena.replace(" ", ch)

# Programa principal
cad = input("Ingresá una cadena de caracteres: ")
caracter = input("Ingresá un carácter: ")
cad2 = insertar(cad, caracter)
cad3 = reemplazar(cad, caracter)
print()
print(cad2)
print(cad3)