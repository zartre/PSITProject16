"""
Internet Usage Behaviours of Thai Netizens

A Project by:
Nathan Yiangsupapaanontr,
Rattanachat Sooksumpus,
Thanathep Thaithae and
Thanpisit Wattanasomvong

For help, please refer to the documentation or type help.
"""

import csv
import pygal

# desktop2557
def view_2557_usage_desktop():
    with open('data/2557_usage_desktop.csv', newline='') as csvfile:
        a = csv.reader(csvfile)
        list_types = []
        list_male = []
        list_female = []
        for types, male, female in a:
            list_types.append(types)
            list_male.append(male)
            list_female.append(female)
        line_chart = pygal.Bar()
        line_chart.title = 'All internet usage desktop 2557 (in %)'
        line_chart.x_labels = list_types[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_desktop_usage_2557.svg')

# desktop2558
def view_2558_usage_desktop():
    with open('data/2558_usage_mobile.csv', newline='') as csvfile:
        a = csv.reader(csvfile)
        list_types = []
        list_male = []
        list_female = []
        for types, male, female in a:
            list_types.append(types)
            list_male.append(male)
            list_female.append(female)
        line_chart = pygal.Bar()
        line_chart.title = 'All internet usage mobile 2558 (in %)'
        line_chart.x_labels = list_types[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_desktop_usage_2558.svg')

# device2556
def view_2557_devices():
    with open('data/2556_devices.csv',newline='') as csvfile:
        a = csv.reader(csvfile)
        lst = []
        lst2 = []
        lst3 = []
        for device, male, female in a:
            lst.append(device)
            lst2.append(male)
            lst3.append(female)
        line_chart = pygal.Bar()
        line_chart.title = 'All internet usage device 2556 (in %)'
        line_chart.x_labels = lst[1:]
        line_chart.add('Male', [float(i) for i in lst2[1:]])
        line_chart.add('Female',  [float(i)  for i in lst3[1:]])
        line_chart.render_to_file('chart_devices_2556.svg')

# device2558
def view_2558_devices():
    with open('data/2558_devices.csv',newline='') as csvfile:
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
        line_chart.render_to_file('chart_devices_2558.svg')

# locations2557
def view_2557_locations():
    with open('data/2557_locations.csv', newline='') as csvfile:
        a = csv.reader(csvfile)
        list_local = []
        list_male = []
        list_female = []
        for locations, male, female in a:
            list_local.append(locations)
            list_male.append(male)
            list_female.append(female)
        line_chart = pygal.Bar()
        line_chart.title = 'All internet usage locations 2557 (in %)'
        line_chart.x_labels = list_local[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_locations_2557.svg')

# locations2558
def view_2558_locations():
    with open('data/2558_locations.csv', newline='') as csvfile:
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
        line_chart.render_to_file('chart_locations_2558.svg')

# mobile2557
def view_2557_usage_mobile():
    with open('data/2557_usage_mobile.csv', newline='') as csvfile:
        a = csv.reader(csvfile)
        list_types = []
        list_male = []
        list_female = []
        for types, male, female in a:
            list_types.append(types)
            list_male.append(male)
            list_female.append(female)
        line_chart = pygal.Bar()
        line_chart.title = 'All internet usage mobile 2557 (in %)'
        line_chart.x_labels = list_types[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_mobile_usage_2557.svg')

# mobile2558
def view_2558_usage_mobile():
    with open('data/2558_usage_mobile.csv', newline='') as csvfile:
        a = csv.reader(csvfile)
        list_types = []
        list_male = []
        list_female = []
        for types, male, female in a:
            list_types.append(types)
            list_male.append(male)
            list_female.append(female)
        line_chart = pygal.Bar()
        line_chart.title = 'All internet usage mobile 2558 (in %)'
        line_chart.x_labels = list_types[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_mobile_usage_2558.svg')

# shopping2558
def view_2558_shopping():
    with open('data/2558_shopping.csv', newline='') as csvfile:
        a = csv.reader(csvfile)
        list_types = []
        list_male = []
        list_female = []
        for types, male, female in a:
            list_types.append(types)
            list_male.append(male)
            list_female.append(female)
        line_chart = pygal.Bar()
        line_chart.title = 'All internet usage shopping 2558 (in %)'
        line_chart.x_labels = list_types[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_shopping_2558.svg')

# usagetypes2556
def view_2556_purposes():
    with open('data/2556_usage_all.csv', newline='') as csvfile:
        a = csv.reader(csvfile)
        list_types = []
        list_male = []
        list_female = []
        for types, male, female in a:
            list_types.append(types)
            list_male.append(male)
            list_female.append(female)
        line_chart = pygal.Bar()
        line_chart.title = 'All internet usage type 2556 (in %)'
        line_chart.x_labels = list_types[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_internet.svg')

view_2557_usage_desktop()
view_2558_usage_desktop()
view_2557_devices()
view_2558_devices()
view_2557_locations()
view_2558_locations()
view_2557_usage_mobile()
view_2558_usage_mobile()
view_2558_shopping()
view_2556_purposes()
print("Charts created successfully!")
