import random

inter_arrival = []

for i in range(1000):
    num = random.expovariate(1/5)
    inter_arrival.append(num)

print("Inter-arrival Times:")
for i, num in enumerate(inter_arrival, start=1):
    print(f"{i}. {num:.3f}")