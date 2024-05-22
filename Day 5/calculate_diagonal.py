#Create a class Square that inherits from the Rectangle class. Add a method calculate_diagonal() to calculate the diagonal of the square.

import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def calculate_diagonal(self):
        return math.sqrt(2) * self.length


if __name__ == "__main__":
    
    my_square = Square(4)
    
    
    area = my_square.calculate_area()
    print(f"Area: {area}")

   
    perimeter = my_square.calculate_perimeter()
    print(f"Perimeter: {perimeter}")

   
    diagonal = my_square.calculate_diagonal()
    print(f"Diagonal: {diagonal}")
