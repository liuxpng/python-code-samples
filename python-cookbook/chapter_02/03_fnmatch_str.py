
from fnmatch import fnmatch, fnmatchcase

filename = 'test.csv'
print(fnmatch(filename, 'csv'))
print(fnmatch(filename, '*.csv'))


filename = 'TEST.PY'

print(fnmatch(filename, '*.py'))
print(fnmatchcase(filename, '*.PY'))
