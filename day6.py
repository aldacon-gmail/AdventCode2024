import re
from collections import defaultdict

movimientos = {'UP':[-1,0],"RIGHT":[0,1],"LEFT":[0,-1],"DOWN":[1,0]}
giro = {'UP':'RIGHT','RIGHT':'DOWN','DOWN':'LEFT','LEFT':'UP'}

def leer_archivo(ruta_archivo):
    array_obstaculos = []
    with open(ruta_archivo, mode="r") as archivo:
        cont = 0
        for linea in archivo:
            line = linea.strip()
            array_obstaculos.append(list(line))
            if '^' in line:
                posicion_inicial = [cont,line.find('^')]
            cont += 1
    return posicion_inicial, array_obstaculos

def mover(mapa,fila,columna,direccion):

    new_fila = 0
    new_ = 0
    # seguir el camino
    new_fila =  fila + movimientos[direccion][0]
    new_columna =  columna + movimientos[direccion][1]

#    print(new_fila,new_columna)

    if (0 <= new_fila < len(mapa)) and (0 <= new_columna < len(mapa[fila])):
        if '#' in mapa[new_fila][new_columna]:
#            print('entro', mapa[new_fila][new_columna], new_fila, new_columna)
            direccion = giro[direccion]
            return True, fila, columna, direccion
        else:
            return True, new_fila, new_columna, direccion
    else:
        return False, fila, columna, direccion


def recorrer_mapa(fila, columna, opcion):

    mapa = [list(row) for row in opcion]

    direccion = 'UP'


    loop = True
    while loop:
        if direccion in mapa[fila][columna]:
            return True
        else:
            mapa[fila][columna] = mapa[fila][columna] + direccion

        loop, fila, columna, direccion = mover(mapa,fila,columna,direccion)

    return False

# Ruta de entrada y salida
ruta_entrada = "/Users/david.conejero/Documents/AdventCode2024/input_day6.txt"

[fila,columna], mapa = leer_archivo(ruta_entrada)
direccion = 'UP'

fila_inicial = fila
columna_inicial = columna

en_el_mapa = True
contador = 0

while en_el_mapa:
    if mapa[fila][columna] != "X":
        mapa[fila][columna] = "X"
        contador += 1

    en_el_mapa, fila, columna, direccion = mover(mapa,fila,columna,direccion)
#    print(loop, fila, columna, direccion)



# validate all possible blockers to loop the survaillance
fil = 0
total_loops = 0

for linea in mapa:
    col = 0
    for posicion in mapa[fil]:
        if 'X' in posicion and (fila != fila_inicial or col != columna_inicial):
            mapa[fil][col] = mapa[fil][col] + '#'

            loop = recorrer_mapa(fila_inicial, columna_inicial, mapa)        
            if loop:
                total_loops += 1

            mapa[fil][col] = 'X'
        col += 1
    fil += 1






print(contador, total_loops)
