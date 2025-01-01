
ruta_entrada = "/Users/davidconejero/Documents/github/AdventCode2024/input_day9.txt"

fichero = open(ruta_entrada, mode="r")
disk_map = fichero.read()
#disk_map = '2333133121414131402'


class Bloque:

	def __init__(self, id=0, orden=0, length=0, posicion_inicial=0, posicion_final=0, espacios=0):
		self.id = id
		self.orden = orden
		self.length = length
		self.posicion_inicial = posicion_inicial
		self.posicion_final = posicion_final
		self.espacios = espacios

	def __str__(self):
		return f'Id: {self.id} Orden: {self.orden} Length: {self.length} Posicion_Inicial: {self.posicion_inicial} Posicion_Final: {self.posicion_final} Espacio: {self.espacios}' 

	def __repr__(self):
		return repr((self.orden, self.posicion_inicial))

	def __copy__(self):
		return Bloque(self.id, self.orden, self.length, self.posicion_inicial, self.posicion_final, self.espacios)



def mapear(map):

	lista_bloques = []
	lista_espacios = []
	cont = 0
	posicion_inicial = 0
	posicion_final = -1

	mapa = map.strip()
	print(len(mapa))

	for i in range(0,len(mapa),2):

		number = int(map[i])
		if i+1 >= len(mapa): 
			espacios = 0
		else:
			espacios = int(map[i+1])
		posicion_final = posicion_inicial + number - 1
		lista_bloques.append(Bloque(int(i/2),int(i/2),int(number),posicion_inicial,posicion_final,espacios))
		
		posicion_inicial =  posicion_final + 1 + espacios


	return lista_bloques, lista_espacios



def descypher_map(map):

	file = []
	lista_bloques = []
	cont = 0
	num_file = 0


	for number in map.strip():
		
		num = 1
		posicion_inicial = len(file) - 1

		while num <= int(number):
			if (cont % 2 == 0):
				file.append(num_file)
			else:
				file.append('.')
			num += 1


		
		cont += 1
#		print (number, num, cont, num_file, file)
		
		if (cont % 2 == 0): 
#			lista_bloques.append(Bloque(num_file,int(number),posicion_inicial,len(file)-1))
			num_file += 1


	print(num_file)

	return file

def compress_disk(file):

	posicion_inicial = 0
	posicion_final = -1
	longitud = len(file)

	loop = True
	loop_2 = True

	while loop:

		if file[posicion_inicial] == '.':

			loop_2 = True
			while loop_2 and loop:

				if file[posicion_final] != ".":
					file[posicion_inicial] = file[posicion_final]
					file[posicion_final] = '.'
					loop_2 = False
				
				posicion_final -= 1
				if (posicion_inicial - posicion_final) >= (longitud - 1):
					loop_2 = False
					

#		print(longitud, posicion_inicial, posicion_final, file[posicion_inicial], file[posicion_final+1], "".join(str(file)))
		posicion_inicial += 1
		if (posicion_inicial - posicion_final) >= (longitud):
					loop = False



	return file


def defrag_disk(file_2, disk_map):

	file = file_2.copy()

	disk = list(disk_map)

	longitud = len(disk)

	posicion_inicial = 1

	if (longitud % 2 == 0):
		posicion_final = longitud
		ids = longitud / 2
	else:
		posicion_final = longitud - 1
		ids = (longitud - 1) /2 

	pi_file = int(disk[0])
	pf_file = len(file) - int(disk[posicion_final])


	while (posicion_inicial <= posicion_final):

		print('comp', posicion_inicial, posicion_final, disk[posicion_inicial], disk[posicion_final])
		if disk[posicion_final] <= disk[posicion_inicial]:

			#mover bloques

#			print ('tt', disk_map, posicion_inicial, posicion_final, pi_file, pf_file, disk[posicion_inicial], disk[posicion_final])
			mover = 0
			while mover < int(disk[posicion_final]):
				file[pi_file+mover] =  file[pf_file+mover]
				file[pf_file+mover] =  '.'
				mover += 1

			pi_file += int(disk[posicion_inicial+1])
			pf_file -= int(disk[posicion_final-1])


			# block mogut


			posicion_inicial += 2
			pi_file += int(disk[posicion_inicial])

			posicion_final -= 2
			pf_file -= int(disk[posicion_final])

			ids -= 1


		else:
			posicion_final -= 2
			pf_file -= int(disk[posicion_final+1])
			pf_file -= int(disk[posicion_final])
			ids -= 1

		print(longitud, posicion_inicial, posicion_final, disk[posicion_inicial], disk[posicion_final],file)






	return file




def checksum(disk):

	csum = 0
	cont = 0
	longitud = len(disk)

	while cont < longitud:
		if disk[cont] != '.':
			csum += cont * int(disk[cont])
		cont += 1



	return csum



def compresor(bloques, espacios):

	posicion = len(bloques)-2
	for index, bloque in enumerate(reversed(bloques)):

		posicion -= index

		espacios = sorted(bloques, key=lambda espacio: espacio.posicion_inicial)
		for index_r in range(len(espacios)):
#			print(index_r, espacios[index_r].orden)
			espacios[index_r].orden = index_r

#		print(bloque)
		for index_e, espacio in enumerate(espacios):

#			print("espacio", espacio)

			if bloque.posicion_inicial > espacio.posicion_inicial:
				if bloque.length <= espacio.espacios:
#					print("entro ", index, index_e, posicion)
#					print("bloque", index, bloque)
#					print("espacio", index_e, espacio)

					for e in espacios:
						if e.orden == bloque.orden -1:
#							print('bloque_anterior', e)
							e.espacios += bloque.length + bloque.espacios


#				new_bloque = Bloque()
#				bloque.id = bloque.id
#				bloque.orden = espacio.orden + 1
#				new_bloque.length = bloque.length
					bloque.posicion_inicial = espacio.posicion_final + 1
					bloque.posicion_final = espacio.posicion_final + bloque.length
					bloque.espacios = espacio.espacios - bloque.length

					espacio.espacios = 0

#				if (index_e -1 >= 0) and (espacios[index_e-1].espacios == 0):
#					espacios[index_e-1] = espacio.length


#					print("new ", bloque)

#				bloques.insert(espacio.orden+1,new_bloque)
#				bloques.remove(bloque)

					break


	return bloques, espacios



def checksum2(blocks):

#	posicio = 0
	total = 0
	for block in blocks:

		repes = 0
		posicio = block.posicion_inicial
		while repes < block.length:

			total += block.id * posicio
			repes += 1
			posicio += 1

	return total



disk_status = descypher_map(disk_map)
bloques, espacios = mapear(disk_map)

#for b in bloques:
#	print(b)

#print("Espacios")
#for e in espacios:
#	print(e)

#print("FIN")


compressed_blocks, reduced_spaces = compresor(bloques, espacios)

t = checksum2(compressed_blocks)

print(t)

#print("Fimna")
#for cb in compressed_blocks:
#	print(cb)
#for rs in reduced_spaces:
#	print(rs)

disk_compressed = compress_disk(disk_status)

checksum = checksum(disk_compressed)

#print(disk_status)
##print(disk_compressed)
print(checksum)


#checksum = checksum(t)
