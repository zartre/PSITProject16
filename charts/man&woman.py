import pygal
line_chart = pygal.Pie(print_values=True)
line_chart.title = 'สรุปชายหญิงไปแก้เป็นภาษาอังกฤษให้หน่อย (percentage)'
line_chart.add('Men', 43)
line_chart.add('Women', 57)
line_chart.render_to_file('chart_3_year_usage.svg')