# default value should be immutable type: string, int, True, False, None
def a(x, y='y'):
    print(x, y)
    return dict(x=x, y=y)


def b(x, y=None):
    return dict(x=x, y=y)


def c(x, y=1):
    return dict(x=x, y=y)


_no_value = object()
def d(x, y=_no_value):
    if y is _no_value:
        print('no b value supplied')


d(1)
d(1, 2)
