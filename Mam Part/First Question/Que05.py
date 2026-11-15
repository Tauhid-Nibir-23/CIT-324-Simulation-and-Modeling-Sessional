
import random

numbers = []

for i in range(10000):
    num = random.uniform(0, 1)
    numbers.append(num)

for i in range(10000):
    print(i + 1, ".", round(numbers[i], 3))

mean = sum(numbers) / len(numbers)

minimum = min(numbers)

total = 0

for num in numbers:
    total = total + (num - mean) ** 2

variance = total / len(numbers)

std_dev = variance ** 0.5

print("\nTotal Numbers:", len(numbers))
print("Mean:", mean)
print("Minimum:", minimum)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
