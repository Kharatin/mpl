import  matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Дать названия графику и осям.
ax.set_title("Squar Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Задать размер шрифта для надписей на розметке.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()