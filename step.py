import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parameter sistem
A = 1
omega_n = 1
zeta = 0.5

# Fungsi alih sistem
num = [0, 0, A * omega_n**2]
den = [1, 2 * zeta * omega_n, omega_n**2]
system = signal.TransferFunction(num, den)

# Masukan step
t_step, y_step = signal.step(system)

# Plot
plt.plot(t_step, y_step, label='Step Response')
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Transient Response of the System to a Step Input')
plt.grid()
plt.legend()
plt.show()
