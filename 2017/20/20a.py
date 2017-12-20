import re

with open('i', 'r') as f:
    inp = f.read().strip().split('\n')
data = [re.findall(r'<(.*?)>',row) for row in inp]

new_data = []

for row in data:
    new_row = []
    for prop in row:
        new_row.append([int(x) for x in prop.split(',')])
    new_data.append(new_row)

lowest_value = 10000000000
for i, row in enumerate(new_data):
    if max([abs(x) for x in row[2]]) < lowest_value:
        lowest_value = max([abs(x) for x in row[2]])
        lowest_value_i = i

print(lowest_value_i)
