with open('8a.input', 'r') as f:
    inp = f.read().split('\n')

inp = [x.split(' ') for x in inp]

def init_value(register, registers):
	if register not in [item[0] for item in registers.items()]:
		registers[register] = 0
	return registers

def check_condition(condition, registers):
	if condition[2] == '==':
		return registers[condition[1]] == int(condition[3])
	elif condition[2] == '>':
		return registers[condition[1]] > int(condition[3])
	elif condition[2] == '<':
		return registers[condition[1]] < int(condition[3])
	elif condition[2] == '>=':
		return registers[condition[1]] >= int(condition[3])
	elif condition[2] == '<=':
		return registers[condition[1]] <= int(condition[3])
	elif condition[2] == '!=':
		return registers[condition[1]] != int(condition[3])
	else:
		print('Ello dick\'ed')

def perform_instruction(instruction, registers):
	if instruction[1] == 'inc':
		registers[instruction[0]] += int(instruction[2])
	elif instruction[1] == 'dec':
		registers[instruction[0]] -= int(instruction[2])
	return registers
registers = {}

max_values = []

for instruction in inp:
	registers = init_value(instruction[4], registers)
	if check_condition(instruction[3:], registers):
		registers = init_value(instruction[0], registers)
		registers = perform_instruction(instruction[:3], registers)
		max_values.append(max([value for value in registers.values()]))


print(max([value for value in registers.values()]))
print(max(max_values))