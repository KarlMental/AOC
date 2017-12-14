import numpy as np

def reverse_circular_list(lista, start_index, length):
	if start_index + length - 1 >= len(lista):
		stop_index = start_index + length - len(lista)
		sublist = lista[start_index:]+lista[0:stop_index]
		sublist	= sublist[::-1]
		lista[0:stop_index] = sublist[-len(lista[0:stop_index]):]
		lista[start_index:] = sublist[:len(lista[start_index:])]
	else:
		sublist = lista[start_index:start_index+length]
		lista[start_index:start_index+length] = sublist[::-1]
	return lista


def knot_hash(inp):

	inp_list = [ord(x) for x in inp] + [17, 31, 73, 47, 23]

	lista = [i for i in range(256)]

	skip = 0
	curr_pos = 0

	for i in range(64):
		for instruction in inp_list:
			lista = reverse_circular_list(lista, curr_pos%256, instruction)
			curr_pos = curr_pos + instruction+ skip
			skip += 1

	lista_split = np.array_split(lista, 16)
	dense_hash = []
	for row in lista_split:
		temp_value = 0
		for i in range(16):
			temp_value = temp_value ^ row[i]
		dense_hash.append(temp_value)

	hex_string = ''
	for value in dense_hash:
		if len(hex(value)[2:]) == 1:
			hex_string += '0' + hex(value)[2:]
		else:
			hex_string += hex(value)[2:]

	return hex_string

def create_binary_repr(char):
	bin_number = bin(int(char, 16))[2:]
	pad = 4-len(bin_number)
	return ''.join(['0' for p in range(pad)]) + bin_number

inp = 'hfdlxzhv'
grid = []
for i in range(128):
	row_hash = knot_hash(inp + '-' + str(i))
	bin_string = ''
	for char in row_hash:
		bin_string += create_binary_repr(char)
	grid.append([int(x) for x in bin_string])
summa = 0
for row in grid:
	summa += sum(row)
print(summa)