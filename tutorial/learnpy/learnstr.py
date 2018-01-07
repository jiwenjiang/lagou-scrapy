# print(type(()))
# print(max('12asd'))
# print({1, 2, 3, 4} | {2, 3, 5})
# l = [1, 2, 4, 6, 5, 6, 7, 8]
#
# for i in range(0, len(l), 2):
#     print(l[i])
import tutorial

tutorial.sys.setrecursionlimit(500)


class People():
    sum = 9

    def __init__(self, name, age):
        # print(555)
        self.name = name
        self.age = age


class Student(People):
    ff = 2

    def __init__(self, oo, name, age):
        # print(444)
        self.name = oo
        People.__init__(self, name, age)
        # print(oo)

    @classmethod
    def printname(cls):
        cls.ff += 1
        print(cls.ff)


# stu = Student('ff', 'rr', 7)
stu = People('2','2')
# print(stu.name)
print(People('2','2').sum)
