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

print("Internet Usage Behaviours of Thai Netizens \n\n A Project by:\n Nathan Yiangsupapaanontr,\n Rattanachat Sooksumpus, \n \
Thanathep Thaithae and\n Thanpisit Wattanasomvong \n\n For help, please refer to the documentation or type help.\n\n")
print("Please wait while we creating charts....")
# desktop2557
def view_2557_usage_desktop():
    """ Analytic graph for type of usage via desktops platform in 2557 """
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
        line_chart.title = 'Types of Internet Usage on Desktops in 2014 (percentage)'
        line_chart.x_labels = list_types[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_desktop_usage_2557.svg')

# desktop2558
def view_2558_usage_desktop():
    """ Analytic graph for type of usage via desktops platform in 2558 """
    with open('data/2558_usage_desktop.csv', newline='') as csvfile:
        a = csv.reader(csvfile)
        list_types = []
        list_male = []
        list_female = []
        for types, male, female in a:
            list_types.append(types)
            list_male.append(male)
            list_female.append(female)
        line_chart = pygal.Bar()
        line_chart.title = 'Types of Internet Usage on Desktops in 2015 (percentage)'
        line_chart.x_labels = list_types[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_desktop_usage_2558.svg')

# device2556
def view_2556_devices():
    """ Analytic graph for type of device for internet usage in 2556 """
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
        line_chart.title = 'Internet Access Devices in 2013 (percentage)'
        line_chart.x_labels = lst[1:]
        line_chart.add('Male', [float(i) for i in lst2[1:]])
        line_chart.add('Female',  [float(i)  for i in lst3[1:]])
        line_chart.render_to_file('chart_devices_2556.svg')

# device2558
def view_2558_devices():
    """ Analytic graph for type of device for internet usage in 2558 """
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
        line_chart.title = 'Internet Access Devices in 2015 (percentage)'
        line_chart.x_labels = lst[1:]
        line_chart.add('Male', [float(i) for i in lst2[1:]])
        line_chart.add('Female',  [float(i)  for i in lst3[1:]])
        line_chart.render_to_file('chart_devices_2558.svg')

# locations2557
def view_2557_locations():
    """ Analytic graph for location internet usage being use in 2557 """
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
        line_chart.title = 'Internet Usage Locations in 2014 (percentage)'
        line_chart.x_labels = list_local[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_locations_2557.svg')

# locations2558
def view_2558_locations():
    """ Analytic graph for location internet usage being use in 2558 """
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
        line_chart.title = 'Internet Usage Locations in 2015 (percentage)'
        line_chart.x_labels = list_locations[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_locations_2558.svg')

# mobile2557
def view_2557_usage_mobile():
    """ Analytic graph for type of usage via mobiles platform in 2557 """
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
        line_chart.title = 'Types of Internet Usage on Mobiles in 2014 (percentage)'
        line_chart.x_labels = list_types[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_mobile_usage_2557.svg')

# mobile2558
def view_2558_usage_mobile():
    """ Analytic graph for type of usage via mobiles platform in 2558 """
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
        line_chart.title = 'Types of Internet Usage on Mobiles in 2015 (percentage)'
        line_chart.x_labels = list_types[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_mobile_usage_2558.svg')

# shopping2558
def view_2558_shopping():
    """ Analytic graph for genre of online shopping in 2558 """
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
        line_chart.title = 'Online Shopping Genres in 2015 (percentage)'
        line_chart.x_labels = list_types[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_shopping_2558.svg')

# usagetypes2556
def view_2556_purposes():
    """ Analytic graph for type of internet usage in 2556 """
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
        line_chart.title = 'Internet Usage Types in 2013 (percentage)'
        line_chart.x_labels = list_types[1:]
        line_chart.add('Male', [float(i) for i in list_male[1:]])
        line_chart.add('Female',  [float(i)  for i in list_female[1:]])
        line_chart.render_to_file('chart_internet.svg')

view_2557_usage_desktop()
view_2558_usage_desktop()
view_2556_devices()
view_2558_devices()
view_2557_locations()
view_2558_locations()
view_2557_usage_mobile()
view_2558_usage_mobile()
view_2558_shopping()
view_2556_purposes()

print("\n\nCharts created successfully!")
