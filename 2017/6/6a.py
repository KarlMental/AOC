import copy
with open('6a.input', 'r') as f:
    inp = f.read().split('\t')

inp = [int(x) for x in inp]

seen_lists = []

count = 0
while True:
	seen_lists.append(copy.deepcopy(inp))
	if seen_lists.count(inp) > 1:
		break
	count += 1
	redistr = max(inp)
	i = inp.index(redistr)+1
	inp[i-1] = 0
	while redistr > 0:
		if i >= len(inp):
			i = 0
		inp[i] += 1
		redistr -= 1
		i += 1
print(count)
print(len(seen_lists)-seen_lists.index(inp)-1)