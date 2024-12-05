import csv
import operator

# Función para leer el archivo CSV y extraer las conexiones origen-destino
def leer_conexiones_csv(ruta_archivo):
    lista_origen = []
    lista_destino = []
    lista_origen_destino = []
    with open(ruta_archivo, mode="r") as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            if len(fila) >= 2:
                origen, destino = fila[0].strip(), fila[1].strip()
                lista_origen.append(int(origen))
                lista_destino.append(int(destino)) 
    
    lista_origen_destino.append(lista_origen)
    lista_origen_destino.append(lista_destino)
    
    return lista_origen_destino


# Función para construir el grafo
def construir_grafo(lista_origen_destino):
    grafo = defaultdict(list)
    for origen, destino in lista_origen_destino:
        if destino != "END":
            grafo[origen].append(destino)
    return grafo


# Función para calcular la distancia entre dos listas
def calcular_distancia_listas(lista_origen, lista_destino):
	
	suma = 0
	count = -1
	for origen in lista_origen:
		count += 1
		suma += abs(origen - lista_destino[count])

	return suma

def similitary_score(lista_origen,lista_destino):

	score = 0
	origen_en_destino = {}

	for origen in lista_origen:

		if origen in origen_en_destino:
			count = origen_en_destino[origen]
		else:
			count = 0
			for destino in lista_destino:
				if destino == origen:
					count += 1

			origen_en_destino[origen] = count

		score += origen * count

	return score

# Ruta de entrada y salida
ruta_entrada = "/Users/david.conejero/Documents/AdventCode2024/input.csv"



lista_origen_destino = leer_conexiones_csv(ruta_entrada) 

origen_ordenado = lista_origen_destino[0]

total = calcular_distancia_listas(sorted(lista_origen_destino[0]), sorted(lista_origen_destino[1]))
print(total)

new_list = list(map(operator.sub, sorted(lista_origen_destino[0]), sorted(lista_origen_destino[1])))
total2 = 0
for item in new_list:
	total2 += abs(item)

print(total2)

final_score = similitary_score(lista_origen_destino[0], lista_origen_destino[1])
print (final_score)

