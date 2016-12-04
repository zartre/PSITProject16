"""
    This Program is used to make bar graph from file CSV.
    This graph is All internet usage shopping in 2558
"""
import csv
import pygal
with open('All_usage.csv', newline='') as csvfile:
    a = csv.reader(csvfile)
    list_types = []
    list_2013 = []
    list_2014 = []
    list_2015 = []
    for types, first, seccond, third in a:
        list_types.append(types)
        list_2013.append(first)
        list_2014.append(seccond)
        list_2015.append(third)
    line_chart = pygal.Bar()
    line_chart.title = 'All internet usage since 2013 to 2015 (Percentage)'
    line_chart.x_labels = list_types[1:]
    line_chart.add('2013', [float(i) for i in list_2013[1:]])
    line_chart.add('2014',  [float(i)  for i in list_2014[1:]])
    line_chart.add('2015',  [float(i)  for i in list_2015[1:]])
    line_chart.render_to_file('line_chart2.svg')