import subprocess
import numpy as np
import matplotlib.pyplot as plt


# Step 3: Load points from the generated file
points = np.loadtxt('ellipse_points.txt', delimiter=',')  # Load x and y points

# Step 4: Extract x and y values
x = points[:, 0]
y = points[:, 1]

# Step 5: Plot the ellipse
plt.figure(figsize=(8, 6))
a = 2 #semimajor axis
b = 3 #semiminor axis
center_x = 0
center_y = 0
vertices = [(0,-3),(0,3)]
covertices = [(2,0),(-2,0)]
center = [(0,0)]
plt.plot(x, y, label='Ellipse', color='blue')
plt.scatter(*zip(*covertices),color ="red",label="vertices")
plt.scatter(*zip(*vertices),color = "green", label = "covertices")
plt.scatter(*zip(*center),color="yellow",label = "center")
plt.fill(x, y, color='lightblue', alpha=0.3)  # Fill the ellipse with color
plt.xlabel('X-axis')

# Plot vertices
for vertex in vertices:
    plt.plot(*vertex, 'ro') 
    plt.text(vertex[0], vertex[1], f'{vertex}', fontsize=10, ha='left', color='red')

# Plot co-vertices
for covertex in covertices:
    plt.plot(*covertex, 'go')  
    plt.text(covertex[0], covertex[1],f'{covertex}', fontsize=10, ha='left', color='green')

# plot center point
for center in center:    
    plt.plot(*center, 'yo')  
    plt.text(center[0], center[1], f'{center}', fontsize=10, ha='left', color='yellow')

plt.ylabel('Y-axis')
plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')  
plt.axvline(0, color='gray', linewidth=0.5, linestyle='--')  
plt.xlim(-5, 5) 
plt.ylim(-4, 4)  
plt.gca().set_aspect('equal', adjustable='box')  
plt.grid(True)
plt.legend()
plt.show()

