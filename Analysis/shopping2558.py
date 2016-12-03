"""
    This Program is used to make bar graph from file CSV.
    This graph is All internet usage shopping in 2558
"""
import csv
import pygal
import cairo
with open('2557_shopping.csv', newline='') as csvfile:
    a = csv.reader(csvfile)
    list_shoppingtypes = []
    list_male = []
    list_female = []
    for typess, male, female in a:
        list_shoppingtypes.append(types)
        list_male.append(male)
        list_female.append(female)
    line_chart = pygal.Bar()
    line_chart.title = 'All internet usage shopping 2558 (in %)'
    line_chart.x_labels = lst[1:]
    line_chart.add('Male', [float(i) for i in lst2[1:]])
    line_chart.add('Female',  [float(i)  for i in lst3[1:]])
    line_chart.render_to_file('line_chart2.svg')                          # Save the svg to a file
