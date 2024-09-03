import matplotlib.pyplot as plt

# Read the data from the file
def read_data(filename):
    x_coords = []
    y_coords = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(int, line.split())
            x_coords.append(x)
            y_coords.append(y)
    return x_coords, y_coords

# Plot the data
def plot_points(x, y):
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', marker='o')  # Scatter plot
    for i, (x_i, y_i) in enumerate(zip(x, y)):
        plt.text(x_i, y_i, f"({x_i:.2f}, {y_i:.2f})")
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('2D Plot of Points')
    plt.axhline(0, color='red',linewidth=0.5)
    plt.axvline(0, color='red',linewidth=0.5)
    plt.grid(True)
    plt.show()
    

# Get data and plot
x, y = read_data('data.txt')
plot_points(x, y)
plt.show()

