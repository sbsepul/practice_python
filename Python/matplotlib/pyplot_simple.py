import numpy as np
import matplotlib.pyplot as plt

def f(t,q0,w0,p):
    return q0* np.cos(2*w0*t + p)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1,4,0.5,1), 'bo', t2, f(t2,1,9,1), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()