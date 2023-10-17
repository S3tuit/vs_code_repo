import numpy as np

numbers = [26, 28, 29, 29, 30, 32, 32, 33, 35, 36, 36, 37,37,37,39,39,42,42,43,47,48]

# Sort the data
sorted_numbers = sorted(numbers)

# Calculate Q1 (25th percentile)
q1 = np.percentile(sorted_numbers, 25)

# Calculate Q3 (75th percentile)
q2 = np.percentile(sorted_numbers, 50)

q3 = np.percentile(sorted_numbers, 75)

print(f"Q1: {q1}")
print(f"Q2: {q2}")
print(f"Q3: {q3}")



