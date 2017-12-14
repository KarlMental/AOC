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

def create_grid_from_input(inp):
	grid = []
	for i in range(128):
		row_hash = knot_hash(inp + '-' + str(i))
		bin_string = ''
		for char in row_hash:
			bin_string += create_binary_repr(char)
		grid.append([int(x) for x in bin_string])
	return grid

def paint_adjacents(x, y, grid, val):
	for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
		if y + dy >= 0 and y + dy < 128 and x + dx >= 0 and x + dx < 128 and grid[y+dy][x+dx] == 1:
			grid[y+dy][x+dx] = val
			grid = paint_adjacents(x+dx, y+dy, grid, val)
	return grid


grid = create_grid_from_input('hfdlxzhv')

inc_group_value = 2
for i, row in enumerate(grid):
	for j, cell in enumerate(row):
		if cell == 1:
			grid[i][j] = inc_group_value
			grid = paint_adjacents(j, i, grid, inc_group_value)
			inc_group_value	+= 1
max_v = 0
for row in grid:
	if max(row) > max_v:
		max_v = max(row)
print(max_v-1)

