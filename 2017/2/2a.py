with open('2a.input', 'r') as f:
    data = f.read().split('\n')

new_data = []
for elem in data:
    new_data.append(elem.split('\t'))
spreadsheet = [[int(word) for word in x] for x in new_data]

summa = 0
for row in spreadsheet:
    summa +=  max(row)-min(row)

#2a 
print(summa)
summa=0

from itertools import permutations

for row in spreadsheet:
    for perm in permutations(row, 2):
        if perm[0]%perm[1]==0:
            summa+=perm[0]/perm[1]
#2b
print(summa)