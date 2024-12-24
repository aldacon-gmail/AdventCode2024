import re
import numpy as np

def leer_archivo(ruta_archivo):
    array_letras = []
    with open(ruta_archivo, mode="r") as archivo:
        for line in archivo:
            linea = line.strip()
            array_letras.append(re.findall(r'.',linea))

    return array_letras

def localizar_letras(texto):

    letras = {}

    fil = 0

    filas = len(texto)
    columnas = len(texto[0])

    while fil < filas:
        col = 0
        while col < columnas:
            letra = texto[fil][col]
            posicion = [fil, col]
            if letra != '.':
                if letra not in letras:
                    letras[letra] = [posicion]
                else:
                    letras[letra].append(posicion)
            col += 1
        fil += 1


    return letras

def localizar_antidodes(frequencies):


    antinodes = {}
    for frequency in frequencies:

        posiciones = frequencies[frequency]
        num_posiciones = len(posiciones)
        posicion = 0
        antinodes[frequency] = []

 
        while posicion < num_posiciones:
            next_position = posicion +1
            
            posicion_inicial = np.array([posiciones[posicion][0],posiciones[posicion][1]])
            while next_position < num_posiciones:
                posicion_final = np.array([posiciones[next_position][0],posiciones[next_position][1]])

                distancia = posicion_final - posicion_inicial
                antinodes[frequency].append(posicion_inicial - distancia)
                antinodes[frequency].append(posicion_final + distancia)
                next_position += 1
            posicion += 1

    return antinodes

def localizar_n_antidodes(frequencies):


    antinodes = {}
    for frequency in frequencies:

        posiciones = frequencies[frequency]
        num_posiciones = len(posiciones)
        posicion = 0
        antinodes[frequency] = []

 
        while posicion < num_posiciones:
            next_position = posicion +1
            
            posicion_inicial = np.array([posiciones[posicion][0],posiciones[posicion][1]])
            while next_position < num_posiciones:
                posicion_final = np.array([posiciones[next_position][0],posiciones[next_position][1]])

                distancia = posicion_final - posicion_inicial

                n = 0

                while n < 50:
                    antinodes[frequency].append(posicion_inicial - n*distancia)
                    antinodes[frequency].append(posicion_final + n*distancia)
                    n += 1

                next_position += 1
            posicion += 1

    return antinodes
                
def unico(posicion, lista_posiciones):

    for elemento in lista_posiciones:
        if (elemento[0] == posicion[0]) and (elemento[1] == posicion[1]):
            return False

    return True

def limpiar_antinodes(antinodes, max_filas, max_columnas):

    lista_limpia = []

    for antinode in antinodes:


        for posicion_antinode in antinodes[antinode]:

            if ((posicion_antinode[0] >= 0) and (posicion_antinode[0] <= max_filas) and 
               (posicion_antinode[1] >= 0) and (posicion_antinode[1] <= max_columnas) and
               unico(posicion_antinode, lista_limpia)):
                lista_limpia.append(posicion_antinode)

    return lista_limpia 



# Ruta de entrada y salida
ruta_entrada = "/Users/david.conejero/Documents/AdventCode2024/input_day8.txt"

texto = leer_archivo(ruta_entrada)
print(len(texto))
print(len(texto[0]))

frequencies = {}
frequencies = localizar_letras(texto)
antinodes = localizar_antidodes(frequencies)
antinodes_limpios = limpiar_antinodes(antinodes, len(texto)-1, len(texto[0])-1)





print(frequencies)
print(antinodes)
print('limpios', antinodes_limpios)
print(len(antinodes_limpios))
print(frequencies.keys())


#segunda parte

n_antinodes = localizar_n_antidodes(frequencies)
n_antinodes_limpios = limpiar_antinodes(n_antinodes, len(texto)-1, len(texto[0])-1)
print(len(n_antinodes_limpios))


#for elemento in antinodes_limpios:
#    texto[elemento[0]][elemento[1]] = '#'

#for linea in texto:
#    print(linea)




