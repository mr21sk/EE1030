import matplotlib.pyplot as plt

x = [-2, 3, -1, 1, -3] 
y = [4, -1, 0, 2, -5] 

plt.scatter(x, y, color='blue', marker='o') 

for (i, j) in zip(x, y):
    plt.text(i, j, f'({i}, {j})', fontsize=9, ha='right')

plt.title('Scatter Plot of Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.grid(True)

plt.show()
