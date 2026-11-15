import random
inter_arrival = []

for i in range(1000):
    num = random.expovariate(1/5)
    inter_arrival.append(num)

# Calculate mean
mean = sum(inter_arrival) / len(inter_arrival)

# Calculate standard deviation
total = 0

for num in inter_arrival:
    total = total + (num - mean) ** 2

variance = total / (len(inter_arrival) - 1)

std_dev = variance ** 0.5

print("Mean:", mean)
print("Standard Deviation:", std_dev)


service_time = []

for i in range(1000):
    num = random.uniform(2, 8)
    service_time.append(num)

# Calculate mean
mean = sum(service_time) / len(service_time)

# Calculate standard deviation
total = 0

for num in service_time:
    total = total + (num - mean) ** 2

variance = total / (len(service_time) - 1)

std_dev = variance ** 0.5

print("Mean:", mean)
print("Standard Deviation:", std_dev)