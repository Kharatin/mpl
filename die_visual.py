from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#  Создать D6(кубик с шестью гранями).
die = Die()

# Сделать несколько бросков и сохранить данные в список.
results = []

for roll_num in range(1000):

    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализировать результаты.
x_value = list(range(1, die.num_sides+1))
data = [Bar(x=x_value, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Result of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')