def outer():
    seq = 0

    def inner():
        print(seq)

    def get_seq():
        return seq

    def set_seq(s):
        nonlocal seq
        seq = s

    inner.get_seq = get_seq
    inner.set_seq = set_seq

    return inner


a = outer()
print(a.get_seq())

a.set_seq(9)
print(a.get_seq())

a()
