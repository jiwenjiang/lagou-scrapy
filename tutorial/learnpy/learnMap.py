from functools import reduce

a = [1, 2, 3, 4, 5]


def square(x):
    return x * x


for x in a:
    square(x)
r = map(square, a)
c = map(lambda x: x * x, a)
v = reduce(lambda x, y: x + y, a)
print(list(r))
print(list(c))
print(v)
