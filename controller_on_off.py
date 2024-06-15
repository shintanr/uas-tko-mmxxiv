import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameter sistem
tau = 5.0  # Konstanta waktu sistem
K = 1.0    # Penguatan sistem

# Fungsi alih sistem orde pertama
def system(y, t, u):
    dydt = (-y + K * u) / tau
    return dydt

# Controller On-Off
def on_off_controller(setpoint, measurement):
    if measurement < setpoint:
        return 1  # Aktuator ON
    else:
        return 0  # Aktuator OFF

# Simulasi
t = np.linspace(0, 50, 500)  # Waktu simulasi
setpoint = 1.0               # Setpoint
y = np.zeros(len(t))         # Output sistem
u = np.zeros(len(t))         # Input sistem (kontrol)
y0 = 0.0                     # Kondisi awal

for i in range(1, len(t)):
    # Hitung input (kontrol)
    u[i] = on_off_controller(setpoint, y[i-1])
    
    # Integrasikan sistem
    tspan = [t[i-1], t[i]]
    ysol = odeint(system, y0, tspan, args=(u[i],))
    y[i] = ysol[1]
    y0 = ysol[1]

# Plot hasil simulasi
plt.figure()
plt.plot(t, y, label='Output (y)')
plt.plot(t, setpoint * np.ones_like(t), 'r--', label='Setpoint')
plt.step(t, u, label='Control (u)', where='post')
plt.xlabel('Time')
plt.ylabel('Output / Control')
plt.title('Simulasi Controller On-Off')
plt.legend()
plt.grid()
plt.show()
