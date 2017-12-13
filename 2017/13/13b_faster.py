with open('i', 'r') as f:
    inp = f.read().strip().split('\n')
layers = [(int(i.split(': ')[0]), int(i.split(': ')[1])) for i in inp]

delay = 0
brk = False
while True:
	for layer in layers:
		if (layer[0]+delay) % (layer[1]*2-2) == 0:
			break
	else:
		brk = True 
	if brk:
		break
	delay += 1
	
print(delay)
