import time


def decoratoer(func):
    def fn():
        print(time.time())
        func()

    return fn


def f1():
    print('fn1')


@decoratoer
def f2():
    print('fn2')


f = decoratoer(f1)()
for x in range(1, 99999):
    pass
f2()
