import copy
with open('7a.input', 'r') as f:
    inp = f.read().split('\n')

inp = [x.split(' ') for x in inp]
inp = [[w.replace(',','') for w in x] for x in inp]

programs = {}

reference_list = []
i = 0
while i < len(inp):
	try:
		ind = inp[i].index('->')
		for ref in range(ind+1, len(inp[i])):
			reference_list.append(inp[i][ref])
	except:
		i += 1
		continue
	i += 1

i = 0
while True:
	if inp[i][0] not in reference_list:
		print(inp[i][0])
		break
	i += 1

for line in inp:
	programs[line[0]] = {}
	if len(line) > 2:
		programs[line[0]]['references'] = line[3:]
	programs[line[0]]['number'] = int(line[1][1:-1])

for line in inp:
	programs[line[0]]['reference_sum'] = 0
	try:
		for ref in programs[line[0]]['references']:
			programs[line[0]]['reference_sum'] += programs[ref]['number']
	except:
		pass
reference_sums = [programs[line[0]]['reference_sum'] + programs[line[0]]['number'] for line in inp]
print(reference_sums)
#print(reference_sums.sort())