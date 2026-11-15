import random

numbers = []

for i in range(100):
    num = random.uniform(0, 1)
    numbers.append(num)

mean = sum(numbers) / len(numbers)

minimum = min(numbers)

total = 0

for num in numbers:
    total = total + (num - mean) ** 2

dev = total / len(numbers)

std_dev = dev ** 0.5

print("Mean:", mean)
print("Minimum:", minimum)
print("Standard Deviation:", std_dev)