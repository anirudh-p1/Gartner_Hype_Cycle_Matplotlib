import numpy as np
import matplotlib.pyplot as plt

# Define the range (x-axis)
x = np.linspace(0, 40, 1000)

# Formula for the hype cycle
y = (10 * x**2 / np.exp(0.6 * x)) + (5 / (0.5 + np.exp(-(x - 15)))) + 0.1 * x

# Create plot
plt.figure(figsize=(10, 6), facecolor='#0d1117')
ax = plt.gca()
ax.set_facecolor('#0d1117')

# Plot the curve
plt.plot(x, y, color='#58a6ff', linewidth=3)

# Add the point 
plt.scatter(16, 7.5, color='#79c0ff', s=120, zorder=5)

# Turn off axis
plt.axis('off')

# Result
plt.show()
