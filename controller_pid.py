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

# Controller PID
def pid_controller(setpoint, measurement, prev_error, integral, dt, Kp, Ki, Kd):
    error = setpoint - measurement
    integral += error * dt
    derivative = (error - prev_error) / dt
    output = Kp * error + Ki * integral + Kd * derivative
    return output, error, integral

# Simulasi
t = np.linspace(0, 50, 500)  # Waktu simulasi
setpoint = 1.0               # Setpoint
y = np.zeros(len(t))         # Output sistem
u = np.zeros(len(t))         # Input sistem (kontrol)
y0 = 0.0                     # Kondisi awal
prev_error = 0.0             # Kesalahan sebelumnya
integral = 0.0               # Integral kesalahan

# Parameter PID
Kp = 2.0
Ki = 0.1
Kd = 1.0

for i in range(1, len(t)):
    dt = t[i] - t[i-1]
    # Hitung input (kontrol)
    u[i], prev_error, integral = pid_controller(setpoint, y[i-1], prev_error, integral, dt, Kp, Ki, Kd)
    
    # Integrasikan sistem
    tspan = [t[i-1], t[i]]
    ysol = odeint(system, y0, tspan, args=(u[i],))
    y[i] = ysol[1]
    y0 = ysol[1]

# Plot hasil simulasi
plt.figure()
plt.plot(t, y, label='Output (y)')
plt.plot(t, setpoint * np.ones_like(t), 'r--', label='Setpoint')
plt.plot(t, u, label='Control (u)')
plt.xlabel('Time')
plt.ylabel('Output / Control')
plt.title('Simulasi Controller PID')
plt.legend()
plt.grid()
plt.show()
