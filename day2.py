

# Función para leer el archivo CSV y extraer las conexiones origen-destino
def leer_reports(ruta_archivo):
    lista_reports = []
    with open(ruta_archivo, mode="r") as archivo:
        for fila in archivo:
        	report = list(map(int,fila.split()))        	
        	lista_reports.append(report)
    
    return lista_reports


def identify_safe_reports(report):
	increase = True

	auxiliar = report.copy()

	ref = auxiliar[0]
	auxiliar.pop(0)

	if ref > auxiliar[0]:
		increase = False

	for value in auxiliar:
		if (value == ref) or (increase and (value < ref or value > ref+3)) or (not increase and (value > ref or value < ref-3)):
				return False
		ref = value

	return True



# Generar todos los posibles vectores quitando un elemento de la lista
def generate_variations(report):

	lista_reports = []
	idx = 0
	while idx < len(report):
		copy = report.copy()
		copy.pop(idx)
		lista_reports.append(copy)
		idx += 1

	return lista_reports

# Ruta de entrada y salida
ruta_entrada = "/Users/david.conejero/Documents/AdventCode2024/input_day2"

lista_reports = leer_reports(ruta_entrada)

counter = 0
for report in lista_reports:
	if identify_safe_reports(report):
		counter += 1
	else:
		variaciones = generate_variations(report)
		for variacion in variaciones:
			if identify_safe_reports(variacion):
				counter += 1
				break


print (counter)
