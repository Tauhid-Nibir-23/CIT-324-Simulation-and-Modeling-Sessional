
import random

numbers = []

for i in range(100):
    num = random.uniform(0, 1)
    numbers.append(num)

for i in range(100):
    print(i + 1, ".", round(numbers[i], 3))
