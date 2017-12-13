with open('i', 'r') as f:
    inp = f.read().split('\n')
instructions = {}
for n in inp:
	instructions[int(n.split(': ')[0])] = int(n.split(': ')[1])


layers = {}
for i in range(int(inp[-1].split(': ')[0])+1):
	try:
		temp_value = instructions[i]
	except:
		temp_value = 0
	layers[i] = {}
	layers[i]['depth'] = temp_value
	layers[i]['pos'] = -1
	layers[i]['dir'] = 1

def update_layers(layers):
	for key in layers.keys():
		if layers[key]['depth'] == 0:
			continue
		elif layers[key]['dir'] > 0:
			layers[key]['pos'] += 1
		elif layers[key]['dir'] < 0:
			layers[key]['pos'] -= 1
		if (layers[key]['pos'] == 0 and layers[key]['dir'] < 0) or layers[key]['pos'] + 1 == layers[key]['depth']:
			layers[key]['dir'] = layers[key]['dir']*(-1)
delay = 0
while True:
	score = 0
	for i in range(delay):
		update_layers(layers)
	for i in range(max(layers.keys())+1):
		update_layers(layers)
		if layers[i]['pos'] == 0:
			score += i*layers[i]['depth']
	if score == 0:
		break