from enum import Enum


class ColorEnum(Enum):
    blue = 1
    red = 2
    green = 3


class ColorEnum2(Enum):
    blue = 1
    red = 2
    green = 3


print(ColorEnum.blue.value == ColorEnum2.blue.value)
