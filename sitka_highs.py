import csv

import matplotlib.pyplot as plt


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    #for index, column_header in enumerate(header_row):
        #print(index, column_header)

    # Получить высокие температуры с этого файла.
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# Создать график высоких температур.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Отформотировать график.
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

print(highs)