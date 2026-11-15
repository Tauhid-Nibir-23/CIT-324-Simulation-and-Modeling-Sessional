import random

random.seed(23)

numbers1 = []

for i in range(100):
    numbers1.append(random.uniform(0, 1))

mean1 = sum(numbers1) / len(numbers1)

random.seed(23)

numbers2 = []

for i in range(100):
    numbers2.append(random.uniform(0, 1))

mean2 = sum(numbers2) / len(numbers2)


print("First Mean:", mean1)
print("Second Mean:", mean2)

if mean1 == mean2:
    print("Means are same")
else:
    print("Means are different")