import re
with open('i', 'r') as f:
	inp = f.read().split('\n')

instructions = [re.split(' <-> |, ', row) for row in inp]

relations = {}
for instruction in instructions:
	if instruction[0] not in relations.keys():
		relations[instruction[0]] = instruction[1:]
	else:
		for relation in instruction[1:]:
			if relation not in instruction:
				relations[instruction[0]].append(relation)
	for relation in instruction[1:]:
		if relation not in relations.keys():
			relations[relation] = instruction[:1]
		if instruction[0] not in relations[relation]:
			relations[relation].append(instruction[0])

def creep_creep(relations_dict, key, visited, count):
	if relations_dict[key]:
		visited.append(key)
		for relation in relations_dict[key]:
			if relation not in visited:
				count += 1
				creep_creep(relations_dict, relation, visited, count)


count = 0
visited = []
creep_creep(relations, '0', visited, count)
print(len(visited))

groups = []
for key in relations.keys():
	count = 0
	visited = []
	creep_creep(relations, key, visited, count)
	visited = sorted(visited)
	if visited not in groups:
		groups.append(visited)
print(len(groups))