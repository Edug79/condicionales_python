# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''



from audioop import lin2adpcm


print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

texto_3 = str(input('Ingrese la tercer palabra:\n'))

l_1 = len(texto_1)
l_2 = len(texto_2)
l_3 = len(texto_3)


print("Si desea ordenar alfabeticamente ingrese: 1")
print("Si desea ordenar por cantidad de letras : 2")
Respuesta = int(input("ingrese opcion deseada por favor: "))


if Respuesta == 1:

    if texto_1 < texto_2 and texto_2 < texto_3: 
        print("{} , {} , {}".format(texto_1,texto_2,texto_3))
    elif texto_1 < texto_3 and texto_3 < texto_2: 
        print("{} ,{} , {}".format(texto_1,texto_3,texto_2))  
    elif texto_2 < texto_3 and texto_3 < texto_1: 
        print("{} , {} , {}".format(texto_2,texto_3,texto_1))  
    elif texto_2 < texto_1 and texto_1 < texto_3: 
        print("{} , {} , {}" .format(texto_2,texto_1,texto_3)) 
    elif texto_3 < texto_1 and texto_1 < texto_2: 
        print("{} , {} , {}".format(texto_3,texto_1,texto_2))  
    elif texto_3 < texto_2 and texto_2 < texto_1: 
        print("{} , {} , {}".format(texto_3,texto_2,texto_1))  
    elif texto_1 < texto_2 and texto_1 < texto_3 and texto_2 == texto_3:
        print("{} , La 2da y 3er palabra tienen el mismo orden alfabetico".format(texto_1))   
    elif texto_2 < texto_1 and texto_2 < texto_3 and  texto_1 == texto_3:
        print("{} , La 1ra y 3er palabra tienen el mismo orden alfabetico".format(texto_2))   
    elif texto_3 < texto_2 and texto_3 < texto_1 and texto_2 == texto_1:
        print("{} , La 1ra y 2da palabra tienen el mismo orden alfabetico".format(texto_3))
    elif texto_3 < texto_1 and texto_2 < texto_1 and texto_2 == texto_3:
        print("{} y {} son iguales y despues sigue {} alfabeticamente ".format(texto_3 , texto_2 , texto_1))  
    elif texto_1 < texto_2 and texto_3 < texto_2 and texto_1 == texto_3:
        print("{} y {} son iguales y despues sigue {} alfabeticamente ".format(texto_1 , texto_3 , texto_2))  

    elif texto_1 == texto_2 == texto_3:
        print("Las tres palabras son iguales y tienen el mismo orden alfabetico")

elif Respuesta == 2:

    if l_1 > l_2 and l_2 > l_3: 
        print("{} , {} , {}".format(texto_1,texto_2,texto_3))
    elif l_1 > l_3 and l_3 > l_2: 
        print("{} ,{} , {}".format(texto_1,texto_3,texto_2))  
    elif l_2 > l_3 and l_3 > l_1: 
        print("{} , {} , {}".format(texto_2,texto_3,texto_1))  
    elif l_2 > l_1 and l_1 > l_3: 
        print("{} , {} , {}" .format(texto_2,texto_1,texto_3)) 
    elif l_3 > l_1 and l_1 > l_2: 
        print("{} , {} , {}".format(texto_3,texto_1,texto_2))  
    elif l_3 > l_2 and l_2 > l_1: 
        print("{} , {} , {}".format(texto_3,texto_2,texto_1))     

    elif l_1 > l_2 and l_1 > l_3 and l_2 == l_3:
        print("La palabra con mas letras es: {} y la 2da y 3er palabra tienen la misma cantidad de letras".format(texto_1))   
    elif l_2 > l_1 and l_2 > l_3 and  l_1 == l_3:
        print("La plabra con mas letras es: {} y la 1ra y 3er palabra tienen la misma cantidad de letras".format(texto_2))   
    elif l_3 > l_2 and l_3 > l_1 and l_2 == l_1:
        print("La palabra con mas letras es: {} y la 1ra y 2da palabra tienen la misma cantidad de letras".format(texto_3))
    elif l_3 > l_1 and l_2 > l_1 and l_2 == l_3:
        print("{} y {}, son las dos palabras con mayor con mas cantidad de letras y despues sigue: {} con menor cantidad de letras ".format(texto_3 , texto_2 , texto_1))  
    elif l_1 > l_2 and l_3 > l_2 and l_1 == l_3:
        print("{} y {} son las dos palabras con mayor con mas cantidad de letras y despues sigue {} con menor cantidad de letras ".format(texto_1 , texto_3 , texto_2))

    elif l_1 == l_2 == l_3:
        print("las tres palabras tienen la misma cantidad de letras!")      
        
print( "Deberia haber una mejor forma de hacer esto escribinedo un poco menos de codigo")   


    

