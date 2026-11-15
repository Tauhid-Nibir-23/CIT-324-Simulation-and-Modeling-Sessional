import random
import math

def is_inside(x, y):
    return (x**2 + y**2) <= 81

def estimate_area(x_min, x_max, y_min, y_max, total_points=100000):
    bounding_box_area = (x_max - x_min) * (y_max - y_min)
    inside_count = 0

    for _ in range(total_points):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)

        if is_inside(x, y):
            inside_count += 1

    p = inside_count / total_points
    estimated_area = bounding_box_area * p
    standard_error = bounding_box_area * math.sqrt(p * (1 - p) / total_points)

    return estimated_area, inside_count, bounding_box_area, standard_error

if __name__ == "__main__":
    X_MIN, X_MAX = 0.0, 9.0
    Y_MIN, Y_MAX = 0.0, 9.0
    
    N = 100000

    area, inside_pts, box_area, std_err = estimate_area(X_MIN, X_MAX, Y_MIN, Y_MAX, N)

    print("=" * 50)
    print("      MONTE CARLO AREA ESTIMATION RESULTS      ")
    print("=" * 50)
    print(f"Bounding Box Range : x in [{X_MIN}, {X_MAX}], y in [{Y_MIN}, {Y_MAX}]")
    print(f"Bounding Box Area  : {box_area:.4f}")
    print(f"Total Points (N)   : {N:,}")
    print(f"Points Inside (M)  : {inside_pts:,}")
    print(f"Estimated Area     : {area:.6f}")
    print(f"Standard Error     : ±{std_err:.6f}")
    print(f"95% Confidence Int : [{area - 1.96 * std_err:.6f}, {area + 1.96 * std_err:.6f}]")
    print("=" * 50)