with open('i', 'r') as f:
    inp = f.read().split(',')
inp_list = [int(x) for x in inp]


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

for instruction in inp_list:
	lista = reverse_circular_list(lista, curr_pos%256, instruction)
	curr_pos = curr_pos + instruction + skip
	skip += 1
print(lista[0]*lista[1])
