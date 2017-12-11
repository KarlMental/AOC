with open('i', 'r') as f:
    inp = f.read().split(',')

pos = [0, 0]

instruction_map = {
	'n': [-1, 1],
	'ne': [0, 1],
	'se': [1, 0],
	's': [1, -1],
	'sw': [0, -1],
	'nw': [-1, 0]

}

max_length = []

for instruction in inp:
	pos = [x + y for x, y in zip(pos, instruction_map[instruction])]
	if (pos[0] < 0 and pos[1] < 0) or (pos[0] > 0 and pos[1] > 0):
		max_length.append(abs(pos[0]+pos[1]))
	else:
		max_length.append(max(abs(pos[0]), abs(pos[1])))

print(max_length[-1])
print(max(max_length))