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

def creep_creep(relations_dict, key, visited):
	if relations_dict[key]:
		visited.append(key)
		for relation in relations_dict[key]:
			if relation not in visited:
				visited = creep_creep(relations_dict, relation, visited)
	return visited

visited = creep_creep(relations, '0', [])
print(len(visited))

groups = []
for key in relations.keys():
	if key not in [item for sublist in groups for item in sublist]:
		visited = sorted(creep_creep(relations, key, []))
		if visited not in groups:
			groups.append(visited)
print(len(groups))