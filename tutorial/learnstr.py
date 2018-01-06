# print(type(()))
# print(max('12asd'))
# print({1, 2, 3, 4} | {2, 3, 5})
# l = [1, 2, 4, 6, 5, 6, 7, 8]
#
# for i in range(0, len(l), 2):
#     print(l[i])
import tutorial

tutorial.sys.setrecursionlimit(500)


class Student():
    name = 'aa'
    ff = 2

    def __init__(self, name):
        self.name = name
        print(name)
        pass

    @classmethod
    def printname(cls):
        cls.ff += 1
        print(cls.ff)


stu = Student('ff333')
Student.printname()
