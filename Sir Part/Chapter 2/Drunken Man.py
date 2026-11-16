
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Random Numbers
RN = [6, 2, 0, 6, 2, 8, 5, 7, 7, 9,
      8, 4, 8, 2, 6, 2, 1, 3, 0, 8]

# Step 2: Starting Position
x = 0
y = 0

X = [x]
Y = [y]

# Step 3: Simulate 20 Steps
for r in RN:

    if r == 0:
        y = y - 30       # Backward

    elif r <= 5:
        y = y + 80       # Forward

    elif r <= 7:
        x = x + 60       # Right

    else:
        x = x - 40       # Left

    X.append(x)
    Y.append(y)

# Step 4: Final Position
print("Final X =", x, "cm")
print("Final Y =", y, "cm")

# Step 5: Draw Graph
plt.figure(figsize=(8, 6))

plt.plot(X, Y, marker='o', color='blue')

plt.scatter(X[0], Y[0], color='green', label='Start')
plt.scatter(X[-1], Y[-1], color='red', label='End')

plt.xlabel("X (cm)")
plt.ylabel("Y (cm)")
plt.title("Drunkard's Walk Simulation")

plt.legend()
plt.grid()
plt.show()
