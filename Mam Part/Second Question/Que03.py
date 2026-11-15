import random
import matplotlib.pyplot as plt

inter_arrival = []

for i in range(1000):
    num = random.expovariate(1/5)
    inter_arrival.append(num)

service_time = []

for i in range(1000):
    num = random.uniform(2, 8)
    service_time.append(num)

# Inter-arrival time histogram
plt.subplot(1, 2, 1)
plt.hist(inter_arrival, bins=20, edgecolor="black")
plt.title("Inter-arrival Time")
plt.xlabel("Time (minutes)")
plt.ylabel("Frequency")

# Service time histogram
plt.subplot(1, 2, 2)
plt.hist(service_time, bins=20, edgecolor="black")
plt.title("Service Time")
plt.xlabel("Time (minutes)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()