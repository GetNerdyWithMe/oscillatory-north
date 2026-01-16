import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
t = np.arange(0, 50, dt)

theta1 = np.zeros_like(t)
theta2 = np.zeros_like(t)

omega1 = 1.0
omega2 = 1.2
K = 0.5

for i in range(1, len(t)):
    theta1[i] = theta1[i-1] + dt * (omega1 + K * np.sin(theta2[i-1] - theta1[i-1]))
    theta2[i] = theta2[i-1] + dt * (omega2 + K * np.sin(theta1[i-1] - theta2[i-1]))

plt.figure()
plt.plot(t, theta1 - theta2)
plt.xlabel("Time")
plt.ylabel("Phase Difference")
plt.title("Phase Locking Between Oscillators")
plt.show()
