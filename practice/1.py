class Shape:
    def __init__(self,color="yellow",filled=True):
        self.__color = color
        self.__filled = filled

    def __str__(self):
        return f'({self.__color}, {self.__filled})'

class Circle(Shape):
    radius = 0
    def __init__(self,color,filled,radius):
        self.__color = color
        self.__filled = filled
        self.__radius = radius

    def area(self):
        return 3.14*self.__radius * self.__radius

    def __str__(self):
        return f'({self.__color}, {self.__filled})(radius = {self.__radius})'

def main():
    a = Shape()
    b = Shape("red")
    print(a,b)
    c = Circle("blue", False, 10)
    print(c)
    print(c.area())

main()