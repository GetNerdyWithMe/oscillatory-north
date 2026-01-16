import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# This system exhibits stable oscillations when damping balances forcing.
# Changing zeta alters convergence behavior and stability.

# Canonical second-order oscillator:
# x'' + 2*zeta*omega*x' + omega^2*x = F(t)

def oscillator(t, y, omega, zeta):
    x, x_dot = y
    F = np.sin(t)  # simple periodic forcing
    x_ddot = F - 2*zeta*omega*x_dot - omega**2 * x
    return [x_dot, x_ddot]

# Parameters
omega = 1.0      # natural frequency
zeta = 0.1       # damping ratio

# Initial conditions
y0 = [0.0, 0.0]

# Time span
t_span = (0, 50)
t_eval = np.linspace(*t_span, 1000)

# Solve ODE
solution = solve_ivp(
    oscillator,
    t_span,
    y0,
    args=(omega, zeta),
    t_eval=t_eval
)

# Plot
plt.figure()
plt.plot(solution.t, solution.y[0])
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.title("Canonical Driven Oscillator")
plt.show()
plt.figure()
plt.plot(solution.y[0], solution.y[1])
plt.xlabel("x")
plt.ylabel("x_dot")
plt.title("Phase Space Trajectory")
plt.show()
