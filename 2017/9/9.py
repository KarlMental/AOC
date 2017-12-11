with open('i', 'r') as f:
    inp = f.read()

inc_point = 1
summa = 0
garbage = False
skip = False
garbage_count = 0

for char in inp:
	if not garbage:
		if char == '<':
			garbage = True
		elif char == '{':
			summa += inc_point
			inc_point += 1
		elif char == '}':
			inc_point -= 1
	else:
		if skip:
			skip = False
		elif char == '!':
			skip = True
		elif char == '>':
			garbage = False
		else:
			garbage_count += 1
	print(summa)
	print(garbage_count)