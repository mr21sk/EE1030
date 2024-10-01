import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the ellipse
a = 4  # semi-major axis (sqrt(16))
b = 3  # semi-minor axis (sqrt(9))

# Create an array of angles from 0 to 2*pi
theta = np.linspace(0, 2 * np.pi, 100)

# Parametric equations for the ellipse
x = a * np.cos(theta)
y = b * np.sin(theta)

# Plotting the ellipse and shading the area inside
plt.figure(figsize=(8, 6))
plt.fill(x, y, color='lightblue', alpha=0.5, label='Shaded Area')  # Shade the ellipse
plt.plot(x, y, color='blue')  # Outline the ellipse
plt.plot(x, y, label=r'$\frac{x^2}{16} + \frac{y^2}{9} = 1$', color='blue')
plt.title('Plot of the Ellipse with Shaded Area')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.axis('equal')  # Equal scaling for x and y axes
plt.legend()
plt.xlim(-5, 5)
plt.ylim(-4, 4)
plt.show()

