import re

def leer_archivo(ruta_archivo):
    array_letras = []
    with open(ruta_archivo, mode="r") as archivo:
        for line in archivo:
            linea = line.strip()
            array_letras.append(re.findall(r'.',linea))



    return array_letras

def num_xmas(matriz, fil, col):

    vector = [-1,0,1]
    is_mas = ['M','A','S']

    num = 0

    for posicion_x in vector:
        for posicion_y in vector:
            if (posicion_x != 0 or posicion_y != 0) and (0 <= fil+3*posicion_x < len(matriz)) and (0 <= col+3*posicion_y < len(matriz[fil])):
 #               print("entro: ", fil, col, posicion_x, posicion_y, matriz[fil][col], num)
                paso = 1
                for letter in is_mas:
 #                   print(matriz[fil+posicion_x*paso][col+posicion_y*paso])
                    if letter != matriz[fil+posicion_x*paso][col+posicion_y*paso]:
                        break;
                    paso += 1
                if paso == 4:
                    num += 1

    return num


#                print("entro: ", fil, col, posicion_x, posicion_y, fil+4*posicion_x, col+4*posicion_y, len(matriz), len(matriz[fil]))
#                print(matriz[fil+4*posicion_x][col+4*posicion_y])
#            else:
#                print("fuera", fil, col, posicion_x, posicion_y, fil+1+4*posicion_x, col+1+4*posicion_y, len(matriz), len(matriz[fil]))


    return num

# Ruta de entrada y salida
ruta_entrada = "/Users/david.conejero/Documents/AdventCode2024/input_day4"

texto = leer_archivo(ruta_entrada)

fil = 0
col = 0
total_xmas = 0

while fil < len(texto):
    while col < len(texto[fil]):
        if texto[fil][col] == 'X':
            total_xmas += num_xmas(texto, fil, col)
 #           print("total: ", total)
        col += 1
    fil += 1
    col = 0


total_X_mas = 0

pos = [-1, 1]
for value_x in range(len(texto)):
    for value_y in range(len(texto[value_x])):
        if texto[value_x][value_y] == "A":
            num_m = 0
            num_s = 0

            # Si las Ms y Ss estan en diagonal, la palbra es MAM SAS. 
            # Estos casos se dan si las Ms (o las Ss) estan en la diagonal es decir [-1,-1][1, 1] o [-1,1][1,-1]
            # así que eliminaremos los casos en las q las Ms esten en diagonal (-1*-1)+(1*1)
            # Si no estan en diagonal su situación será [1,1][1,-1] o cualquiera de estas combinaciones
            diagonal = 0
            
            for px in pos:
                for py in pos:
                    try:
                        if texto[value_x+px][value_y+py] == "M":
                            num_m += 1
                            diagonal += px*py
                        if texto[value_x+px][value_y+py] == "S":
                            num_s += 1
                    except:
                        break;

            if num_m == 2 and num_s == 2 and diagonal == 0:
                total_X_mas += 1

        


print(total_xmas, total_X_mas)

