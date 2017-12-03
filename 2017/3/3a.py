
# coding: utf-8

# In[58]:


inp = 277678


# In[59]:


i = 9
cnt = 1
while i < inp:
    cnt += 1
    i = i + cnt * 8


# In[60]:


import math


# In[61]:


print(int(cnt+inp%(int(math.sqrt(i))/2)))


# In[62]:



def sum_adjacents(matris, x, y):
    return_sum = 0
    return_sum += matris[x-1][y]
    return_sum += matris[x+1][y]
    return_sum += matris[x-1][y-1]
    return_sum += matris[x-1][y+1]
    return_sum += matris[x+1][y-1]
    return_sum += matris[x+1][y+1]
    return_sum += matris[x][y-1]
    return_sum += matris[x][y+1]
    return return_sum
    


# In[65]:


north, south, west, east = (0, -1), (0, 1), (-1, 0), (1, 0)
new_dir = {north: west, west: south, south: east, east: north}
center = (int(math.sqrt(i)/2), int(math.sqrt(i)/2))
matris = [[0 for i in range(int(math.sqrt(i)))] for j in range(int(math.sqrt(i)))]
matris[center[0]][center[1]] = 1

pos_x, pos_y = center[0], center[1]
dir_x, dir_y = south

while True:
    if pos_x == center[0] and pos_y == center[1]:
        matris[pos_y][pos_x] = 1
    else:
        matris[pos_y][pos_x] = sum_adjacents(matris, pos_y, pos_x)
        if matris[pos_y][pos_x] > inp:
            print(matris[pos_y][pos_x])
            break
    new_dir_x, new_dir_y = new_dir[dir_x,dir_y]
    new_pos_x, new_pos_y = pos_x + new_dir_x, pos_y + new_dir_y
    if matris[new_pos_y][new_pos_x] == 0:
        pos_x, pos_y = new_pos_x, new_pos_y
        dir_x, dir_y = new_dir_x, new_dir_y
    else:
        pos_x, pos_y = pos_x + dir_x, pos_y + dir_y
    

