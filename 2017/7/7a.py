from collections import Counter

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
	programs[line[0]]['references'] = []
	if len(line) > 2:
		for ref in line[3:]:
			programs[line[0]]['references'].append([ref, None])
	programs[line[0]]['number'] = int(line[1][1:-1])

for line in inp:
	for i in programs[line[0]]['references']:
		i[1] = programs[i[0]]['number']

def set_level(item, level, programs):
	programs[item]['level'] = level
	try:
		for ref in programs[item]['references']:
			set_level(ref[0], level+1, programs)
	except:
		pass

ref_numbers = [[item[1] for item in programs[line[0]]['references'][:]] for line in inp if programs[line[0]]['references']]

reference_sums = sorted([sum(item) for item in ref_numbers])

for item in programs.items():
	if item[1]['references']:
		if sum(x[1] for x in item[1]['references']) == reference_sums[-1]:
			set_level(item[0], 0, programs)

max_level = max([value['level'] for value in programs.values()])

for i in range(max_level, -1, -1):
	for item in programs.items():
		if i == max_level:
			programs[item[0]]['refsum'] = programs[item[0]]['number']
		elif item[1]['level'] == i:
			programs[item[0]]['refsum'] = sum([programs[ref[0]]['refsum'] for ref in programs[item[0]]['references']]) + programs[item[0]]['number']

for line in inp:
	for i in programs[line[0]]['references']:
		i[1] = programs[i[0]]['refsum']

for i in range(max_level-1, -1, -1):
	for item in programs.items():
		if item[1]['level'] == i and item[1]['references']:
			if item[1]['references'][0][1] != sum(x[1] for x in item[1]['references'])/sum([1 for x in item[1]['references']]):
				print(item[1]['references'])


#FUUUCK IIIIT
print(programs['cwwwj'])