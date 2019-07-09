# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import math

# Initialize arrays
t = np.zeros(200)
t1 = np.zeros(len(t))
t2 = np.zeros(len(t))
t3 = np.zeros(len(t))

# Test function for exponential growth
def A(A0, k, t):
    return A0 * math.exp(k*t)
 
# Test variables 
A0 = 45.0  # Initial value
k1 = -0.01 # Growth rate
k2 = -0.1  # Growth rate
gain = 0.7 # Fixed gain

# Calculate the functions
for i in range(len(t)):
    t[i] = i
    t1[i] = A(A0, k1, t[i])
    t2[i] = A(A0,k2, t[i])+np.random.rand()*5
    t3[i] = t1[i] + gain*(t2[i] - t1[i])

# Plot the functions
plt.close()
plt.plot(t,t1,'r-')
plt.plot(t,t2,'b-')
plt.plot(t,t3,'g-')
plt.show()

# Fixed gain algorythm
# Xnew = Xslow + K (Xfast - Xslow)

