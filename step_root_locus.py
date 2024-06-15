import numpy as np
import matplotlib.pyplot as plt
from control import tf, rlocus, step_response

# Langkah 1: Definisikan parameter sistem
omega_n = 1.0  # Frekuensi alami
zeta = 0.5     # Rasio redaman
A = 1.0        # Amplitudo masukan step

# Langkah 2: Definisikan fungsi alih H(s)
omega = omega_n
numerator = [omega**2]
denominator = [1, 2*zeta*omega, omega**2]
H = tf(numerator, denominator)

# Langkah 3: Analisis root locus
plt.figure()
rlocus(H)
plt.title('Root Locus of the System')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.grid(True)

# Langkah 4: Simulasi respon waktu
t = np.linspace(0, 10, 1000)  # Waktu simulasi
t, y = step_response(H, T=t)

# Langkah 5: Plotting
plt.figure()
plt.plot(t, A * y)
plt.title('Step Response of the System')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.grid(True)
plt.show()
