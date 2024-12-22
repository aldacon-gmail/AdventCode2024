import re
from collections import defaultdict

def leer_archivo(ruta_archivo):
    array_numeros = []
    with open(ruta_archivo, mode="r") as archivo:
        for linea in archivo:
            linea = linea.replace(':', '')
            line = linea.strip()
            array_numeros.append([int(x) for x in line.split(" ")])
    return array_numeros

def operar(operacion, numero_1, numero_2):
    if (operacion == 'sumar'):
        return numero_1 + numero_2
    else: 
        return numero_1 * numero_2

def genera_operaciones(vector_inicial, cantidad):

#    print(vector_inicial, cantidad, len(vector_inicial), pow(2,cantidad))

    if len(vector_inicial) == pow(2,cantidad):
        return vector_inicial
    else:
        vector_final = []
        for entrada in vector_inicial:
            nueva_entrada_1 = entrada.copy()
            nueva_entrada_1.append('sumar')
            nueva_entrada_2 = entrada.copy()
            nueva_entrada_2.append('multiplicar')                                   
            vector_final.append(nueva_entrada_1)
            vector_final.append(nueva_entrada_2)

        vector_final = genera_operaciones(vector_final, cantidad)

    return vector_final


def calculo_valido(numeros):
    resultado = numeros.pop(0)
    


    posibles_operaciones = genera_operaciones([['sumar'], ['multiplicar']],len(numeros)-1)
#    print (numeros, len(numeros)-1, posibles_operaciones)

    for lista_operaciones in posibles_operaciones:
        resultado_posible = numeros[0]
        contador = 0
        while contador < len(lista_operaciones):
            resultado_posible = operar(lista_operaciones[contador],resultado_posible, numeros[contador+1])
            contador += 1

#        print (numeros, lista_operaciones, resultado, resultado_posible)
        if resultado == resultado_posible:
            return resultado

    return 0




def operar_2(operacion, numero_1, numero_2):
    if (operacion == 'sumar'):
        return numero_1 + numero_2
    elif (operacion == 'multiplicar'):
        return numero_1 * numero_2
    else:
        return int(str(numero_1)+str(numero_2))

def genera_operaciones_2(vector_inicial, cantidad):


    if len(vector_inicial) == pow(3,cantidad):
        return vector_inicial
    else:
        vector_final = []
        for entrada in vector_inicial:
            nueva_entrada_1 = entrada.copy()
            nueva_entrada_1.append('sumar')
            nueva_entrada_2 = entrada.copy()
            nueva_entrada_2.append('multiplicar')                                   
            nueva_entrada_3 = entrada.copy()
            nueva_entrada_3.append('||')                                   
            vector_final.append(nueva_entrada_1)
            vector_final.append(nueva_entrada_2)
            vector_final.append(nueva_entrada_3)

        vector_final = genera_operaciones_2(vector_final, cantidad)

    return vector_final


def calculo_valido_2(numeros):
    resultado = numeros.pop(0)
    
    posibles_operaciones = genera_operaciones_2([['sumar'], ['multiplicar'], ['||']],len(numeros)-1)

    for lista_operaciones in posibles_operaciones:
        resultado_posible = numeros[0]
        contador = 0
        while contador < len(lista_operaciones):
            resultado_posible = operar_2(lista_operaciones[contador],resultado_posible, numeros[contador+1])
            contador += 1

        if resultado == resultado_posible:
            return resultado

    return 0




# Ruta de entrada y salida
ruta_entrada = "/Users/davidconejero/Documents/github/AdventCode2024/input_day7.txt"

a_evaluar = leer_archivo(ruta_entrada)

print(a_evaluar)

# operaciones para resolver la primera parte del problema
#total = 0
#for entrada in a_evaluar:
#    total += calculo_valido(entrada)

#print(total)
# operaciones para resolver la segunda parte del problema
total_2 = 0
for entrada in a_evaluar:
    total_2 += calculo_valido_2(entrada)

print(total_2)
