with open('i', 'r') as f:
    inp = f.read().split(',')

line = 'abcdefghijklmnop'
def run_instruction(instruction, line):
	line = [char for char in line]
	if instruction[0] == 's':
		line = spin(instruction[1:], line)
	if instruction[0] == 'x':
		line = exchange(instruction[1:], line)
	if instruction[0] == 'p':
		line = partner(instruction[1:], line)
	return ''.join(line)

def spin(instruction, line):
	line = [char for char in line]
	return line[-int(instruction):] + line[:-int(instruction)]

def exchange(instruction, line):
	line = [char for char in line]
	instruction = [int(x) for x in instruction.split('/')]
	line[instruction[0]], line[instruction[1]] = line[instruction[1]], line[instruction[0]]
	return ''.join(line)

def partner(instruction, line):
	line = [char for char in line]
	instruction = instruction.split('/')
	index_inst = str(line.index(instruction[0])) + '/' + str(line.index(instruction[1]))
	line = exchange(index_inst, line)
	return ''.join(line)
original_line = line

for dance in range(10**9):
	if dance != 0 and line == original_line:
		repetition_index = dance
		break
	for instruction in inp:
		line = run_instruction(instruction, line)

for dance in range(10**9%repetition_index):
	for instruction in inp:
		line = run_instruction(instruction, line)
print(line)