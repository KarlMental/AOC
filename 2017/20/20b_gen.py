import re
import itertools

def create_iter_particle(particle):
    def func(i):
        x = particle[0][0] + particle[1][0]*i + particle[2][0]*i*(i+1)/2
        y = particle[0][1] + particle[1][1]*i + particle[2][1]*i*(i+1)/2
        z = particle[0][2] + particle[1][2]*i + particle[2][2]*i*(i+1)/2
        return [int(x), int(y), int(z)]
    return func

def functify_particle_list(particles):
    particle_functions = [create_iter_particle(particle) for particle in particles]
    return particle_functions

def remove_collisions(particles, iteration):
    values = [particle(iteration) for particle in particles]
    new_func = [particles[j] for j, value in enumerate(values) if values.count(value) < 2]
    return new_func

def get_input_data():
    with open('i', 'r') as f:
        inp = f.read().strip().split('\n')
    return [re.findall(r'<(.*?)>',row) for row in inp]

def main():
    particles = [[[int(x) for x in prop.split(',')] for prop in row] for row in get_input_data()]
    particles = functify_particle_list(particles)

    consecutives = 0
    for i in itertools.count():
        length = len(particles)
        particles = remove_collisions(particles, i)
        if len(particles) == length:
            consecutives += 1
            if consecutives > 20:
                break
        else:
            consecutives = 0
        
    print(len(particles))

if __name__ == '__main__':
    main()
