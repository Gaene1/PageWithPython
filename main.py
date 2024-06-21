import numpy as np
import matplotlib.pyplot as plt


houses = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
points = [715, 517, 470, 482]

plt.bar(houses, points)
plt.ylabel("Hogwarts Points")
plt.xlabel("Hogwarts House")
plt.title("Hogwarts House Points")
plt