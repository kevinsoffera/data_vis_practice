import matplotlib.pyplot as plt
import numpy as np

from die import Die

# Create two D6.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(1_000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results.
x = list(range(2, max_result+1))

fig, ax = plt.subplots(figsize = (9, 3))
plt.bar(x, frequencies)
plt.suptitle('Sum of two dice rolled 1000 times')

plt.show()
