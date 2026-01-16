import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

g = 9.81
L = 2.0

def swing(t, y):
    theta, theta_dot = y
    human_input = 0.2 * np.sin(t)
    theta_ddot = - (g / L) * theta + human_input
    return [theta_dot, theta_ddot]

y0 = [0.1, 0.0]
t_span = (0, 50)
t_eval = np.linspace(*t_span, 1000)

solution = solve_ivp(
    swing,
    t_span,
    y0,
    t_eval=t_eval
)

plt.figure()
plt.plot(solution.t, solution.y[0])
plt.xlabel("Time")
plt.ylabel("Angle (rad)")
plt.title("Human-Driven Swing Dynamics")
plt.show()
