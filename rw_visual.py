import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Создай случайное блуждание.
rw = RandomWalk()
rw.fill_walk()
# Нанести на график точки блуждания.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
