with open('i', 'r') as f:
    inp = f.read().split('\n')

data = [x.split(' ') for x in inp]
print(data)