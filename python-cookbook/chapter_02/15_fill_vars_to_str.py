s = 'hello {}'
print(s.format('python'))

s = 'hello {name}'
print(s.format(name='python'))


name = 'python'
print(s.format_map(vars()))
print(s.format_map({'name': 'python'}))


class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


s = 'Your gender is {gender}'
print(s.format_map(safesub(vars())))
