with open('4a.input', 'r') as f:
    inp_split = f.read().split('\n')

def find_valids(data):
    phrase_count = 0
    invalids = 0
    for phrase in data:
        phrase_count += 1
        for i in range(len(phrase)):
            complement = phrase[:i]+phrase[i+1:]
            if phrase[i] in complement:
                invalids += 1
                break
    return phrase_count - invalids

data = []
for phrase in inp_split:
    data.append(phrase.split(' '))

print(find_valids(data))

data_b = [[''.join(sorted(word)) for word in phrase] for phrase in data]

print(find_valids(data_b))
