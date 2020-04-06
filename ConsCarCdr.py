


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def char(pair):
    def get_first(item1, item2):
        return item1
    return pair(get_first)


def cdr(pair):
    def get_last(item1, item2):
        return item2
    return pair(get_last)


print(char(cons(3,4)))
print(cdr(cons(3, 4)))