# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

print("Veamos algunas comparaciones:") 

if texto_1 > texto_2:
    print('{} es mayor que {}'.format(texto_1, texto_2))
else:
    print('{} es mayor que {}'.format(texto_2, texto_1))

if len(texto_1) > len(texto_2):
    print('{} contiene mas caracteres que {}'.format(texto_1, texto_2))
else:     
    print('{} contiene mas caracteres que {}'.format(texto_2, texto_1))

primer_caracter1 = texto_1[0]
primer_caracter2 = texto_2[0] 

if primer_caracter1 > primer_caracter2:
    print("{} , El primer caracter de la primera palabra,  es mayor que: {} , el de la segunda ".format(primer_caracter1, primer_caracter2))
else:     
    print('{} , El primer caracter de la segunda palabra  es mayor que: {} , el de la primera '.format(primer_caracter2, primer_caracter1))

if copia_texto_1 == texto_1:
    print(copia_texto_1 , "es iagual a:" , texto_1)

if copia_texto_1 != texto_1:
    print(copia_texto_1 , "es distinto a:" , texto_1)