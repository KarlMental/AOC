import numpy as np
with open('i', 'r') as f:
    inp = f.read()
inp_list = [ord(x) for x in inp] + [17, 31, 73, 47, 23]


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

print(hex_string)