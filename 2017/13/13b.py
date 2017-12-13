with open('i', 'r') as f:
    inp = f.read().split('\n')
instructions = {}
for n in inp:
	instructions[int(n.split(': ')[0])] = int(n.split(': ')[1])


layers = []
for i in range(int(inp[-1].split(': ')[0])+1):
	try:
		temp_value = instructions[i]
	except:
		temp_value = 0
	layers.append(temp_value)
print(layers)

def give_hit_at_iteration(layer_value, iteration):
	if iteration % (layer_value*2-2) == 0:
		return True
	else:
		return False

delay = 0

while True:
	cont = False
	for i, layer_value in enumerate(layers):
		if give_hit_at_iteration(layer_value, i+delay):
			cont = True
			break
	if not cont:
		break
	delay += 1
	if delay%100000 == 0:
		print(delay, cont)
	
print(delay)