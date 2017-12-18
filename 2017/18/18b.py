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

def rcv(variables, var, val):
    variables[var] = val
    return variables

def jgz(variables, var, val):
    if variables[var] > 0:
        return val
    else:
        return 1

def snd(variables, var):
    return variables[var]

with open('i', 'r') as f:
    inp = f.read().split('\n')


variables_A = {'p': 0}
variables_B = {'p': 1}

A_queue = []
B_queue = []
i = 0

while i < len(inp):
    instruction = parse(variables_A, inp[i])
    if instruction[0] == 'jgz':
        try:
            i += jgz(variables_A, instruction[1], instruction[2]) - 1
        except KeyError:
            pass
    elif instruction[0] == 'set':
        try:
            variables_A = set(variables_A, instruction[1], instruction[2])
        except KeyError:
            pass
    elif instruction[0] == 'mul':
        try:
            variables_A = mul(variables_A, instruction[1], instruction[2])
        except KeyError:
            pass
    elif instruction[0] == 'add':
        try:
            variables_A = add(variables_A, instruction[1], instruction[2])
        except KeyError:
            pass            
    elif instruction[0] == 'mod':
        try:
            variables_A = mod(variables_A, instruction[1], instruction[2])
        except KeyError:
            pass            
    elif instruction[0] == 'snd':
        try: 
            A_queue.append(snd(variables_A, instruction[1]))
        except KeyError:
            pass            
    elif instruction[0] == 'rcv':
        break
    i += 1
print(A_queue)
i = 0
while i < len(inp):
    instruction = parse(variables_B, inp[i])
    if instruction[0] == 'jgz':
        try:
            i += jgz(variables_B, instruction[1], instruction[2]) - 1
        except KeyError:
            pass
    elif instruction[0] == 'set':
        try:
            variables_B = set(variables_B, instruction[1], instruction[2])
        except KeyError:
            pass
    elif instruction[0] == 'mul':
        try:
            variables_B = mul(variables_B, instruction[1], instruction[2])
        except KeyError:
            pass
    elif instruction[0] == 'add':
        try:
            variables_B = add(variables_B, instruction[1], instruction[2])
        except KeyError:
            pass            
    elif instruction[0] == 'mod':
        try:
            variables_B = mod(variables_B, instruction[1], instruction[2])
        except KeyError:
            pass            
    elif instruction[0] == 'snd':
        try: 
            B_queue.append(snd(variables_B, instruction[1]))
        except KeyError:
            pass            
    elif instruction[0] == 'rcv':
        try:
            variables_B = rcv(variables_B, instruction[1], A_queue.pop(0))
        except KeyError:
            pass
        except IndexError:
            print(len(B_queue)) 
            break        
    i += 1
