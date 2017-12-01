# coding: utf-8

# In[42]:


with open('1a.input', 'r') as f:
    data = f.read().split('\n')


# In[43]:


new_data = [int(d) for d in data[0]]


# In[50]:


sumz=0
for i in range(0, len(new_data)):
    if i &lt; len(new_data)-1 and new_data[i] == new_data[i+1]:
        sumz+=new_data[i]
    elif i == len(new_data)-1 and new_data[i] == new_data[0]:
        sumz+=new_data[i]
print(sumz)


# In[44]:


length = int(len(new_data)/2)
a = new_data[length:]
b = new_data[:length]


# In[45]:


sumz=0
for i in range(0, len(a)-1):
    if a[i]==b[i]:
        sumz+=a[i]+b[i]
print(sumz)