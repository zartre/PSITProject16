"""
    This Program is used to make bar graph from file CSV.
    This graph is All internet usage location in 2558
"""
import csv
import pygal
with open('2558_locations.csv', newline='') as csvfile:
    a = csv.reader(csvfile)
    list_locations = []
    list_male = []
    list_female = []
    for locations, male, female in a:
        list_locations.append(locations)
        list_male.append(male)
        list_female.append(female)
    line_chart = pygal.Bar()
    line_chart.title = 'All internet usage location in 2558 (in %)'
    line_chart.x_labels = list_locations[1:]
    line_chart.add('Male', [float(i) for i in list_male[1:]])
    line_chart.add('Female',  [float(i)  for i in list_female[1:]])
    line_chart.render_to_file('line_chart2.svg')                          # Save the svg to a file
