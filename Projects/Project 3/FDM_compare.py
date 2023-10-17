import numpy as np


# Forward Euler method
def forward_euler(f, t, y0 = 0):
    n = len(t)
    y = np.zeros(n)
    y[0] = y0
    for i in range(n - 1):
        y[i + 1] = y[i] + (t[i + 1] - t[i]) * f(y[i], t[i])
    return y

# Runge-Kutta 4 method
def runge_kutta_4(f, t, y0 = 0):
    n = len(t)
    y = np.zeros(n)
    y[0] = y0
    for i in range(n - 1):
        h = t[i + 1] - t[i]
        k1 = f(y[i], t[i])
        k2 = f(y[i] + k1 * h / 2, t[i] + h / 2)
        k3 = f(y[i] + k2 * h / 2, t[i] + h / 2)
        k4 = f(y[i] + k3 * h, t[i] + h)
        y[i + 1] = y[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return y

# Runge-Kutta 2 method
def runge_kutta_2(f, t, y0 = 0):
    n = len(t)
    y = np.zeros(n)
    y[0] = y0 
    for i in range(n - 1):
        h = t[i + 1] - t[i]
        k1 = f(y[i], t[i])
        k2 = f(y[i] + k1 * h / 2, t[i] + h / 2)
        y[i + 1] = y[i] + h * k2
    return y

# Backward Euler method with Newton-Raphson
def backward_euler(f, dfdx, t, y0 = 0, max_iter=100, tol=1e-6):
    n = len(t)
    y = np.zeros(n)
    y[0] = y0
    
    for i in range(1, n):
        y_guess = y[i - 1]
        
        for iteration in range(max_iter):
            # Calculate the residual using Backward Euler
            residual = y_guess - y[i - 1] - (t[i] - t[i - 1]) * f(y_guess, t[i])
            
            if abs(residual) < tol:
                y[i] = y_guess
                break
            
            # Calculate the Jacobian (df/dy)
            jacobian = 1 - (t[i] - t[i - 1]) * dfdx(y_guess, t[i])
            
            # Update the guess using the Newton-Raphson method
            y_guess -= residual / jacobian
        
        if iteration >= max_iter - 1:
            raise Exception("Newton-Raphson did not converge.")
    
    return y
