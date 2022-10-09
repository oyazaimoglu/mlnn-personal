#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Question 1


# In[5]:


import numpy as np
import matplotlib.pylab as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


n = 64
x = np.linspace(0, 1, n)
y = np.linspace(0, 1, n) + np.random.rand(n) - 1


# In[26]:


plt.scatter(x, y)


# In[27]:


# Question 2


# In[28]:


m_numer = np.sum(x) * np.sum(y)/n - np.sum(x * y) 


# In[29]:


m_denom = np.sum(x) * np.sum(x)/n - np.sum(x * x) 


# In[30]:


m_numer/m_denom #m = slope


# In[31]:


b = (np.sum(x * x) * np.sum(y) - np.sum(x) * np.sum(x * y))/(n * np.sum(x*x) - np.sum(x) * np.sum(x))
b


# In[32]:


# Question 3


# In[33]:


n = 64
x = np.linspace(0, 1, n) + np.random.rand(2, n)
x = np.vstack([x, np.ones(len(x.T))]).T
y = np.linspace(0, 1, n) + np.random.rand(n) - 1


# In[34]:


plt.scatter(x.T[0], y)


# In[35]:


plt.scatter(x.T[1], y)


# In[36]:


left = np.linalg.inv(np.dot(x.T, x))


# In[37]:


right = np.dot(y.T, x)


# In[38]:


np.dot(left, right)


# In[39]:


beta = np.linalg.lstsq(x, y)[0]
beta


# In[40]:


pred = np.dot(x, beta)


# In[41]:


plt.scatter(x.T[0], pred, c='red')
plt.scatter(x.T[0], y, c='b')


# In[42]:


plt.scatter(x.T[1], pred, c='red')
plt.scatter(x.T[1], y, c='b')


# In[43]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(23, 30)
ax.scatter(x.T[0], x.T[1], pred, zdir='z', c='r')
ax.scatter(x.T[0], x.T[1], y, zdir='z', c='b')


# In[ ]:


# Question 4


# In[46]:


import pandas as pd
import numpy as np
credit = pd.read_csv('/Users/oyazaimoglu/Desktop/Machine Learning/Credit.csv')
credit.head()


# In[48]:


columns = ["Income", "Limit", "Cards", "Age", "Balance"] # numeric only
x = credit[columns].values

x = np.vstack([x.T, np.ones(len(x))]).T
x


# In[49]:


y = credit['Rating'] #this is my dependent variable
y


# In[50]:


# Question 5


# In[51]:


plt.scatter(x.T[0], y)


# In[52]:


plt.scatter(x.T[1], y)


# In[ ]:




