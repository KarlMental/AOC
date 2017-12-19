def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ' ':
                return i, j

def new_direction(grid, directions, old_direction, y, x):
    for direction in directions:
        if direction[1:] != (old_direction[1]*-1, old_direction[2]*-1):
            if grid[y+direction[1]][x+direction[2]] != ' ':
                return direction

def travel(direction, y, x):
    return y + direction[1], x+direction[2]

def check_new_pos(grid, y, x):
    if grid[y][x] not in [' ', '-', '|', '+']:
        return (grid[y][x], False)
    elif grid[y][x] == '+':
        return (None, True)
    else:
        return (None, None)

with open('i', 'r') as f:
    inp = f.read().split('\n')
grid = [[char for char in row] for row in inp]

char_list = []
directions = [('s', 1, 0), ('n', -1, 0), ('w', 0, -1), ('e', 0, 1)]
y_pos, x_pos = find_start(grid)
direction = new_direction(grid, directions, ('e', 0, 1), y_pos, x_pos)

i = 0
while True:
    y_pos, x_pos = travel(direction, y_pos, x_pos)
    new_pos = check_new_pos(grid, y_pos, x_pos)
    i += 1
    if new_pos[0]:
        char_list.append(new_pos[0])
    elif new_pos[1]:
        direction = new_direction(grid, directions, direction, y_pos, x_pos)
    if grid[y_pos][x_pos] == ' ':
        print(''.join(char_list), i)
        break
    