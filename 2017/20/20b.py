import re
from operator import add

def remove_collisions(particles):
    new_particles = []
    for particle in particles:
        if [part[0] for part in particles].count(particle[0]) < 2:
            new_particles.append(particle)
    return new_particles

def update_positions_mut(particles):
    for i, particle in enumerate(particles):
        v = list(map(add, particle[1], particle[2]))
        p = list(map(add, particle[0], v))
        particles[i] = [p, v, particle[2]]
    return particles

with open('i', 'r') as f:
    inp = f.read().strip().split('\n')
data = [re.findall(r'<(.*?)>',row) for row in inp]

particles = []

for row in data:
    new_row = []
    for prop in row:
        new_row.append([int(x) for x in prop.split(',')])
    particles.append(new_row)

while True:
    particles = remove_collisions(particles)
    particles = update_positions_mut(particles)
    print(len(particles))