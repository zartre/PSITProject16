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
from time import sleep

print("\nInternet Usage Behaviours of Thai Netizens\n\n A Project by:\n \
Nathan Yiangsupapaanontr,\n Rattanachat Sooksumpus,\n \
Thanathep Thaithae and\n Thanpisit Wattanasomvong\n\n\
Charts are created in the project's root.")

def view_2557_usage_desktop():
    """ Analytic graph for types of usage via desktops in 2557 """
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

def view_2558_usage_desktop():
    """ Analytic graph for types of usage via desktops in 2558 """
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

def view_2556_devices():
    """ Analytic graph for types of Internet access devices in 2556 """
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

def view_2558_devices():
    """ Analytic graph for types of Internet access devices in 2558 """
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

def view_2557_locations():
    """ Analytic graph for Internet usage locations in 2557 """
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

def view_2558_locations():
    """ Analytic graph for Internet usage locations in 2558 """
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

def view_2557_usage_mobile():
    """ Analytic graph for types of usage via mobile devies in 2557 """
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

def view_2558_usage_mobile():
    """ Analytic graph for types of usage via mobile devies in 2558 """
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

def view_2558_shopping():
    """ Analytic graph for genres of online shopping in 2558 """
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

def view_2556_purposes():
    """ Analytic graph for types of Internet usage in 2556 """
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

def create_chart():
    """ Asks the user for inputs """
    available = ["Usages on desktops", "Usages on mobiles", "Device types",\
    "Usage locations", "Shopping genres", "Usage types", "All"]
    item = 1
    print("\nWhich chart do you want to generate?")
    for i in available:
        print("[%d] %s" %(item, i))
        item += 1
    user_wants = input("\nType a number or type STOP to terminate: ")
    if user_wants == '5':
        view_2558_shopping()
        print("\nChart created successfully!")
    elif user_wants == '6':
        view_2556_purposes()
        print("\nChart created successfully!")
    elif user_wants == '1':
        year = input("2014 or 2015: ")
        if year == "2014":
            view_2557_usage_desktop()
            print("\nChart created successfully!")
        elif year == "2015":
            view_2558_usage_desktop()
            print("\nChart created successfully!")
        else:
            print("Invalid command.")
    elif user_wants == '2':
        year = input("2014 or 2015: ")
        if year == "2014":
            view_2557_usage_mobile()
            print("\nChart created successfully!")
        elif year == "2015":
            view_2558_usage_mobile()
            print("\nChart created successfully!")
        else:
            print("Invalid command.")
    elif user_wants == '3':
        year = input("2014 or 2015: ")
        if year == "2014":
            view_2557_devices()
            print("\nChart created successfully!")
        elif year == "2015":
            view_2558_devices()
            print("\nChart created successfully!")
        else:
            print("Invalid command.")
    elif user_wants == '4':
        year = input("2014 or 2015: ")
        if year == "2014":
            view_2557_locations()
            print("\nChart created successfully!")
        elif year == "2015":
            view_2558_locations()
            print("\nChart created successfully!")
        else:
            print("Invalid command.")
    elif user_wants == '7':
        view_2557_usage_desktop() # 1
        view_2558_usage_desktop()
        view_2556_devices() # 3
        view_2558_devices()
        view_2557_locations() # 4
        view_2558_locations()
        view_2557_usage_mobile() # 2
        view_2558_usage_mobile()
        view_2558_shopping() # 5
        view_2556_purposes() # 6
        print("\nCharts created successfully!")
    elif user_wants.lower() == "stop":
        return "stop"
    else:
        print("Invalid command.")
    sleep(1)

while 1:
    if create_chart() == "stop":
        print("\nBye!\n")
        break

# view_2557_usage_desktop() 1
# view_2558_usage_desktop() 1
# view_2556_devices() 3
# view_2558_devices() 3
# view_2557_locations() 4
# view_2558_locations() 4
# view_2557_usage_mobile() 2
# view_2558_usage_mobile() 2
# view_2558_shopping() 5
# view_2556_purposes() 6
