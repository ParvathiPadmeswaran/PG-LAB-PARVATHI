class Rectangle:
    def __init__(self, length, width):
         self.length = length
         self.width = width
           
  
    def compute_area(self):
        return self.length * self.width
    
   
    def compute_perimeter(self):
        return 2 * (self.length+self.width)
l= float(input('Please Enter the Length of the Rectangle: '))
w= float(input('Please Enter the Width of the Rectangle: '))
    

object1 = Rectangle(l,w)


area = object1.compute_area()
perimeter = object1.compute_perimeter()


print("Area of Rectangle object = %.2f" %area)
print("Perimeter of Rectangle object= %.2f" %perimeter)


print("-----------------------------------")
print("-----------------------------------")
print("-----------------------------------")


def __init__(self, length1, width1):
         self.length1 = length1
         self.width1 = width1
           
  
def compute_area(self):
        return self.length1 * self.width1

l1= float(input('Please Enter the Length of the Rectangle1: '))
w1= float(input('Please Enter the Width of the Rectangle1: '))
    

object1 = Rectangle(l1,w1)


area1 = object1.compute_area()


print("Area of Rectangle1 object1 = %.2f" %area1)

def __init__(self, length2, width2):
         self.length2 = length2
         self.width2 = width2
           
  
def compute_area(self):
        return self.length2 * self.width2

l2= float(input('Please Enter the Length of the Rectangle2: '))
w2= float(input('Please Enter the Width of the Rectangle2: '))
    

object2 = Rectangle(l2,w2)


area2 = object2.compute_area()


print("Area of Rectangle2 object2 = %.2f" %area2)


if area1 > area2:
            print('Rectangle one\'s area is greater.')
elif area1 < area2:
            print('Rectangle two\'s area is greater.')
elif area1 == area2:
            print('Rectangle\'s areas are equal.')


