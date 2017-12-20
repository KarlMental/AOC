import re
import itertools

with open('i', 'r') as f:
    inp = f.read().strip().split('\n')
data = [re.findall(r'<(.*?)>',row) for row in inp]

particles = []

for row in data:
    new_row = []
    for prop in row:
        new_row.append([int(x) for x in prop.split(',')])
    particles.append(new_row)

def create_iter_particle(particle):

    def func(i):
        x = particle[0][0] + particle[1][0]*i + particle[2][0]*i*(i+1)/2
        y = particle[0][1] + particle[1][1]*i + particle[2][1]*i*(i+1)/2
        z = particle[0][2] + particle[1][2]*i + particle[2][2]*i*(i+1)/2
        return [int(x), int(y), int(z)]
    return func

function_list = []

for particle in particles:
    function_list.append(create_iter_particle(particle))

for i in itertools.count():
    print(len(function_list))
    values = []
    not_index = []
    for particle in function_list:
        values.append(particle(i))
    for j, value in enumerate(values):
        if values.count(value) > 1:
            not_index.append(j)
    new_func = []
    for j, particle in enumerate(function_list):
        if j not in not_index:
            new_func.append(particle)
    function_list = new_func
    

