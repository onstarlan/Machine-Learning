#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = 3*np.sin(4*np.pi-x)


# In[3]:


plt.plot(x,y,color = "Red")
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
           [r'$-2\pi$', r'$-\pi$',r'$0$',r'$+\pi$',r'$+2\pi$'])
plt.yticks([-3,-2,-1,0,+1,+2,+3],
           [r'$-3$',r'$-2$',r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3'])
plt.text(-2*np.pi,2.5,r'$y=3\sin \left( 4\pi -x\right)$',
        fontsize=10,bbox={'facecolor':'blue','alpha':0.2})
print("www.linkedin.com/onstarlan\nGraph of a Sinusoidal function")


# In[ ]:




