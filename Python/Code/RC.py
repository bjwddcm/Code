import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 2*np.pi, 1000)

plt.plot(a, np.sin(a), label='sin(x)')
plt.plot(a, np.sin(a-2*np.pi/3), label='sin(x-2pi/3)')
plt.plot(a, np.sin(a+2*np.pi/3), label='sin(x+2pi/3)')

plt.legend()
plt.grid()
plt.show()
