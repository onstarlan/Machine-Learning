import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 1000)
y = (x**3) + 4*x +6

plt.text(-2,100,'$y=x^3+4*x+6$',fontsize = 15,
         bbox = {'facecolor':'red','alpha':0.2})
plt.grid()
plt.plot(x,y)