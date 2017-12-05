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
    data = [data[x]-1 if x == index_temp and data[x] >= 3 else data[x]+1 if x == index_temp and data[x] < 3 else data[x] for x in range(len(data))]
