
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

sorted_rows = sorted(rows, key=itemgetter('fname'))
print(sorted_rows)

sorted_rows = sorted(rows, key=itemgetter('fname', 'lname'))
print(sorted_rows)

sorted_rows = sorted(rows, key=lambda v: (v['fname'], v['lname']))
print(sorted_rows)
