"""
    This Program is used to make bar graph from file CSV.
    This graph is All internet usage device in 2558
"""
import csv
import pygal
import cairo
with open('2558_devices.csv',newline='') as csvfile:
    a = csv.reader(csvfile)
    lst = []
    lst2 = []
    lst3 = []
    for device, male, female in a:
        lst.append(device)
        lst2.append(male)
        lst3.append(female)
    line_chart = pygal.Bar()
    line_chart.title = 'All internet usage device 2558 (in %)'
    line_chart.x_labels = lst[1:]
    line_chart.add('Male', [float(i) for i in lst2[1:]])
    line_chart.add('Female',  [float(i)  for i in lst3[1:]])
    line_chart.render_to_file('line_chart2.svg')                          # Save the svg to a file
