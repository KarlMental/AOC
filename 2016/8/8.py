from collections import deque
import numpy as np

def draw_rect(screen, x, y):
	for i in range(x):
		for j in range(y):
			screen[i][j] = 1
	return screen

def rotate_column(screen, column, offset):
	temp_col = deque(screen[column])
	temp_col.rotate(offset)
	screen[column] = list(temp_col)
	return screen

def rotate_row(screen, row, offset):
	screen = np.asarray(screen)
	screen = list(np.transpose(screen))
	rotate_column(screen, row, offset)
	screen = np.asarray(screen)
	return list(np.transpose(screen))

with open('i', 'r') as f:
    inp = f.read().split('\n')

data = [x.split(' ') for x in inp]

dim_x = 50
dim_y = 6

screen = [[0 for i in range(dim_y)] for p in range(dim_x)]

for instruction in data:
	if instruction[0] == 'rect':
		x_y = [int(i) for i in instruction[1].split('x')]
		screen = draw_rect(screen, x_y[0], x_y[1])
	elif instruction[0] == 'rotate':
		index = int(instruction[2].split('=')[1])
		offset = int(instruction[4])
		if instruction[1] == 'row':
			screen = rotate_row(screen, index, offset)
		elif instruction[1] == 'column':
			screen = rotate_column(screen, index, offset)

print(sum([sum(row) for row in screen]))

for row in np.transpose(screen):
	string = ''
	for light in row:
		if light == 1:
			string += 'X'
		else:
			string += ' '
	print(string)