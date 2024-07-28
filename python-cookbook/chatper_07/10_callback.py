def a(*, callback):
    callback(1,2,3)


class Handler:
    def __init__(self):
        self.seq = 0

    def handler(self, *r):
        self.seq += 1
        print("{} Got: {}".format(self.seq, r))


handler = Handler().handler
a(callback=handler)
a(callback=handler)
a(callback=handler)
a(callback=handler)


def handler(seq):
    def inner(*r):
        nonlocal seq
        seq += 1
        print("{} Got: {}".format(seq, r))

    return inner


handler = handler(0)
a(callback=handler)
a(callback=handler)
a(callback=handler)
a(callback=handler)
