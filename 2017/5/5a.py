with open('5a.input', 'r') as f:
    data = f.read().split('\n')

data = [int(x) for x in data]
count = 0
index = 0
while True:
    count += 1
    index_temp = index
    try:
        index += data[index]
    except:
        print(count-1)
        break
    data[index_temp] += 1

with open('5a.input', 'r') as f:
    data = f.read().split('\n')

data = [int(x) for x in data]
count = 0
index = 0
while True:
    count += 1
    index_temp = index
    try:
        index += data[index]
    except:
        print(count-1)
        break
    if data[index_temp] >= 3:
        data[index_temp] -= 1
    else:
        data[index_temp] += 1