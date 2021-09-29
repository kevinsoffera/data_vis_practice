import matplotlib.pyplot as plt 

x_values1 = range(1, 6)
y_values1 = [x**3 for x in x_values1]

x_values2 = range(1, 5001)
y_values2 = [x**3 for x in x_values2]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values1, y_values1, c='purple', s = 100)
ax.scatter(x_values2, y_values2, c=x_values2, cmap = plt.cm.magma, s = 10)
plt.show()
