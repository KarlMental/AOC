with open('4a.input', 'r') as f:
    inp_split = f.read().split('\n')

data = []
for phrase in inp_split:
    data.append(phrase.split(' '))

phrase_count = 0
invalids = 0
for phrase in data:
    phrase_count += 1
    for i in range(len(phrase)):
        complement = phrase[:i]+phrase[i+1:]
        if phrase[i] in complement:
            invalids += 1
            break
print(phrase_count - invalids)

data = []
for phrase in inp_split:
    data.append(phrase.split(' '))
data_b = []
temp_phrase = []
for phrase in data:
    temp_phrase = []
    for word in phrase:
        temp_phrase.append(''.join(sorted(word)))
    data_b.append(temp_phrase)

phrase_count = 0
invalids = 0
for phrase in data_b:
    phrase_count += 1
    for i in range(len(phrase)):
        complement = phrase[:i]+phrase[i+1:]
        if phrase[i] in complement:
            invalids += 1
            break
print(phrase_count - invalids)
