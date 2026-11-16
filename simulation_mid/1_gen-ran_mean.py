import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate 100 random numbers
np.random.seed(10)

numbers = np.random.rand(100)

# Step 2: Calculate Mean, Minimum and Standard Deviation
mean_value = np.mean(numbers)
min_value = np.min(numbers)
std_value = np.std(numbers)

print("For 100 Random Numbers")
print("Mean =", round(mean_value, 4))
print("Minimum =", round(min_value, 4))
print("Standard Deviation =", round(std_value, 4))


# Step 3: Generate 100 random numbers again
numbers2 = np.random.rand(100)

mean2 = np.mean(numbers2)

print("\nFor Second 100 Random Numbers")
print("Mean =", round(mean2, 4))


# Step 4: Use the same random seed
np.random.seed(10)

numbers3 = np.random.rand(100)

mean3 = np.mean(numbers3)

print("\nUsing Same Random Seed")
print("Mean =", round(mean3, 4))


# Step 5: Generate 10000 random numbers
numbers4 = np.random.rand(10000)

mean4 = np.mean(numbers4)
min4 = np.min(numbers4)
std4 = np.std(numbers4)

print("\nFor 10000 Random Numbers")
print("Mean =", round(mean4, 4))
print("Minimum =", round(min4, 4))
print("Standard Deviation =", round(std4, 4))


# Step 6: Draw Histogram
plt.figure(figsize=(10, 5))  #(width,height)

plt.hist(numbers, bins=10, edgecolor="black") #bins mane width ke koy vage  vag korbe 

plt.title("Histogram of 100 Random Numbers")
plt.xlabel("Random Number")
plt.ylabel("Frequency")

plt.grid()
plt.show()



# Step 7: Compare 100 and 10000 numbers

plt.figure(figsize=(10, 5))

plt.hist(numbers, bins=10, density=True,
         alpha=0.7, label="100 Numbers",
         edgecolor="black")

plt.hist(numbers4, bins=10, density=True,
         alpha=0.5, label="10000 Numbers",
         edgecolor="black")

plt.title("Comparison: 100 vs 10000 Random Numbers")
plt.xlabel("Random Number")
plt.ylabel("Density")

plt.legend()
plt.grid()
plt.show()
