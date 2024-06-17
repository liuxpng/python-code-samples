
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

sorted_rows = sorted(rows, key=lambda v: v['date'])
print(sorted_rows)

from operator import itemgetter

sorted_rows = sorted(rows, key=itemgetter('date'))
print(sorted_rows)

from itertools import groupby

print(dict(groupby(sorted_rows, key=itemgetter('date'))))

for date, items in groupby(sorted_rows, key=itemgetter('date')):
    print(date, list(items))
