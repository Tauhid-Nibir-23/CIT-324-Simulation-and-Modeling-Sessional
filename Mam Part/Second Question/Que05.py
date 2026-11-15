
import random

# Generate Inter-arrival Times
inter_arrival = []

for i in range(1000):
    num = random.expovariate(1/5)
    inter_arrival.append(num)


# Generate Service Times
service_time = []

for i in range(1000):
    num = random.uniform(2, 8)
    service_time.append(num)


# Calculate Inter-arrival Mean
mean1 = sum(inter_arrival) / len(inter_arrival)

# Calculate Inter-arrival SD
total = 0

for num in inter_arrival:
    total = total + (num - mean1) ** 2

variance = total / (len(inter_arrival) - 1)
sd1 = variance ** 0.5


# Calculate Service Mean
mean2 = sum(service_time) / len(service_time)

# Calculate Service SD
total = 0

for num in service_time:
    total = total + (num - mean2) ** 2

variance = total / (len(service_time) - 1)
sd2 = variance ** 0.5


# Theoretical Values
theoretical_mean1 = 5
theoretical_sd1 = 5

theoretical_mean2 = (2 + 8) / 2
theoretical_sd2 = (8 - 2) / (12 ** 0.5)


# Final Comparison
print("===== INTER-ARRIVAL TIME =====")

print("Sample Mean:", round(mean1, 3))
print("Theoretical Mean:", theoretical_mean1)

print("Sample SD:", round(sd1, 3))
print("Theoretical SD:", theoretical_sd1)


print("\n===== SERVICE TIME =====")

print("Sample Mean:", round(mean2, 3))
print("Theoretical Mean:", theoretical_mean2)

print("Sample SD:", round(sd2, 3))
print("Theoretical SD:", round(theoretical_sd2, 3))
