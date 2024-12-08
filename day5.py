import re
from collections import defaultdict

def leer_archivo(ruta_archivo):
    grafo_ordenes = defaultdict(list)
    array_updates = []
    with open(ruta_archivo, mode="r") as archivo:
    	for linea in archivo:
        	line = linea.strip()
        	if "|" in line:
        		antes, despues = line.split('|')
        		grafo_ordenes[int(antes)].append(int(despues))
        	elif "," in line:
        		array_updates.append([int(x) for x in line.split(",")])
    return grafo_ordenes, array_updates

def right_order(lista, ordenes):

	longitud = len(lista)
	for i in range(longitud-1,0,-1):
#		print("i:", i, lista[i])
		for j in range(0,i,1):
#			print("j: ", j, lista[j])
#			print ("pagina: ", lista[j], " está en ordenes lista i: ", ordenes[lista[i]], "?") 
			if lista[j] in ordenes[lista[i]]:
				return False;

	return True

def reorder(lista, ordenes):

	longitud = len(lista)
	for i in range(longitud-1,0,-1):
#		print("i:", i, lista[i])
		for j in range(0,i,1):
#			print("j: ", j, lista[j])
			if lista[j] in ordenes[lista[i]]:
#				print ("pagina: ", lista[j], " está en ordenes lista i: ", ordenes[lista[i]])
				auxiliar = lista[i]
				lista[i] = lista[j]
				lista[j] = auxiliar
				modificada, lista = reorder(lista, ordenes)
				return True, lista;

	return False, lista






def valor_intermedio(vector):
	return vector[len(vector)//2]

# Ruta de entrada y salida
ruta_entrada = "/Users/david.conejero/Documents/AdventCode2024/input_day5.txt"

ordenes, updates = leer_archivo(ruta_entrada)

print(ordenes)
print(updates)

total = 0
for update in updates:
	if right_order(update, ordenes):
		total += valor_intermedio(update)


total2 = 0
modificada = False
for update in updates:
	modificada, new_update = reorder(update,ordenes)
	if modificada:
		print("original: ", update, " modificada: ", new_update)
		total2 += valor_intermedio(new_update)



print("Total1: ", total, " Total2: ", total2)