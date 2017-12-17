from tqdm import tqdm
step_numb = 355
pos = 0
current_1_pos = 0

for i in tqdm(range(50000001)):
	pos = 1 + (pos + step_numb) % (i + 1)
	if pos == 1:
		current_1_pos = i+1

print(current_1_pos)