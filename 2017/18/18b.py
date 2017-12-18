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

def start_program(program1, program2, inp, first_question=False):
    while program1['step'] < len(inp):
        instruction = parse(program1['variables'], inp[program1['step']])
        print(len(program1['queue']), len(program2['queue']))
        if instruction[0] == 'jgz':
            try:
                program1['step'] += jgz(program1['variables'], instruction[1], instruction[2]) - 1
            except KeyError:
                pass
        elif instruction[0] == 'set':
            try:
                program1['variables'] = set(program1['variables'], instruction[1], instruction[2])
            except this_variables:
                pass
        elif instruction[0] == 'mul':
            try:
                program1['variables'] = mul(program1['variables'], instruction[1], instruction[2])
            except KeyError:
                pass
        elif instruction[0] == 'add':
            try:
                program1['variables'] = add(program1['variables'], instruction[1], instruction[2])
            except KeyError:
                pass            
        elif instruction[0] == 'mod':
            try:
                program1['variables'] = mod(program1['variables'], instruction[1], instruction[2])
            except KeyError:
                pass            
        elif instruction[0] == 'snd':
            try: 
                program1['queue'].append(snd(program1['variables'], instruction[1]))
                if program1['name'] == 'B':
                    program1['counter'] += 1
            except KeyError:
                pass            
        elif instruction[0] == 'rcv':
            if first_question is True:
                return program1['queue']
            if not program2['queue']:
                if not program1['queue']:
                    return program1['queue']
                else:
                    program2, program1 = start_program(program2, program1, inp), program2
                    continue
            try:
                program1['variables'] = set(program1['variables'], instruction[1], program2['queue'].pop(0))
            except KeyError:
                pass
        program1['step'] += 1

with open('i', 'r') as f:
    inp = f.read().split('\n')

program_A = {'name': 'A', 'variables': {}, 'queue': [], 'step': 0, 'counter': 0}
program_B = {'name': 'B', 'variables': {}, 'queue': [], 'step': 0, 'counter': 0}

print(start_program(program_A, program_B, inp, True))
print(start_program(program_A, program_B, inp))