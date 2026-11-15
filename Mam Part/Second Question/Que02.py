import random

service_time = []

for i in range(1000):
    num = random.uniform(2, 8)
    service_time.append(num)

print("Service Times:")
for i, num in enumerate(service_time, start=1):
    print(f"{i}. {num:.3f}")