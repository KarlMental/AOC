buff = [0]
step_numb = 355
pos = 0


for i in range(2018):
	pos = 1 + (pos + step_numb) % len(buff)
	buff.insert(pos, i+1)

print(buff[buff.index(2017)+1])