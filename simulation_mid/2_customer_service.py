
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate 1000 Inter-arrival Times
np.random.seed(10)

inter_arrival = np.random.exponential(scale=5, size=1000)

# Step 2: Generate 1000 Service Times

service_time = np.random.uniform(2, 8, 1000)


# Step 3: Calculate Mean and Standard Deviation

mean_inter = np.mean(inter_arrival)
std_inter = np.std(inter_arrival, ddof=1)

mean_service = np.mean(service_time)
std_service = np.std(service_time, ddof=1)


# Step 4: Calculate Theoretical Values

theory_mean_inter = 5
theory_std_inter = 5

theory_mean_service = (2 + 8) / 2
theory_std_service = (8 - 2) / np.sqrt(12)


# Step 5: Print Results

print("Inter-arrival Time")
print("Sample Mean =", round(mean_inter, 2))
print("Sample Standard Deviation =", round(std_inter, 2))

print("\nTheoretical Mean =", theory_mean_inter)
print("Theoretical Standard Deviation =", theory_std_inter)


print("\nService Time")
print("Sample Mean =", round(mean_service, 2))
print("Sample Standard Deviation =", round(std_service, 2))

print("\nTheoretical Mean =", round(theory_mean_service, 2))
print("Theoretical Standard Deviation =", round(theory_std_service, 2))


# Step 6: Histogram of Inter-arrival Time

plt.figure(figsize=(10, 5))

plt.hist(inter_arrival, bins=20, edgecolor="black")

plt.title("Histogram of Inter-arrival Time")
plt.xlabel("Time (Minutes)")
plt.ylabel("Frequency")

plt.grid()
plt.show()


# Step 7: Histogram of Service Time

plt.figure(figsize=(10, 5))

plt.hist(service_time, bins=20, edgecolor="black")

plt.title("Histogram of Service Time")
plt.xlabel("Time (Minutes)")
plt.ylabel("Frequency")

plt.grid()
plt.show()
