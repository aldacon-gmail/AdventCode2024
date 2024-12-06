import re

string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# Función para leer el archivo CSV y extraer las conexiones origen-destino
def leer_reports(ruta_archivo):
    with open(ruta_archivo, mode="r") as archivo:
        fila = archivo

    return fila


# Ruta de entrada y salida
ruta_entrada = "/Users/david.conejero/Documents/AdventCode2024/input_day3"

file = open(ruta_entrada, 'r')

string = file.read()



# PROBLEM 1:
# multiples = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', string)
#total = 0
#for multipliers in multiples:
#	total += int(multipliers[0]) * int(multipliers[1])


# PROBLEM 2:
total = 0
stop_counting = False
for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)', string):
#	print(stop_counting, m.group(1), m.group(2))
	if not stop_counting and m.group(1):
		total += int(m.group(1)) * int(m.group(2))
	elif m.group(0) == "don't()":
		stop_counting = True
	elif m.group(0) == "do()":
		stop_counting = False












print(total)