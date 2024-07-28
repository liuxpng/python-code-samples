def cal_sum(first, *rest):
    print(rest)
    return first + sum(rest)

a = cal_sum(1, 2, 3, 4, 5, 6, 7)
print(a)


def comb_dict(first, **rest):
    print(rest)
    return {
        'first': first,
        'rest': rest
    }


b = comb_dict('first_value', k1='v1', k2='v2', k3='v3')
print(b)


def any_args(x, *args, **kwargs):
    print(args)
    print(kwargs)
    return dict(x=x, args=args, kwargs=kwargs)


c = any_args('x', 1, 2, 3, 4, y='y', z='z')
print(c)


def kw_only_args(x, *y, z, **j):
    print(y)
    print(z)
    print(j)
    return dict(x=x, y=y, z=z, j=j)


d = kw_only_args('x', 1, 2, z=4)
print(d)

