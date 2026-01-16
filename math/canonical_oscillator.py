# exploratory parameters
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

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

for zeta in [0.05, 0.2, 0.6]:
    solution = solve_ivp(
        oscillator,
        t_span,
        y0,
        args=(omega, zeta),
        t_eval=t_eval
    )
    plt.plot(solution.t, solution.y[0], label=f"zeta = {zeta}")

plt.xlabel("Time")
plt.ylabel("Displacement")
plt.title("Effect of Damping on Oscillatory Stability")
plt.legend()
plt.show()

# phase space

plt.figure()

for zeta in [0.05, 0.2]:
    solution = solve_ivp(
        oscillator,
        t_span,
        y0,
        args=(omega, zeta),
        t_eval=t_eval
    )
    plt.plot(
        solution.y[0],      # x
        solution.y[1],      # x_dot
        label=f"zeta = {zeta}"
    )

plt.xlabel("x")
plt.ylabel("x_dot")
plt.title("Phase Space Trajectories and Mode Collapse")
plt.legend()
plt.axis("equal")
plt.savefig("results/phase_space_modes.png", dpi=150)
plt.show()
