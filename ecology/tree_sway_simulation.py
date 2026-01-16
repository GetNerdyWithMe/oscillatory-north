# NOTE:
# This file is a domain-specific application of the canonical oscillator
# defined in src/oscillators.py

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def tree_sway(t, y, omega, zeta):
    x, x_dot = y
    wind = 0.5 * np.sin(0.8 * t)
    x_ddot = wind - 2*zeta*omega*x_dot - omega**2 * x
    return [x_dot, x_ddot]

omega = 0.8   # effective sway frequency
zeta = 0.2    # higher damping than swing

y0 = [0.0, 0.0]
t_span = (0, 100)
t_eval = np.linspace(*t_span, 2000)

solution = solve_ivp(
    tree_sway,
    t_span,
    y0,
    args=(omega, zeta),
    t_eval=t_eval
)

plt.figure()
plt.plot(solution.t, solution.y[0])
plt.xlabel("Time")
plt.ylabel("Lateral Displacement")
plt.title("Tree Sway Under Oscillatory Wind")
plt.show()
