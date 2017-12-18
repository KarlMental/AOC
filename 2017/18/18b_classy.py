class Connector():

    def __init__(self, program1, program2):
        self.active_program = {'program': program1, 'name': 'program1'}
        self.waiting_program = {'program': program2, 'name': 'program2'}

        with open('i', 'r') as f:
            self.inp = f.read().split('\n')

    def run_main(self, return_program):
        while self.active_program['program'].step < len(self.inp):
            switch = self.active_program['program'].initiate_run(
                    self.inp[self.active_program['program'].step]
                    )
            if switch:
                self.active_program, self.waiting_program = self.waiting_program, self.active_program
                self.active_program['program'].in_queue = switch
                self.waiting_program['program'].out_queue = []
            if (self.active_program['program'].send_count + self.waiting_program['program'].send_count > 0
                    and not self.active_program['program'].in_queue
                    and not self.waiting_program['program'].in_queue
                    and not self.active_program['program'].out_queue
                    and not self.waiting_program['program'].out_queue):

                if self.active_program['name'] == return_program:
                    return self.active_program['program'].__dict__
                else:
                    return self.active_program['program'].__dict__

class Program():

    def __init__(self, name, variables={}):
        self.name = name
        self.variables = variables
        self.in_queue = []
        self.out_queue = []
        self.step = 0
        self.send_count = 0

    def initiate_run(self, instruction):
        instruction = instruction.split(' ')
        if instruction[0] in ['set', 'add', 'mul', 'mod']:
            switch = self.validate_modifiers(instruction[0], instruction[1], instruction[2])

        if instruction[0] == 'jgz':
            switch = self.validate_jgz(instruction[1], instruction[2])

        if instruction[0] in ['snd', 'rcv']:
            switch = self.validate_communicators(instruction[0], instruction[1])

        if not switch:
            self.step += 1

        return switch

    def validate_modifiers(self, cmd, var, val):
        if val in self.variables.keys():
            val = self.variables[val]
        elif try_int(val):
            val = int(val)
        else:
            return None

        if cmd == 'set':
            return self.set(var, val)
        if var in self.variables.keys():
            if cmd == 'add':
                return self.add(var, val)
            elif cmd == 'mul':
                return self.mul(var, val)
            elif cmd == 'mod':
                return self.mod(var, val)

    def validate_jgz(self, var, val):
        #Check if variable has value
        if var in self.variables.keys():
            var = self.variables[var]
        elif try_int(var):
            var = int(var)
        else:
            return
        #Check if jumpvalue has value
        if val in self.variables.keys():
            val = self.variables[val]
        elif try_int(val):
            val = int(val)
        else:
            return
        if var > 0:
            return self.jgz(var, val)

    def validate_communicators(self, cmd, var):
        var_val = None
        if var in self.variables.keys():
            var_val = self.variables[var]
        elif try_int(var):
            var_val = int(var)

        if cmd == 'rcv':
            return self.rcv(var)
        elif cmd == 'snd' and var_val is not None:
            return self.snd(var_val)

    def set(self, var, val):
        self.variables[var] = val

    def add(self, var, val):
        self.variables[var] += val

    def mul(self, var, val):
        self.variables[var] = self.variables[var] * val

    def mod(self, var, val):
        self.variables[var] = self.variables[var]  % val

    def jgz(self, var, val):
        self.step += val - 1

    def snd(self, var):
        self.out_queue.append(var)
        self.send_count += 1

    def rcv(self, var):
        if self.in_queue:
            self.variables[var] = self.in_queue.pop(0)
        else:
            return self.out_queue

def try_int(in_string):
    try:
        int(in_string)
        return True
    except:
        return False

def main():
    program1 = Program('program1', {'p': 0})
    program2 = Program('program2', {'p': 1})
    connector = Connector(program1, program2)
    print(connector.run_main('program2')['send_count'])


if __name__ == '__main__':
    main()