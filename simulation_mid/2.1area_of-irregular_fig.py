
import numpy as np
import matplotlib.pyplot as plt

# Total random points
N = 10000

# Generate random points
x = np.random.uniform(0, 2, N)
y = np.random.uniform(0, 5, N)

# Check which points are inside the region
inside = y <= (x**2 + 1)

# Count inside points
inside_count = np.sum(inside)

# Rectangle area
rectangle_area = 2 * 5

# Calculate irregular area
area = (inside_count / N) * rectangle_area

print("Points inside:", inside_count)
print("Total points:", N)
print("Estimated Area:", area)

# Plot the points
plt.scatter(x[inside], y[inside], color='green', s=2, label='Inside')
plt.scatter(x[~inside], y[~inside], color='red', s=2, label='Outside')

plt.title("Monte Carlo Method - Irregular Area")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()









# ==========================================
# 1. PARABOLA
# Equation: y = x^2
# Region: Below the parabola
# ==========================================

inside = y <= x**2


# ==========================================
# 2. CIRCLE
# Equation: x^2 + y^2 = 25
# Region: Inside the circle
# ==========================================

inside = (x**2 + y**2) <= 25


# ==========================================
# 3. BETWEEN TWO CURVES
# Upper curve: y = x + 2
# Lower curve: y = x^2
# Region: Between the two curves
# ==========================================

inside = (y >= x**2) & (y <= x + 2)


# ==========================================
# 4. ELLIPSE
# Equation: x^2/25 + y^2/9 = 1
# Region: Inside the ellipse
# ==========================================

inside = (x**2 / 25) + (y**2 / 9) <= 1
