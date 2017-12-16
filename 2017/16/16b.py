import sys
from tqdm import tqdm

with open('i', 'r') as f:
    inp = f.read().split(',')

instructions = []
for i in inp:
	instruction = []
	if i[0] == 's':
		instruction = ['s', int(i[1:])]
	elif i[0] == 'p':
		instruction = [i[0]]
		for inst in sorted([ord(x)-97 for x in i[1:].split('/')]):
			instruction.append(inst)
	else:
		instruction = [i[0]]
		for inst in sorted([int(x) for x in i[1:].split('/')]):
			instruction.append(inst)
	instructions.append(instruction)

line = list(range(16))

for dance in range(10**9):
	if line == list(range(16)) and dance != 0:
		repetition_index = dance
		break
	for instruction in instructions:
		if instruction[0] == 's':
			line = line[-instruction[1]:] + line[:-instruction[1]]
		elif instruction[0] == 'x':
			line[instruction[1]], line[instruction[2]] = line[instruction[2]], line[instruction[1]]
		elif instruction[0] == 'p':
			i, j = line.index(instruction[1]), line.index(instruction[2])
			line[i], line[j] = line[j], line[i]

for dance in range(10**9%repetition_index):
	for instruction in instructions:
		if instruction[0] == 's':
			line = line[-instruction[1]:] + line[:-instruction[1]]
		elif instruction[0] == 'x':
			line[instruction[1]], line[instruction[2]] = line[instruction[2]], line[instruction[1]]
		elif instruction[0] == 'p':
			i, j = line.index(instruction[1]), line.index(instruction[2])
			line[i], line[j] = line[j], line[i]

print(''.join([chr(x+97) for x in line]))