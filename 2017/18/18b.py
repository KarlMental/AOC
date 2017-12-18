def parse(variables, instruction):
    instruction = instruction.split(' ')
    try:
        instruction[2] = int(variables[instruction[2]])
    except:
        try:
            instruction[2] = int(instruction[2])
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

def rcv(sound):
    print(sound)

def jgz(variables, var, val):
    if variables[var] > 0:
        return val
    else:
        return 1

def snd(variables, var):
    return variables[var]

with open('i', 'r') as f:
    inp = f.read().split('\n')



variables = {}
sound = 0
i = 0
while i < len(inp):
    instruction = parse(variables, inp[i])
    if instruction[0] == 'jgz':
        try:
            i += jgz(variables, instruction[1], instruction[2]) - 1
        except KeyError:
            pass
    elif instruction[0] == 'set':
        try:
            variables = set(variables, instruction[1], instruction[2])
        except KeyError:
            pass
    elif instruction[0] == 'mul':
        try:
            variables = mul(variables, instruction[1], instruction[2])
        except KeyError:
            pass
    elif instruction[0] == 'add':
        try:
            variables = add(variables, instruction[1], instruction[2])
        except KeyError:
            pass            
    elif instruction[0] == 'mod':
        try:
            variables = mod(variables, instruction[1], instruction[2])
        except KeyError:
            pass            
    elif instruction[0] == 'snd':
        try: 
            sound = snd(variables, instruction[1])
        except KeyError:
            pass            
    elif instruction[0] == 'rcv':
        rcv(sound)
        break
    i += 1


