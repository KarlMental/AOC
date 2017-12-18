def parse(variables, instruction):
    instruction = instruction.split(' ')
    try:
        instruction[2] = int(variables[instruction[2]])
    except:
        try:
            instruction[2] = int(instruction[2])
        except:
            try:
                instruction[1] = int(instruction[1])
            except:
                pass
    return instruction

def set(variables, var, val):
    variables[var] = val
    return variables

def add(variables, var, val):
    variables[var] = variables[var] + val
    return variables

def mul(variables, var, val):
    variables[var] = variables[var] * val
    return variables

def mod(variables, var, val):
    variables[var] = variables[var] % val
    return variables

def jgz(variables, var, val):
    if variables[var] > 0:
        return val
    else:
        return 1

def snd(variables, var):
    if var in variables.keys():
        return variables[var]
    else:
        return var

def start_program(this_program, other_program, this_variables, other_variables, this_queue, other_queue, this_iter, other_iter, inp, counter, first_question=False):
    while this_iter < len(inp):
        instruction = parse(this_variables, inp[this_iter])
        print(len(this_queue), len(other_queue))
        if instruction[0] == 'jgz':
            try:
                this_iter += jgz(this_variables, instruction[1], instruction[2]) - 1
            except KeyError:
                pass
        elif instruction[0] == 'set':
            try:
                this_variables = set(this_variables, instruction[1], instruction[2])
            except this_variables:
                pass
        elif instruction[0] == 'mul':
            try:
                this_variables = mul(this_variables, instruction[1], instruction[2])
            except KeyError:
                pass
        elif instruction[0] == 'add':
            try:
                this_variables = add(this_variables, instruction[1], instruction[2])
            except KeyError:
                pass            
        elif instruction[0] == 'mod':
            try:
                this_variables = mod(this_variables, instruction[1], instruction[2])
            except KeyError:
                pass            
        elif instruction[0] == 'snd':
            try: 
                this_queue.append(snd(this_variables, instruction[1]))
                if this_program == 'B':
                    counter += 1
            except KeyError:
                pass            
        elif instruction[0] == 'rcv':
            if first_question is True:
                return this_queue[-1]
            if not other_queue:
                if not this_queue:
                    return this_program, other_program, this_variables, other_variables, this_queue, other_queue, this_iter, other_iter, inp, counter
                else:
                    other_program, this_program, other_variables, this_variables, other_queue, this_queue, other_iter, this_iter, inp, counter = start_program(other_program, this_program, other_variables, this_variables, other_queue, this_queue, other_iter, this_iter, inp, counter)
                    continue
            try:
                this_variables = set(this_variables, instruction[1], other_queue.pop(0))
            except KeyError:
                pass
        this_iter += 1

with open('i', 'r') as f:
    inp = f.read().split('\n')

print(start_program('A', 'B', {}, {}, [], [], 0, 0, inp, 0, True))
print(start_program('A', 'B', {'p': 0}, {'p': 1}, [], [], 0, 0, inp, 0))