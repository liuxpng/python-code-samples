def kw_only_args1(x, *args, y):
    print(args)
    return dict()

# kw_only_args1('x')  # this will not work
kw_only_args1('x', y='y')


# y is a kw args and it is required
def kw_only_args2(x, *, y):
    return dict()

