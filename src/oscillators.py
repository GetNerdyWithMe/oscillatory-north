"""
Shared oscillator utilities.

This file consolidates core dynamical system patterns used across
tree sway, swing dynamics, and neural oscillation models.
"""

import numpy as np

def canonical_oscillator(t, y, omega, zeta, forcing):
    x, x_dot = y
    x_ddot = forcing(t) - 2*zeta*omega*x_dot - omega**2 * x
    return [x_dot, x_ddot]
