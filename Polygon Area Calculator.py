class Rectangle(object):

    # Has a width and height as instance variables
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    # Define string representation of rectangle
    def __repr__(self):
        return("Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")")

    # Define methods to set width and height
    def set_width(self, newwidth):
        self.width = newwidth

    def set_height(self, newheight):
        self.height = newheight

    # Define methods to get area, perimeter, and diagonal
    def get_area(self):
        return(self.width * self.height)

    def get_perimeter(self):
        return(2 * (self.width + self.height))

    def get_diagonal(self):
        return( (self.width**2 + self.height**2) ** 0.5 )

    # Define method to calculate how many other shapes fit inside this one
    def get_amount_inside(self, otherself):
        num = self.get_area() / otherself.get_area()
        if num < 1:
            return(0) # Passed shape cannot fit into this shape
        else:
            return(int(num)) # Want an integer result

    # Define a method to return a string representation of rectangle
    def get_picture(self):
        if (self.height > 50) or (self.width > 50):
            return("Too big for picture.")
        else:
            the_width = self.width
            the_height = self.height
            line = ''
            for i in range(0, the_height):
                line = line + the_width * '*' + '\n'
            return(line)


# Define square class that inherits from rectangle class
class Square(Rectangle):

    def __init__(self, width = 0, height = 1):
        Rectangle.__init__(self, width, height)
        self.width = width
        self.height = width

    # Define method to set side length of square
    def set_side(self, length):
        self.width = length
        self.height = self.width

    # Define string representation of square
    def __repr__(self):
        return("Square(side=" + str(self.width) + ")")
